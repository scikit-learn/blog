Title: Performance and scikit-learn (0/4)
Date: 2021-12-15
Category: scikit-learn
Slug: sklearn-perf
Lang: en
Authors: Julien Jerphanion
Summary:
Status: Published

For more than 10 years, scikit-learn has been bringing machine learning and
data science to the world. Since then, the library always aimed at delivering
quality implementations to its users.

This series of blog post aims at explaining the ongoing work of the
scikit-learn developers to improve the performance of the library by several
orders of magnitude.

This series should be read as follows:

 - [Context: the current state of scikit-learn](sklearn-perf-context.html)
 - [Hardware scalability issue: the k-neighbors search example](sklearn-perf-knn.html)
 - [Pairwise Distances Reduction: abstracting the $k$-nn search pattern](sklearn-perf-pdr.html)
 - [Pairwise Distances Reduction: extra notes](sklearn-perf-pdr-extra.html)

Knowing about the following topics can help understand the blog posts:

 - the main algorithms in machine learning, especially $k$-nearest neighbors
 - basic datastructures and algorithms complexity
 - RAM and the hierarchy of CPU caches
 - some elements of linear algebra
 - some elements of object-oriented design (abstract class, template methods)
 - some elements of C programming (allocation on the heap, pointer arithmetic)
 - some elements of OpenMP (static scheduling and parallel for-loop)
 - Cython


