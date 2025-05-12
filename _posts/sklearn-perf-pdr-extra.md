Title: Performance and scikit-learn (4/4)
Date: 2021-12-19
Category: scikit-learn
Slug: sklearn-perf-pdr-extra
Lang: en
Authors: Julien Jerphanion
Summary: Pairwise Distances Reductions: extra notes on technical details, benchmarks and further work.
Status: Published

Following up with [this initial post on the design of `PairwiseDistancesReductions`](sklearn-perf-pdr.html),
more details are given regarding experiments' results for performance assessment and about future extensions' design.

## `PairwiseDistancesArgKmin`: Performance improvements

[`KNeighborsMixing.kneighbors`](https://github.com/scikit-learn/scikit-learn/blob/f924bc8a1da541fa63b649046cedbc51d1024464/sklearn/neighbors/_base.py#L647) is the _de facto_ best proxy
for accessing performance of the implementation used in most cases : `EuclideanPairwiseDistancesArgKmin`.

In what follows, experiments testing this interface are made on two aspects: hardware scalability and computational efficiency.

### Hardware scalability

This is the hardware scalability of `kneighbors` in scikit-learn `1.0`:

![Scalability of argkmin reductions in scikit-learn 1.0](https://user-images.githubusercontent.com/13029839/155144242-6c041729-154b-47aa-9069-3a7d26deef5a.svg)

This is the hardware the scalability of `kneighbors` as proposed in `sklearn#22134`:

![Scalability of argkmin reductions using the proposed `PairwiseDistancesReductionArgKmin`](https://user-images.githubusercontent.com/13029839/155096010-d143649b-3904-4d80-b3d0-5017724d19ad.svg)

The proposed implementation provides a better hardware scalability than the previous one.

The plateau after 64 cores can be explained by Amdahl's law[ref]Gene M. Amdahl. 1967. Validity of the single processor approach to achieving large scale computing capabilities. In Proceedings of the April 18-20, 1967, spring joint computer conference (AFIPS '67 (Spring)). Association for Computing Machinery, New York, NY, USA, 483–485. DOI: [`https://doi.org/10.1145/1465482.1465560`](https://doi.org/10.1145/1465482.1465560)[/ref]: as the number of threads grows, the parallel portion of
the
algorithm becomes negligeable compared to its sequential portion, reaching a limit in term of computational time -- the execution period of the sequential part -- hence causing speed-up ratio to stop increasing. Moreover, the small drop in speed-up for 128 threads can be explained by the overhead of setting up threads which becomes non-negligeable compared to the actual computations made in each thread.

### Computational efficiency of `EuclideanPairwiseDistancesArgKmin`

On distributions of GNU/Linux, [`perf(1)`](https://man7.org/linux/man-pages/man1/perf.1.html) comes in handy to introspect a program execution in details[ref]If you are using another OS, `perf(1)` won't be usable. Still, you should be able to perform similar inspections using [`dtrace`](https://www.brendangregg.com/dtrace.html).[/ref].

Here, we inspect where CPUs cycles are spent, as well as L3 caches misses and L3 caches hits using the following script on a machine having 20 physical cores[ref]The CPUs used are: Intel(R) Xeon(R) CPU E5-2660 v2 @ 2.20GHz[/ref]:

```python
# kneighbors_perf.py

import numpy as np
import os
from sklearn.neighbors import NearestNeighbors


if __name__ == "__main__":

    n_train = 100_000
    n_test = 100_000
    n_features = 30

    rng = np.random.RandomState(0)

    # We persist datasets on disk so as to solely have
    # `perf(1)` introspect the events for the core
    # of the computations: `kneighbors`.

    X_train_file = "X_train.npy"
    X_test_file = "X_test.npy"

    if os.path.exists(X_train_file):
        X_train = np.load(X_train_file)
    else:
        X_train = rng.rand(n_train, n_features)
        np.save(X_train_file, X_train)

    if os.path.exists(X_test_file):
        X_test = np.load(X_test_file)
    else:
        X_test = rng.rand(n_test, n_features)
        np.save(X_test_file, X_test)

    est = NearestNeighbors(n_neighbors=10, algorithm="brute").fit(X=X_train)

    # FastEuclideanPairwiseDistancesArgKmin will be used under the hood.
    est.kneighbors(X_test)
```

And the following call to [`perf-record(1)`](https://man7.org/linux/man-pages/man1/perf-record.1.html)[ref]You might need to adapt the events because they change from one architecture to another. See [`perf-list(1)`](https://man7.org/linux/man-pages/man1/perf-list.1.html).[/ref]:

```sh
perf record -e \
    cycles,\                         # Record CPU cycles
    mem_load_uops_retired.llc_miss,\ # Record L3 caches' misses
    mem_load_uops_retired.llc_hit \  # Record L3 caches' hits
    python kneighbors_perf.py
```

this dumps a binary `perf.data` file which can be explored using [`perf-report(1)`](https://man7.org/linux/man-pages/man1/perf-report.1.html):

```sh
perf report --hierarchical \ # to be able to see overhead hierarchically
            --inline         # to annotate with callgraph addresses
```

**On CPUs cycles**

This is the report for the `cycles` events.

```
Samples: 543K of event 'cycles:u', Event count (approx.): 335205056539

-  100.00%        python                                                       ▒
   -   68.07%        libopenblasp-r0.3.18.so                                   ▒
          57.45%        [.] dgemm_kernel_SANDYBRIDGE                           ◆
           4.51%        [.] dgemm_beta_SANDYBRIDGE                             ▒
           3.33%        [.] dgemm_incopy_SANDYBRIDGE                           ▒
           2.59%        [.] dgemm_oncopy_SANDYBRIDGE                           ▒
           0.09%        [.] dgemm_tn                                           ▒
           0.04%        [.] blas_thread_server                                 ▒
           0.01%        [.] dgemm_                                             ▒
           0.01%        [.] ddot_kernel_8                                      ▒
           0.01%        [.] blas_memory_free                                   ▒
           0.01%        [.] blas_memory_alloc                                  ▒
           0.00%        [.] dgemm_small_matrix_permit_SANDYBRIDGE              ▒
           0.00%        [.] dot_compute                                        ▒
           0.00%        [.] ddot_k_SANDYBRIDGE                                 ▒
           0.00%        [.] ddot_                                              ▒
   -   22.17%        _pairwise_distances_reduction.cpython-39-x86_64-linux-gnu.▒
          22.16%        [.] __pyx_f_7sklearn_7metrics_29_pairwise_distances_red▒
           0.00%        [.] __pyx_memoryview_slice_memviewslice                ▒
           0.00%        [.] __pyx_f_7sklearn_7metrics_29_pairwise_distances_red▒
           0.00%        [.] __pyx_f_7sklearn_7metrics_29_pairwise_distances_red▒
           0.00%        [.] __pyx_f_7sklearn_7metrics_29_pairwise_distances_red▒
           0.00%        [.] __pyx_f_7sklearn_7metrics_29_pairwise_distances_red▒
   -    9.25%        _heap.cpython-39-x86_64-linux-gnu.so                      ▒
           9.24%        [.] __pyx_fuse_1__pyx_f_7sklearn_5utils_5_heap_heap_pus▒
           0.01%        [.] __pyx_fuse_1__pyx_f_7sklearn_5utils_5_heap_simultan▒
   +    0.20%        python3.9                                                 ▒
   -    0.15%        libgomp.so.1.0.0                                          ▒
           0.15%        [.] do_wait                                            ▒
           0.00%        [.] gomp_barrier_wait_end                              ▒
           0.00%        [.] gomp_thread_start                                  ▒
           0.00%        [.] gomp_team_barrier_wait_end                         ▒
           0.00%        [.] futex_wake                                         ▒
```

Most of the CPUs cycles are spent in GEMM. The rest of them are mainly used
to iterate on the chunks of the distance matrix, pushing values and indices on the
max-heaps.

Note that the calls of the parallelisation using OpenMP via Cython and
of the CPython interpreter comes with negligeable overhead.

Assuming most readers are curious and like getting into details, we can actually look at the
kind of CPU instructions which are being used in `dgemm_kernel_SANDYBRIDGE`[ref]Unmangling `dgemm_kernel_SANDYBRIDGE`: this is the core (`kernel`) of the float64/double (`d`) implementation of GEMM for the [Sandy Bridge architecture](https://en.wikichip.org/wiki/intel/microarchitectures/sandy_bridge_(client)).[/ref], the critical
region.

```
Samples: 543K of event 'cycles:u', 4000 Hz, Event count (approx.): 335205056539
dgemm_kernel_SANDYBRIDGE
  0.94 │        vmulpd       %ymm1,%ymm3,%ymm7
  0.50 │        vpermilpd    $0x5,%ymm2,%ymm3
  0.52 │        vaddpd       %ymm14,%ymm6,%ymm14
  1.11 │        vaddpd       %ymm12,%ymm7,%ymm12
  1.55 │        vmulpd       %ymm0,%ymm4,%ymm6
  0.25 │        vmulpd       %ymm0,%ymm5,%ymm7
  0.51 │        vmovapd      0xc0(%rdi),%ymm0
  1.81 │        vaddpd       %ymm11,%ymm6,%ymm11
  1.65 │        vaddpd       %ymm9,%ymm7,%ymm9
  0.71 │        vmulpd       %ymm1,%ymm4,%ymm6
  0.33 │        vmulpd       %ymm1,%ymm5,%ymm7
  0.77 │        vaddpd       %ymm10,%ymm6,%ymm10
  2.08 │        vaddpd       %ymm8,%ymm7,%ymm8
  0.86 │        vmovapd      0xe0(%rdi),%ymm1
  0.85 │        vmulpd       %ymm0,%ymm2,%ymm6
  0.85 │        vperm2f128   $0x3,%ymm2,%ymm2,%ymm4
  0.97 │        vmulpd       %ymm0,%ymm3,%ymm7
  0.85 │        vperm2f128   $0x3,%ymm3,%ymm3,%ymm5
  0.22 │        add          $0x100,%rdi
  0.38 │        vaddpd       %ymm15,%ymm6,%ymm15
  1.62 │        vaddpd       %ymm13,%ymm7,%ymm13
  1.12 │        prefetcht0   0x2c0(%rdi)
  0.23 │        vmulpd       %ymm1,%ymm2,%ymm6
  0.80 │        vmovapd      (%rsi),%ymm2
```

Most of the instructions there are SIMD instructions.

If the reader is interested in knowing how those instructions are used, they can have a look at [`OpenBLAS/kernel/x84_64/dgemm_kernel_4x8_sandy.S`](https://github.com/xianyi/OpenBLAS/blob/8cec83bdfb82effda2075309af5ca36df79f1a8e/kernel/x86_64/dgemm_kernel_4x8_sandy.S) which comes which a setup of compilers' macros to define the computations at a high-level in assembly.

**On L3 cache hits and L3 cache misses**

One can inspect the report of the `mem_load_uops_retired.llc_miss` events for L3 cache misses[ref]`"llc"` in `"llc_miss"` stands for "last level cache", which on most architectures is the L3 -- i.e. third level -- cache.[/ref]:
```
Samples: 88  of event 'mem_load_uops_retired.llc_miss:u', Event count (approx.):
543K cycles:u                                                                  ▒
-  100.00%        python                                                       ▒
   -   82.95%        libopenblasp-r0.3.18.so                                   ▒
          81.82%        [.] dgemm_incopy_SANDYBRIDGE                           ▒
           1.14%        [.] dgemm_kernel_SANDYBRIDGE                           ▒
   +    7.95%        [unknown]                                                 ▒
   -    6.82%        _pairwise_distances_reduction.cpython-39-x86_64-linux-gnu.▒
           6.82%        [.] __pyx_f_7sklearn_7metrics_29_pairwise_distances_red▒
   +    2.27%        python3.9                                                 ▒
                                                                               ▒
```

One can inspect the report of the `mem_load_uops_retired.llc_hit` events for L3 cache hits:
```
Samples: 984  of event 'mem_load_uops_retired.llc_hit:u', Event count (approx.):
543K cycles:u                                                                  ▒
-  100.00%        python                                                       ▒
   -   66.26%        libopenblasp-r0.3.18.so                                   ▒
          31.00%        [.] dgemm_kernel_SANDYBRIDGE                           ▒
          19.21%        [.] dgemm_incopy_SANDYBRIDGE                           ▒
          10.16%        [.] dgemm_oncopy_SANDYBRIDGE                           ▒
           3.66%        [.] dgemm_tn                                           ▒
           1.12%        [.] blas_memory_alloc                                  ▒
           0.51%        [.] dgemm_                                             ▒
           0.41%        [.] blas_memory_free                                   ▒
           0.20%        [.] dgemm_beta_SANDYBRIDGE                             ▒
   +   16.36%        [unknown]                                                 ▒
   +    8.84%        python3.9                                                 ▒
   -    5.08%        _pairwise_distances_reduction.cpython-39-x86_64-linux-gnu.▒
           4.98%        [.] __pyx_f_7sklearn_7metrics_29_pairwise_distances_red▒
           0.10%        [.] __pyx_memoryview_slice_memviewslice                ▒
   +    1.83%        _heap.cpython-39-x86_64-linux-gnu.so                      ▒
   +    0.71%        libpthread-2.28.so                                        ▒
   +    0.30%        ld-2.28.so                                                ▒
   +    0.30%        libc-2.28.so                                              ▒
   +    0.20%        _cython_blas.cpython-39-x86_64-linux-gnu.so               ▒
```

The L3 cache hits and misses happens exactly where we ought them to -- that is in the
critical region computing chunks of the distance matrix with GEMM.

In the critical region, one instruction out of ten[ref]This is a rough estimation based on the number
of sampled events, namely 984 for L3 cache hits and 88 for L3 caches misses.[/ref] is missing the L3 cache,
showing that the data-structures used to compute the chunks of the distance matrix generally stay the
L3 caches as intended[ref]For maximum performance, one can adapt $\text{chunk_size}$ for the L3 cache size of the
machine they use. This can be done changing the `pairwise_dist_chunk_size` option with `sklearn.set_config`.[/ref].

### Conclusion

In what we just have covered:

 - The computations scale linearly with respect to the number of threads used, reaching theoretical limits.
 - The interactions with CPython interpreter are minimized.
 - The L3 caches are properly used.
 - SIMD instructions are effectively used in critical sections.

Hence, this shows that the parallel execution of the algorithm is efficient[ref]If this can be made more efficient, feel free to propose in another dedicated PR![/ref].

## float32 datasets pairs support for `PairwiseDistancesReduction`

### Design

The implementation whose details have been covered hereinbefore only address the case of pair of float64 datasets pairs. The support for to 32bit datasets pairs can be addressed using [Tempita](https://pyrocore.readthedocs.io/en/latest/tempita.html) so as to expand the previous interfaces support for float64 to float32[ref]Cython does not support templating but Tempita allows treating most cases needing it.[/ref]. The full design proposal and performance assessement is given
in
[`sklearn#22590`](https://github.com/scikit-learn/scikit-learn/pull/22590).

### Hardware scalability

The current experimentations show that the port of `PairwiseDistancesArgKmin` for 32bit datasets also has a good hardware scalability:

![Hardware scalability of `PairwiseDistancesReductionArgKmin` on 32bit datasets](https://user-images.githubusercontent.com/13029839/155859972-637795e7-b959-4cba-afcc-369b0e84d92e.png)

Its integration first necessitates adapting the test suite for 32bit datasets.

## `PairwiseDistancesRadiusNeighborhood`: a concrete `PairwiseDistancesReductions` for radius-based querying

### Design

The reductions for the radius neighborhood queries can efficiently be implemented using resizable buffers. In Cython, this can easily be implemented using `std::vectors`, with [some adaptation to return them as numpy arrays safely](https://github.com/cython/cython/issues/4487). This has been implemented in [`sklearn#22320`](https://github.com/scikit-learn/scikit-learn/pull/22320).

### Hardware scalability

The implementation offer a better hardware scalability than the previous one:

![Hardware scalability of `PairwiseDistancesRadiusNeighborhood` without mimalloc](https://user-images.githubusercontent.com/13029839/155114222-f6d0cc14-786b-4c3b-9bdb-c4a46ef7a944.png)

Yet, this new implementation suffers from concurrent reallocation in threads, namely when vectors' buffers are being reallocated when new elemented are pushed-back. This concurrent reallocation causes some drops in performance as calls to `malloc(3)` (used under the hood for reallocations of `std::vectors`' buffers) lock by default in the compilers' standard libraries' implementations[ref]This is for instance the case in `malloc_state`, one of the main C structures in [the implementation of
`malloc(3)`
in `glibc`](https://sourceware.org/git/?p=glibc.git;a=blob;f=malloc/malloc.c;hb=HEAD#l1832).[/ref].

A simple alleviation for this is to use another implementation of `malloc(3)` such as [`mimalloc`](https://www.microsoft.com/en-us/research/publication/mimalloc-free-list-sharding-in-action/)'s[ref]For more information, see [this gist](https://gist.github.com/jjerphan/17d38a21a85931b448886087b11d2d19).[/ref], which limits race conditions in threads and thus improve the hardware scalability:

![Hardware scalability of `PairwiseDistancesRadiusNeighborhood` with mimalloc](https://user-images.githubusercontent.com/13029839/155114219-6c2d5434-52fd-4b22-a0dc-5f6655fae639.png)

## Subsequent work

Ideas of subsequent work are listed here on [`sklearn#25888`](https://github.com/scikit-learn/scikit-learn/issues/25888).

Finally, many things can be imagined for the second point. Some other and similar patterns using Gram matrices of positive definite kernels[ref]Hofmann, Thomas and Schölkopf, Bernhard and Smola, Alexander J., Kernel methods in machine learning. DOI: [`https://dx.doi.org/10.1214/009053607000000677`](https://dx.doi.org/10.1214/009053607000000677)[/ref] instead of distance matrices exist and could be optimised.

---

## Notes
