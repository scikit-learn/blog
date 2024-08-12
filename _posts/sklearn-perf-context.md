Title: Performance and scikit-learn (1/4)
Date: 2021-12-16
Category: scikit-learn
Slug: sklearn-perf-context
Lang: en
Authors: Julien Jerphanion
Summary: Context: the current state of scikit-learn performance
Status: Published

## High-level overview of the scikit-learn dependences

scikit-learn is mainly written in Python and is built on top of
some core libraries of the scientific Python ecosystem.

This ecosystem allows _high expressiveness_ and
_interactivity_: one can perform complex operations in a few
lines of code and get the results straight away.

It also allowed setting up simple conventions which makes the
code-base algorithms easy to understand and improve
for new contributors.

It also allows delegating most of the complex operations
to well-tested third-party libraries. For instance, calls
to functions implemented in
[`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html),
[`scipy.linalg`](https://docs.scipy.org/doc/scipy/reference/linalg.html ), and
[`scipy.sparse.linalg`](https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html)
are delegated to
[BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms),
[LAPACK](https://www.netlib.org/lapack/),
and [ARPACK](https://www.caam.rice.edu/software/ARPACK/) interfaces.

## Main reasons for limited performance

The PyData stack is simple but is not tailored for optimal performance
for several reasons.

### CPython internals

CPython -- the main implementation of Python -- is slow.

First, CPython has _an interpreter_: there's a cost in converting Python
instructions into another intermediate representation --
the _byte-code_ -- and executing the instructions by interpreting their
byte-code.

Secondly, nearly every value in CPython is _boxed_ into a `PyObject`
-- implemented as a C struct. As such, simple operations
(like adding two floats) come with a non-negligible dispatch
overhead as the interpreter has to check the type which is unknown
in advance.

Thirdly, CPython for memory management relies on a global
mutex on its interpreter called the _Global Interpreter Lock_[ref]For more information about the GIL, see
[this reference from the Python Wiki](https://wiki.python.org/moin/GlobalInterpreterLock).[/ref].
This mechanism comes in handy but computations are restricted in
most cases to sequential execution in a single thread, removing the benefit
of using threads.

### Memory-hierarchy suboptimal implementations

`numpy` supports high-level operations but this comes with intermediate
and dynamically-allocated arrays.

Moreover, this pattern is inefficient from a memory perspective:
during the execution, blocks of data are moved back and forth
between the RAM and the different CPU caches several times, not
making optimal use of the caches.

For instance, based on this minimalistic toy example:
```python
import numpy as np

A = np.random.rand(100_000_000)
B = np.random.rand(100_000_000)

X = np.exp(A + B)
```

The following is performed:

 - a first temporary array is allocated for `A + B`
 - a second array is allocated to store `np.exp(A + B)` and
 the first temporary array is discarded

This temporary allocation makes the implementation suboptimal
as memory allocation on the heap is slow.

Furthermore, high-level operations on `X` come with more data
moves between the RAM and the CPU than needed to compute the
elements of `X` and hardly make use of the memory hierarchy
and the size of the caches.

### No "bare-metal" data-structures

The Python ecosystem comes with a few high-level containers
such as numpy arrays, and pandas DataFrames.

Contrarily to other languages' standard libraries (like the one of
C++), no "bare-metal" data structures, including heaps, or
memory-contiguous resizable buffers (as implemented in C++ by
[`std::priority_queue`](https://en.cppreference.com/w/cpp/container/priority_queue)
and [`std::vector`](https://en.cppreference.com/w/cpp/container/vector))
are available to implement some algorithms efficiently
from both a computational complexity and a technical perspective.

## Cython: combining the conciseness of Python and the speed of C

In brief, Cython allows transpiling a superset of Python to C code and allows using code that was written in C or C++, which makes bypassing some of CPython's internals possible. Moreover, Cython allows using [OpenMP](https://www.openmp.org/specifications/), an API that allows using lower-level parallelism primitives for implementations written in C or Fortran[ref] For more information on Cython, see [its documentation](https://cython.readthedocs.io/en/latest/).[/ref].

In most cases, features provided by Cython are sufficient enough to reach optimal implementations for many scientific algorithms for which static tasks scheduling -- at the level of C via OpenMP -- is the most natural and optimal one.
Plus, its syntax makes this language expressive enough to get nearly optimal performance while keeping the instructions short and concise -- which is a real advantage for developers coming from Python who are looking for performance and relief for C or C++ developers[ref]Compared to C or C++, Cython is also less verbose and can be integrated Python build system more easily.[/ref].

As such, many algorithms in `scikit-learn` are implemented in Cython performance, some of which use OpenMP when possible. This is for instance the case of `KMeans` which was initially written in Python using numpy and which was rewritten in Cython by Jérémie du Boisberranger, improving the execution time by a factor of 5 for this algorithm[ref]For more information about `KMeans`, see the original contribution,
[`scikit-learn#11950`](https://github.com/scikit-learn/scikit-learn/pull/11950), and [this blog
post](https://scikit-learn.fondation-inria.fr/implementing-a-faster-kmeans-in-scikit-learn-0-23-2/).[/ref].

In the following posts, the case of $k$-nearest neighbors search -- the base routine
for `KNearestNeighborsClassifier`, `KNearestNeighborsRegressor` and other scikit-learn interfaces -- is covered
and a new Cython implementation is proposed.

---

## Notes

