---
#### Blog Post Template ####

#### Post Information ####
title: "Update on array API adoption in scikit-learn"
date: March 05, 2026

#### Post Category and Tags ####
# Format in titlecase without dashes (Ex. "Open Source" instead of "open-source")
categories:
  - Updates
tags:
  - Open Source
  - Machine Learning
  - Array API
  - Performance

#### Featured Image ####
featured-image: array-api-scikit-learn-2026-feature.png

#### Author Info ####
# Can accomodate multiple authors
# Add SQUARE Author Image to /assets/images/author_images/ folder
postauthors:
  - name: Lucy Liu
    website: https://github.com/lucyleeow
    image: lucyliu.jpeg

# This is a cross-post. Better make it explicit to appease the search engine overlords.
canonical_url: https://labs.quansight.org/blog/array-api-scikit-learn-2026
---
<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>
*Note: this blog post is a cross-post of a [Quansight Labs blog post](https://labs.quansight.org/blog/array-api-scikit-learn-2026).*
The [Consortium for Python Data API Standards](https://data-apis.org/)
developed the [Python array API standard](https://data-apis.org/array-api/)
to define a consistent interface for array libraries, specifing core
operations, data types, and behaviours. This enables 'array-consuming'
libraries (such as scikit-learn) to write array-agnostic code that can
be run on any array API compliant backend. Adopting array API support in scikit-learn
means that users can pass arrays from any array API compliant library to
functions that have been converted to be array-agnostic. This is useful because it
allows users to take advantage of array library features, such as hardware
acceleration, most notably via GPUs.

Indeed, GPU support in scikit-learn has been of interest for a long time - 11 years
ago, we added an entry to our FAQ page explaining that we had no plans to add GPU
support in the near future due to the software dependencies and platform specific
issues it would introduce. By relying on the array API standard, however, these
concerns can now be avoided.

In this blog post, I will provide an update to the array API adoption work in
scikit-learn, since it's initial introduction in version 1.3 two years ago.
Thomas Fan's [blog post](https://labs.quansight.org/blog/array-api-support-scikit-learn)
provides details on the status when array API support was initially added.

## Current status

Since the introduction of array API support in version 1.3 of scikit-learn,
several key developments have followed.

### Vendoring `array-api-compat` and `array-api-extra`

Scikit-learn now vendors both
[`array-api-compat`](https://data-apis.org/array-api-compat/) and
[`array-api-extra`](https://data-apis.org/array-api-extra/).
`array-api-compat` is a wrapper around common array libraries (e.g., PyTorch,
CuPy, JAX) that bridges gaps to ensure compatibility with the standard. It
enables adoption of backwards incompatible changes while still allowing array
libraries time to adopt the standard slowly. `array-api-extra` provides array
functions not included in the standard but deemed useful for array-consuming
libraries.

We chose to vendor these now much more mature libraries in order to avoid the
complexity of conditionally handling optional dependencies throughout the
codebase. This approach also follows precedent, as SciPy also vendors these
packages.

### Array libraries supported

Scikit-learn currently supports CuPy ndarrays, PyTorch tensors (testing
against all devices: 'cpu', 'cuda', 'mps' and 'xpu') and NumPy arrays. JAX
support is also on the horizon. The main focus of this work is addressing
in-place mutations in the codebase. Follow
[PR #29647](https://github.com/scikit-learn/scikit-learn/pull/29647) for
updates.

Beyond these libraries, scikit-learn also tests against `array-api-strict`, a
reference implementation that strictly adheres to the array API specification.
The purpose of `array-api-strict` is to help automate compliance checks for
consuming libraries and to enable development and testing of array
API functionality without the need for GPU or other specialized hardware.
Array libraries that conform to the standard and pass the `array-api-tests` suite
should be accepted by scikit-learn and SciPy, without any additional modifications
from maintainers.

### Estimators and metrics with array API support

The full list of metrics and estimators that now support array API can be
found in our
[Array API support](https://scikit-learn.org/dev/modules/array_api.html#)
documentation page. The majority of high impact metrics have now been
converted to be array API compatible. Many transformers are also now
supported, notably `LabelBinarizer` which is widely used internally and
simplifies other conversions.

Conversion of estimators is much more complicated as it often involves
benchmarking different variations of code or consensus gathering on
implementation choices. It generally requires many months of work by several
maintainers. Nonetheless, support for `LogisticRegression`, `GaussianNB`,
`GaussianMixture`, `Ridge` (and family: `RidgeCV`, `RidgeClassifier`,
`RidgeClassifierCV`), `Nystroem` and `PCA` has been added. Work on
`GaussianProcessRegressor` is also underway (follow at
[PR #33096](https://github.com/scikit-learn/scikit-learn/pull/33096)).

### Handling mixed array namespaces and devices

scikit-learn takes a unique approach among 'array-consuming' libraries by
supporting mixed array namespace and device inputs. This design choice enables
the framework to handle the practical complexities of end-to-end machine
learning pipelines.

String-valued class labels are common in classification tasks and enable users
to work with interpretable categories rather than integer codes. NumPy is
currently the only array library with string array support, meaning that any
workflow involving both GPU-accelerated computation and string labels
necessarily involves mixed array type inputs.

Mixed array input support also enables flexible pipeline workflows. Pipelines
provide significant value by chaining preprocessing steps and estimators into
reusable workflows that prevent data leakage and ensure consistent
preprocessing. However, they have an intentional design limitation: pipeline
steps can transform feature arrays (`X`) but cannot modify target arrays
(`y`). Allowing mixed array inputs means a pipeline can include a
`FunctionTransformer` step that moves feature data from CPU to GPU to leverage
hardware acceleration, while allowing the target array, which cannot be
modified, to remain on CPU.

For example, mixed array inputs enable a pipeline where string classification
features are encoded on CPU (as only NumPy supports string arrays), converted
to torch CUDA tensors, then passed to the array API-compatible
`RidgeClassifier` for GPU-accelerated computation:

```python
from functools import partial

from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer, TargetEncoder

pipeline = make_pipeline(
    # Encode string categories with average target values
    TargetEncoder(),
    # Convert feature array `X` to Torch CUDA device
    FunctionTransformer(partial(torch.asarray, dtype="float32", device="cuda"))
    RidgeClassifier(solver="svd"),
)
```

Work on adding mixed array type inputs for metrics and estimators is underway
and expected to progress quickly. This work includes developing a robust
testing framework, including for pipelines using mixed array types (follow
[PR #32755](https://github.com/scikit-learn/scikit-learn/pull/32755) for details).

Finally, we have also revived our work to support the ability to fit and
predict on different namespaces/devices. This allows users to train models on
GPU hardware but deploy predictions on CPU hardware, optimizing costs and
accommodating different resource availability between training and production
environments. Follow
[PR #33076](https://github.com/scikit-learn/scikit-learn/pull/33076) for
details.

## Challenges

The challenges of array API adoption remain largely unchanged from when this
work began. These are also common to other array-consuming libraries, with a
notable addition: the need to handle array movement between namespaces and
devices to support mixed array type inputs.

### Array API Standard is a subset of NumPy's API

The array API standard only includes widely-used functions implemented across
most array libraries, meaning many NumPy functions are absent. When such a
function is encountered while adding array API support, we have the following
options:

* add the function to `array-api-extra` - this allows other array-consuming
  libraries to benefit and allows sharing of maintenance burden, but is only
  relevant for more widely used functions
* add our own implementation in scikit-learn - these functions live in
  `sklearn/utils/_array_api.py`
* check if SciPy implements an array API compatible version of the function

The `quantile` function illustrates this decision-making process. `quantile`
is not included in the standard as it is not widely used (outside of
scikit-learn) and while it is implemented in most array libraries, the
set of quantile methods supported and their APIs vary. Currently, scikit-learn maintains its
own array API compatible version that supports both weights and NaNs, but due
to the maintenance burden we decided to investigate alternatives. SciPy has an
array API compatible implementation, but it did not support weights. We thus
investigated adding `quantile` to `array-api-extra`; however, during this
effort, SciPy decided to add weight support. Thus, we ultimately decided to
transition to the SciPy implementation once our minimum SciPy version allows.

### Compiled code

Many performance-critical parts of scikit-learn are written using compiled
code extensions in Cython, C or C++. These directly access the underlying
memory buffers of NumPy arrays and are thus restricted to CPU.

Metrics and estimators, with compiled code, handle this in one of two ways:
convert arrays to NumPy first or maintain two parallel branches of code, one
for NumPy (compiled) and one for other array types (array API compatible).
When performance is less critical or array API conversion provides no gains
(e.g., `confusion_matrix`), we convert to NumPy. When performance gains are
significant, we accept the maintenance burden of dual code paths. This was the case for
`LogisticRegression` and the extensive process required for making such implementation
decisions can be seen in the
[PR #32644](https://github.com/scikit-learn/scikit-learn/pull/32644).

### Unspecified behaviour in the standard

The array API standard intentionally leaves some function behaviors
unspecified, permitting implementation differences across array libraries. For
example, the order of unique elements is not specified for the `unique_*`
functions and as of NumPy version 2.3, some `unique_*` functions no longer
return sorted values. This will require code amendments in cases where sorted
output was relied upon.

Similarly, NaN handing is also unspecified for `sort`; however, in this case, all
array libraries currently supported by scikit-learn follow NumPy's NaN
semantics, placing NaNs at the end. This consistency eliminates the need for
special handling code, though comprehensive testing remains essential when
adding support for new array libraries.

### Device transfer

Mixed array namespace and device inputs necessitates conversion of arrays
between different namespaces and devices. This presented a number of
considerations and challenges.

The array API standard adopted DLPack as the recommended
[data interchange](https://data-apis.org/array-api/latest/design_topics/data_interchange.html#data-interchange)
protocol. This protocol is widely implemented in array libraries and offers an
efficient, C ABI compatible protocol for array conversion. While this provided
us with an easy way to implement these transfers, there were limitations.
Cross-device transfer capability was only introduced in DLPack v1, released in
September 2024. This meant that only the latest PyTorch and CuPy versions have
support for DLPack v1. Moreover, not all array libraries have adopted support
yet. We therefore implemented a 'manual' fallback; however, this requires
conversion via NumPy when the transfer involves two non-NumPy arrays.
Additionally, there are no DLPack tests in
[array-api-tests](https://github.com/data-apis/array-api-tests), a testing
suite to verify standard compliance, leaving DLPack implementation bugs easier
to overlook. Despite these challenges, scikit-learn will benefit from future
improvements, such as addition of a C-level API for DLPack exchange that
bypasses Python function calls, offering significant benefit for GPU
applications.

Beyond the technical considerations, there were also user interface
considerations. How should we inform users that these conversions, which incur
memory and performance cost, are occurring? We decided against warnings, which
risk being ignored or becoming a nuisance, and to instead clearly document this
behaviour. Additionally, different devices have different data type limitations;
for example, Apple MPS only supports float32. How best to handle these differences
when performing conversions while ensuring users are informed of precision
impacts is an ongoing consideration.

## A quick benchmark

Array API support for `Ridge` regression was added in version 1.5, enabling
GPU-accelerated linear models in scikit-learn. Combined with support of
several transformers, this allows for complete preprocessing and estimation
pipelines on GPU.

The following benchmark shows the use of the `MaxAbsScaler` transformed
followed by `Ridge` regression using randomly generated data with 500,000
samples and 300 features. The benchmarks were run on AMD Ryzen Threadripper
2970WX CPU, NVIDIA Quadro RTX 8000 GPU and Apple M4 GPU (Metal 3).

The figure below shows the performance speed up on CuPy, Torch CPU and Torch
GPU relative to NumPy.

![Benchmarking of MaxAbsScaler/Ridge pipeline](/assets/images/posts_images/array_api_timings.png "Benchmarking of MaxAbsScaler/Ridge pipeline")

*Performance speedup relative to NumPy across different backends.*

The observed speedups are representative of performance gains achievable with
sufficiently large datasets on datacenter-grade GPUs for linear
algebra-intensive workloads. Mobile GPUs, such as those in laptops, would
typically yield more modest improvements.

Note that scikit-learn's `Ridge` regressor currently only supports 'svd'
solver. We selected this solver for initial implementation as it exclusively
uses standard-compliant functions available across all backends and is the
most stable solver. Support for the 'cholesky' solver is also underway (see
details in [PR #29318](https://github.com/scikit-learn/scikit-learn/pull/29318)).

## Looking forward

As of version 1.8, array API support is still in experimental mode and thus
not enabled by default. However, we welcome early adopters and interested
users to try it and report any
[issues](https://github.com/scikit-learn/scikit-learn/issues). See
[our documentation](https://scikit-learn.org/dev/modules/array_api.html#enabling-array-api-support)
for details on enabling array API support.

Before removing experimental status, we would like to:

* develop a system for automatically documenting functions and classes that
  support array API, potentially with the ability to add relevant details
* mixed array type input support
* support fit and predict on different hardware by allowing conversion of
  fitted estimators between namespaces/devices using utility functions
* improved testing, in particular for the new mixed array type
  functionalities
* improved documentation, including adding an example to our gallery
* decide on the minimal dependency versions required
* get real world user feedback

Alongside these infrastructure and framework improvements, we look forward to
adding support for more estimators. These improvements will deliver
production-ready GPU support and flexible deployment options to scikit-learn
users. We welcome community involvement through testing and feedback
throughout this development phase.

## Acknowledgements

Work on array API in scikit-learn has been a combined effort from many
contributors. This work was partly funded by CZI and NASA Roses.

I would like to thank [Olivier Grisel](https://github.com/ogrisel),
[Tim Head](https://github.com/betatim) and
[Evgeni Burovski](https://github.com/ev-br) for helping me with my array API
questions.
