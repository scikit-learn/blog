---
#### Blog Post Template ####

#### Post Information ####
title: "Changes and development of scikit-learn's developer API"
date: December 12, 2024

#### Post Category and Tags ####
# Format in titlecase without dashes (Ex. "Open Source" instead of "open-source")
categories:
  - Updates
tags:
  - Open Source
  - Machine Learning
  - License

#### Featured Image ####
featured-image: BSD_watermark.svg

#### Author Info ####
# Can accomodate multiple authors
# Add SQUARE Author Image to /assets/images/author_images/ folder
postauthors:
  - name: Adrin Jalali
    website: https://adrin.info/
    image: adrin-jalali.jpeg
---
<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

Historically, scikit-learn's API has been divided into public and private. Public API is
intended to be used by users, and private API is used internally in scikit-learn to
develop new features and estimators. However, many of those functionalities have become
essential to develop scikit-learn estimators by third parties who develop them outside
the scikit-learn codebase.

When it comes to our public API, we have very strict and high standards on backward
compatibility. The rule of thumb is that no change should cause a change in users'
code unless we warn about it for two release cycles, which means we give users a year
time to update their code.

On the other hand, we have no such guarantees or constraints on our private API. This
brings an issue to third party developers who would like to use methods used by
scikit-learn developers to develop their estimators. Constantly changing private API
without prior warning brings certain challenges to third party developers which is not
ideal.

As a result, we've been working on creating a developer API which would sit somewhere
between our public and private API in terms of backward compatibility. That means we
intend to try to keep that API stable, and if needed, introduce changes with one release
cycle warning.

In the past few releases, we've slowly introduced more functionalities under this
umbrella. `__sklearn_clone__` and `__sklearn_is_fitted__` are two examples.

In the 1.6 release, we focused on the testing infrastructure and estimator tag system.
Estimator tags used to be private, and we were not sure about their design. In the 1.6
release, new tags are introduced and using them looks like the following:

```python
from sklearn.base import BaseEstimator, ClassifierMixin

class MyEstimator(ClassifierMixin, BaseEstimator):

  ...

  def __sklearn_tags__(self):
    tags = super().__sklearn_tags__()
    # modify tags here
    tags.non_deterministic = True
    return tags
```

The new tags mostly follow the same structure as the old tags, but there are certain
changes to them. The main change is that the old `_xfail_checks` is no longer present
in the new tags. That tag was used to tell the common testing tools about the tests
which are known to fail and are to be skipped. That information is now directly passed
to the test functionalities. The old way of skipping a test was the following:

```python
from sklearn.base import BaseEstimator, ClassifierMixin

class MyEstimator(ClassifierMixin, BaseEstimator):

  ...

  def _more_tags(self):
    return {
      "_xfail_checks": {
        "check_to_skip_name": "this check is known to fail",
        ...
      }
    }
```

And then when calling `check_estimator` or using `parametrize_with_checks` with `pytest`
would automatically ignore those tests for the estimator.

Instead, in this release, you pass that information directly to those methods:

```python
from sklearn.utils.estimator_checks import check_estimator, parametrize_with_checks

CHECKS_EXPECTED_TO_FAIL = {
  "check_to_skip_name": "this check is known to fail",
  ...
}

# Using check_estimator
def test_with_check_estimator():
  check_estimator(MyEstimator(), expected_failed_checks=CHECKS_EXPECTED_TO_FAIL)

# Using parametrize_with_checks
@parametrize_with_checks(
  [MyEstimator()],
  expected_failed_checks=lambda est: CHECKS_EXPECTED_TO_FAIL
)
def test_with_parametrize_with_checks(estimator, check):
  check(estimator)
```

While working on the testing infrastructure, we have also been working on improving our
tests and that means in this release we had a particularly high number of changes in
their names and what they do. The changes will make it easier for developers to fix
issues with their estimators. Note that you can now pass `legacy=False` to both
`check_estimator` and `parametrize_with_checks` to include only strictly API related
tests.

The above changes mean developers need to update their estimators and depending on
what they use, write scikit-learn version specific code to handle supporting multiple
scikit-learn versions. To make that process easier, we've worked on a package called
[`sklearn_compat`](https://github.com/sklearn-compat/sklearn-compat/). You can either
depend on it as a package dependency, or vendor a single file inside your project. At
the moment this project is in its infancy and might change in the future. But hopefully
it helps developers out there.

If you think there are missing functionalities in the developer API, please let us know
and give us feedback on our [issue tracker](
https://github.com/scikit-learn/scikit-learn/issues).
