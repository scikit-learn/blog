Title: Performance and scikit-learn (3/4)
Date: 2021-12-18
Category: scikit-learn
Slug: sklearn-perf-pdr
Lang: en
Authors: Julien Jerphanion
Summary: Pairwise Distances Reductions: Abstracting the k-nn search pattern
Status: Published


## Context

We have seen that $\text{argkmin}$ is the reduction that is performed on pairwise distances for $k$-nearest neighbors search.

Yet, there exist other reductions over pairwise distances ($\text{argmin}$, threshold filtering, cumulative sum, etc.) which are at the core of the computational foundations of many machine learning algorithms.

This blog post presents a design that takes into account the requirements of the existing implementations
to introduce a set of new abstractions to implement reductions over pairwise distances: `PairwiseDistancesReduction`.  This set of interfaces aims at reimplementing patterns that are similar to the $k$-nn search in Cython, to improve the
performance of its computational foundations, and thus the ones of its user-facing interfaces.

To our knowledge, though some projects like [KeOps](https://www.kernel-operations.io/keops/index.html) implement those patterns efficiently for GPUs, no project implements such operations for CPUs efficiently.

> 💡 This blog post won't introduce every technical detail for the sake of conciseness, maintenance, and to respect the [single source of truth principle](https://en.wikipedia.org/wiki/Single_source_of_truth) as much as possible. The implementations are available in the [`sklearn.metrics._pairwise_distances_reduction`](https://github.com/scikit-learn/scikit-learn/tree/main/sklearn/metrics/_pairwise_distances_reduction) submodule.

> 💡 [This presentation](https://docs.google.com/presentation/d/1RwX_P9lnsb9_YRZ0cA88l3VoEYhiMndQYoKLLF_0Dv0/edit?usp=sharing) gives elements of the design of `PairwiseDistancesReductions`.

## Notation

In what follows, the following notations are used:

 - $p$: the dimension of vectors
 - $[n] \triangleq \{0, \cdots, n - 1\}$
 - $\mathbf{X} \in \mathbb{R}^{n_x \times p}$: a first dataset
 - $\mathbf{X}_{i\cdot} \in \mathbb{R}^{p}$: the $i$-th vector of $\mathbf{X}$
 - $\mathbf{Y} \in \mathbb{R}^{n_y \times p}$: a second dataset
 - $\mathbf{Y}_{j\cdot} \in \mathbb{R}^{p}$: the $j$-th vector of $\mathbf{Y}$
 - $c$: the chunk size, i.e. the number of vectors in a chunk (a group of adjacent vectors)
 - $c_x \triangleq \left\lceil \frac{n_x}{c} \right\rceil$, the number of chunks for $\mathbf{X}$
 - $c_y \triangleq \left\lceil \frac{n_y}{c} \right\rceil$, the number of chunks for $\mathbf{Y}$
 - $(\mathbf{X}_c^{(l)})_{l \in [c_x]}$: the ordered family of all the chunks of $\mathbf{X}$
 - $(\mathbf{Y}_c^{(k)})_{k \in [c_y]}$: the ordered family of all the chunks of $\mathbf{Y}$
 - $\mathbf{C}_\text{chunk_size}\mathbf{(X, Y)} \triangleq \left(\mathbf{X}_c^{(l)}, \mathbf{Y}_c^{(k)}\right)_{(l,k) \in [c_x] \times [c_y] }$: the ordered family of all the pairs of chunks
 - $d$, the distance metric to use

$$
d: \mathbb{R}^{p} \times \mathbb{R}^{p} \longrightarrow \mathbb{R}_+
$$

 - $\mathbf{D}_d(\mathbf{A}, \mathbf{B}) \in \mathbf{R}^{n_a \times n_b}$ the distance matrix for $d$ between vectors of two matrices $\mathbf{A} \in \mathbb{R}^{n_a \times p}$ and $\mathbf{B} \in \mathbb{R}^{n_b \times p}$:

$$
\forall (i, j) \in [n_a]\times [n_b], \quad \mathbf{D}_d(\mathbf{A}, \mathbf{B})_{i,j} = d\left(\mathbf{A}_i, \mathbf{B}_j\right)
$$

 - $k$: parameter for the $\text{argkmin}$ operation at the base of $k$ nearest neighbors search


Moreover, the terms "samples" and "vectors" will also be used interchangeably.

## Requirements for reductions over pairwise distances

The following requirements are currently supported within scikit-learn's implementations:

 - Support for float32 datasets pairs and float64 datasets pairs
 - Support for fused $\{\text{sparse}, \text{dense}\}^2$ datasets pairs, i.e.:
    - dense $\mathbf{X}$ and dense $\mathbf{Y}$
    - sparse $\mathbf{X}$ and dense $\mathbf{Y}$
    - dense $\mathbf{X}$ and sparse $\mathbf{Y}$
    - sparse $\mathbf{X}$ and sparse $\mathbf{Y}$
 - Support all the distance metrics as defined via [`sklearn.metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html)
 - Parallelise computations effectively on all cores
 - Prevent threads' oversubscription[ref]Threads' oversubscription happens when threads are spawned at various levels of parallelism, causing the OS to use more threads than necessary for the execution of the program to be optimal.[/ref] (by OpenMP, joblib, or any BLAS implementations)
 - Implement adapted operations for each reduction ($\text{argmin}$, $\text{argkmin}$, threshold filtering, cumulative sum, etc.)
 - Support generic returned values for reductions (varying number, varying types, varying shapes, etc.)
 - Optimise the Euclidean distance metric computations

## Proposed design

The following design proposes treating the given requirements as independently from one another as possible.

### `DatasetsPair`: an abstract class for manipulating datasets[ref]We use the term "abstract class" here to talk about the design: no such concept exists in Cython.[/ref]

This allows:

 - Supporting float32 datasets pairs and float64 datasets pairs
 - Supporting fused $\{\text{sparse}, \text{dense}\}^2$ datasets pairs via concrete implementation, i.e.:
    - `DenseDenseDatasetsPair`
    - `SparseDenseDatasetsPair`
    - `DenseSparseDatasetsPair`
    - `SparseSparseDatasetsPair`
 - Supporting all the distance metrics as defined via [`sklearn.metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html)

Internally, a `DatasetsPair` wraps $(\mathbf{X}, \mathbf{Y}, d)$ and exposes an interface which allows computing $d(\mathbf{X}_{i\cdot}, \mathbf{Y}_{j\cdot})$ for a given tuple $(i, j)$.

### `PairwiseDistancesReduction`: an abstract class defining parallelization templates

This allows:

 - Parallelising computations effectively on all cores
 - Preventing threads' oversubscription (by OpenMP, joblib, or any BLAS implementations)
 - Supporting generic returned values for reductions (varying number, varying types, varying shapes, etc.)

This is made possible by:

 - setting up a general interface that performs the parallelization of computations on $\mathbf{C}_\text{chunk_size}\mathbf{(X, Y)}$: two strategies of parallelization are implemented as it's worth parallelizing on $\mathbf{X}$
or on $\mathbf{Y}$ depending on the context. To choose one or the other strategy, a simple heuristic comparing $c_x$ and $c_y$ about the number of available threads is used and is sufficient.
 - using a [`threadpoolctl.threadpool_limits` context](https://github.com/joblib/threadpoolctl#setting-the-maximum-size-of-thread-pools) at the start of the execution of the generic parallel template
 - having a flexible Python interface to return results and have the parallel computations be defined agnostically from the data structures being modified in concrete classes[ref]A set of template methods are defined so as to have concrete implementations modify data structures when and where needed.[/ref].

The critical areas of the computations -- that is the computations of the chunk of the distance matrix associated to $\mathbf{C}_\text{chunk_size}\mathbf{(X, Y)}$ and its reduction -- is made abstract. This way, when defining a concrete `PairwiseDistancesReduction`, a sole method is to define up to some eventual python helpers methods[ref]If you are looking for the concrete implementations' critical regions, look for
`_compute_and_reduce_distances_on_chunks`.[/ref].


### `PairwiseDistancesReductionArgKmin`: a first concrete `PairwiseDistancesReduction` for $\text{argkmin}$

For this reduction, one can use [max-heaps](https://en.wikipedia.org/wiki/Heap_(data_structure)) which are by design doing the work of
keeping the first $k$ minimum values with their indices. scikit-learn
current implementation of max-heaps is simple, readable and efficient[ref]Thanks to [Jake VanDerplas](https://vanderplas.com/)![/ref] and can be used to manipulate the data structures that we need[ref]We mainly use heap-allocated buffers that we manipulate through pointers and offsets at the lowest level of this new implementation for maximum efficiency.[/ref].

### Specialising reductions for the Euclidean distance metric

Generally, distances associated with neighbors aren't returned to the user. This allows some optimization.

In the case of the Euclidean distance metric, one can use the Squared Euclidean distance metric as a proxy: it is less costly, it preserves ordering and it can be computed efficiently.

Indeed, $\mathbf{D}^{\odot 2}_d(\mathbf{X}_c^{(l)}, \mathbf{Y}_c^{(k)})$ -- the element-wise squared version of the $(l,k)$-th chunk of $\mathbf{D}_d(\mathbf{X}, \mathbf{Y})$ -- can be computed as follows:

$$
\mathbf{D}^{\odot 2}_d(\mathbf{X}_c^{(l)}, \mathbf{Y}_c^{(k)}) \triangleq \left[\Vert \mathbf{X}_{i\cdot}^{(l)} - \mathbf{Y}_{j\cdot}^{(k)} \Vert^2_2\right]_{(i,j)\in [c]^2} = \left[\Vert \mathbf{X}_{i\cdot}^{(l)}\Vert^2_2 \right]_{(i,j)\in [c]^2} + \left[\Vert \mathbf{Y}_{j\cdot }^{(k)}\Vert^2_2 \right]_{(i, j)\in [c]^2} - 2 \mathbf{X}^{(l)} {\mathbf{Y}^{(k)}}^\top
$$

This allows using two optimizations:

 1. $\left[\Vert \mathbf{X}_{i\cdot}\Vert_2^2\right]_{i \in [n_x]}$ and $\left[\Vert \mathbf{Y}_{j\cdot}\Vert_2^2\right]_{j \in [n_y]}$ can be computed once and for all at the start and be cached. Those two vectors will be reused on each chunk of the distance matrix.

 2. More importantly, $- 2 \mathbf{X}^{(l)} {\mathbf{Y}^{(k)}}^\top$ can be computed using the [GEneral Matrix Multiplication from BLAS Level 3](https://www.netlib.org/lapack/explore-html/d1/d54/group__double__blas__level3_gaeda3cbd99c8fb834a60a6412878226e1.html) -- hereinafter refered to as GEMM. This allows getting the maximum arithmetic intensity for the computations, making use of recent BLAS back-ends implementing vectorised kernels, such as
    [OpenBLAS](https://www.openblas.net/).


For instance `EuclideanPairwiseDistancesArgkmin` is the main specialization of `PairwiseDistancesArgkmin` for the
Euclidean distance metric. This specialization solely recomputes the actual Euclidean distances when the caller asked them to be returned.


### Interfacing `PairwiseDistancesReductions` with scikit-learn's algorithms

As of now, the overall design was covered without mentioning ways they can be plugged with the existing scikit-learn algorithms, progressively migrating most algorithms' back-end to those new implementations.

Furthermore, in the future, specialized implementations for various vendors of CPUs and GPUs can be created.
In this case, we want to have such specialized implementations separated from scikit-learn source code (e.g. by having them in optional and vendor-specific packages) so as to keep `PairwiseDistancesReductions` interfaces vendor-specialization-agnostic but still be able to dispatch the computations to the most adapted and available implementations.

To touch two birds with one tiny stone[ref]Disclaimer: during this work, no animal was killed, nor hurt; nor are and nor will.[/ref], the new implementations can be used conditionally to the yet-supported cases based on provided datasets and executed agnostically from them.

This can be implemented by a `PairwiseDistancesReduction.{is_usable_for,compute}` pattern:

 - `PairwiseDistancesReduction.is_usable_for` returns `True` if any implementation for the provided $(\mathbf{X}, \mathbf{Y}, d)$ can be used. If none is available, the caller can default to the current implementation within scikit-learn.
 - `PairwiseDistancesReduction.compute` returns the results of the reduction. Internally, it is responsible for choosing the most appropriate implementation prior to executing it.

In this context, aforementioned vendor-specific packages could register custom implementations explicitly (i.e. with a python context manager as suggested by Olivier Grisel) or implicitly (by some package reflection when importing relevant interfaces).

## Implementing the design

A few first experiments have been made and converged to [`sklearn#22134`](https://github.com/scikit-learn/scikit-learn/pull/22134), a contribution that proposes integrating the previous interfaces progressively via a feature branch.

## Future work

Further work would treat the last requirements:

 - Support for 32 bits datasets pairs
 - Support for the last fused $\{\text{sparse}, \text{dense}\}^2$ datasets pairs, i.e.:
    - sparse $\mathbf{X}$ and dense $\mathbf{Y}$
    - dense $\mathbf{X}$ and sparse $\mathbf{Y}$
    - sparse $\mathbf{X}$ and sparse $\mathbf{Y}$
 - Implement adapted operations for each reduction (radius neighborhood, threshold filtering, cumulative sum, etc.)

> If you are interested in reading more about this, read [this section from the extra notes](sklearn-perf-pdr-extra.html).

## Acknowledgement

This was a joint work with other core-developers -- namely [Olivier Grisel](https://ogrisel.com/), [Jérémie du Boisberranger](https://github.com/jeremiedbb), [Thomas J. Fan](https://www.thomasjpfan.com/) and [Christian Lorentzen](https://github.com/lorentzenchr).

Finally and more importantly, the implementations presented here are made possible thanks to other notable open-source
projects, especially Cython but also OpenBLAS, which provides fast vectorized kernels implemented in C and assembly for BLAS.


---

## Notes

