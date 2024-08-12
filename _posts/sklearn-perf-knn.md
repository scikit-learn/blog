Title: Performance and scikit-learn (2/4)
Date: 2021-12-17
Category: scikit-learn
Slug: sklearn-perf-knn
Lang: en
Authors: Julien Jerphanion
Summary: Hardware scalability issue: the k-neighbors search example
Status: Published

## $k$-nearest neighbors search in scikit-learn

$k$-nearest neighbors search is at the base of many implementations used within scikit-learn.

For instance, it is used in Affinity Propagation, BIRCH, Mean Shift, OPTICS,
Spectral Clustering, TSNE, KNeighbors Regressor, and KNeighbors Classifier.

Whilst many libraries implement approximated versions of $k$-nearest neighbors search to speed-up
the execution time[ref]Approximate nearest neighbors search algorithms come in many different
flavors, and there's even [a benchmark suite comparing them!](https://ann-benchmarks.com/).[/ref], scikit-learn's implementation aims at returning the exact $k$-nearest neighbors.


## Computing chunks of the distance matrix computations

The general steps for $k$-nearest neighbors search are:

 - Compute $\mathbf{D}_d(\mathbf{X}, \mathbf{Y})$, the distance matrix between the vectors of two
 arrays $\mathbf{X}$ and $\mathbf{Y}$.
 - Reduce rows of $\mathbf{D}_d(\mathbf{X}, \mathbf{Y})$ appropriately for the given algorithm:
 for instance, the adapted reduction for $k$-nn search is to return the $k$ smallest indices of values in an ordered set.
In what follows, we call this reduction $\texttt{argkmin}$.
 - Perform extra operations on results of the reductions (here sort values).

Generally, one does not compute $\mathbf{D}_d(\mathbf{X}, \mathbf{Y})$ entirely because its
space complexity is $\Theta(n_x \times n_y)$. Practically,
$\mathbf{D}_d(\mathbf{X}, \mathbf{Y})$ does not fit in RAM for sound datasets.

Thus, in practice, one computes chunks of this dataset and reduced them directly.
This is what was performed as of scikit-learn 1.0[ref][`KNearestNeighbors.kneighbors`](https://github.com/scikit-learn/scikit-learn/blob/c762c407873b8d6417b1c2ff78d19d82550e48d3/sklearn/neighbors/_base.py#L650) is the interface to look for.[/ref].


## Current issues

The current implementation relies on a general parallelization scheme using higher-level functions with
[`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html).

Technically, this is not the most efficient: working at this level with views on numpy arrays moves
large chunks of data back and forth several times between the RAM and the CPUs' caches, hardly
make use of caches, and allocate temporary results.

Moreover, the cost of manipulating those chunks of data in the CPython interpreter causes a non
negligible overhead because they are associated with Python objects which are bound to the
Global Lock Interpreter for counting their references.

Hence, this does not allow getting proper _hardware scalability_: an ideal parallel
implementation of an algorithm would run close to $n$ times faster when running on
$n$ threads on $n$ CPU cores compared to sequentially on $1$ thread.

For instance, the current implementation of $k$-nearest neighbors search of scikit-learn
cannot efficiently leverage all the available CPUs on a machine -- as shown by the figure below.

![Scalability of `kneighbors` as of scikit-learn 1.0](https://user-images.githubusercontent.com/13029839/155144242-6c041729-154b-47aa-9069-3a7d26deef5a.svg)

When using $8$ threads, it only run $\times 2$ faster than the sequential implementation
and adding more threads and CPUs beyond $8$ does not help to get better performance.

In the next blog, we go over the design of a new implementation to improve the scalability of $k$-nn search.

---

## Notes
