---
#### Blog Post Template ####

#### Post Information ####
title: "Update on Metadata Routing"
date: August 25, 2026

#### Post Category and Tags ####
# Format in titlecase without dashes (Ex. "Open Source" instead of "open-source")
categories:
  - Updates
tags:
  - Metadata Routing
  - New Feature
  - API
  - Machine Learning

#### Author Info ####
# Can accomodate multiple authors
# Add SQUARE Author Image to /assets/images/author_images/ folder
postauthors:
  - name: Stefanie Senger
    website: https://github.com/StefanieSenger
    image: stefanie_senger.jpg

# This is a cross-post.
canonical_url: https://blog.probabl.ai/update-on-scikit-learn-metadata-routing-api
---
<div>
  {% include postauthor.html %}
</div>
*Note: this blog post is a cross-post of a [Probabl blog post](
https://blog.probabl.ai/update-on-scikit-learn-metadata-routing-api) and based on a talk given at EuroSciPy 2026 in Kraków [1].*

# An Update on scikit-learn's Metadata Routing API

Metadata routing has been introduced gradually in experimental mode since scikit-learn
1.3; coverage is now almost complete, and the feature is mature enough that users can
use it in real workflows.

---

## What is metadata routing?

In scikit-learn, **metadata** is data you want to apply *on top of* your tabular
features and your target. It influences how a function treats `X` and `y`.

You may be familiar with two common kinds of metadata from scikit-learn: `sample_weight`
and `groups`. In addition to these, libraries such as [fairlearn](https://fairlearn.org)
expose their own kinds of metadata, and you can define custom metadata to be used in
business logic, for instance. The benefit of using metadata is usually not a higher
score on the model, but a **more realistic or better tuned model** to begin with.

**Routing** is the mechanism that passes that metadata between several components of a
pipeline to where it is finally used (“consumed”). Before the routing API, using
metadata was only possible in limited cases. With routing enabled, you can pass
`sample_weight` and `groups` through nested meta-estimators, combine third-party objects
with scikit-learn estimators while still forwarding their metadata, and define custom
metrics, scorers, and estimators that consume metadata you invent yourself.

| Without routing (`enable_metadata_routing=False`, the default) | With routing (`enable_metadata_routing=True`) |
| --- | --- |
| Restricted use of `sample_weight` and `groups` | `sample_weight` and `groups` can be used in nested structures |
| Metadata from other libraries cannot be passed through scikit-learn objects| scikit-learn objects can route metadata to objects from other libraries |
| Local use only of custom metadata | Custom metadata can be routed to custom functions and methods |

The Metadata Routing API is a potent and flexible tool that allows users to define in
detail where their metadata gets used. It enables new use cases and enhances
interoperability with third-party libraries. The adoption of the routing API is
spreading in the ecosystem, for example in [fairlearn](https://fairlearn.org),
[imbalanced-learn](https://imbalanced-learn.org/stable),
[skada](https://github.com/scikit-adaptation/skada),
[skorch](https://skorch.readthedocs.io), and [skfolio](https://skfolio.org).

---

## Metadata in the wild

Let's walk through an example.

Imagine a medical study on the effectiveness of a new treatment. Here we have
observational data that is getting used in that study. Features include "sex", "age",
"severity", and whether a patient received a medication; the target is the "recovery
time". This data is naturally biased, because it does *not* come from a randomized
trial. It entails all the imbalance and structure that real world data usually implies.

![Hospital-grouped patient table: features and recovery-time target, with patients
tagged by hospital](/assets/images/posts_images/fig01_hospital_groups.png)

Figure 1: Table of data and target for our example study.

Patients come from different hospitals that differ in systematic factors such as medical
devices, policies, and the socioeconomic mix of patients. A sample's provenance from a
certain hospital is useful for evaluation, but it is not a feature we want the model to
treat like "age" or "severity". Instead we keep it as **groups** with shape
`(n_samples,)`, but separate from `X`.

![Same table with an explicit groups column (Hospital: Blue / Black / Orange) beside
data and target](/assets/images/posts_images/fig02_groups_as_metadata.png)

Figure 2: Table of data and target with an additional `groups` metadata.

During cross-validation we want a realistic estimate of how well a model can generalize.
If samples from the same hospital appear in both the training and validation fold, the
model can look better than it will on a new hospital, which is a form of [data
leakage](https://en.wikipedia.org/wiki/Leakage_(machine_learning)).

Instead of allowing data to be leaked, we use the metadata **groups** that we pass into
cross-validation. scikit-learn's `GroupKFold` keeps each group entirely in either the
train set *or* the validation set for a given fold:

![GroupKFold diagram: three folds where each hospital group is wholly in train or
validation](/assets/images/posts_images/fig03_groupkfold.png)

Figure 3: Training and validation set after splitting with `GroupKFold`.

Passing `groups` into `cross_validate` together with a grouped splitter has worked in
scikit-learn for a long time and keeps functioning the same way:

```python
from sklearn.model_selection import GroupKFold, cross_validate
from sklearn.linear_model import Ridge

ridge = Ridge()
cv = GroupKFold(n_splits=2)
cross_validate(ridge, X, y, cv=cv, groups=groups)
```

For our patient data set, `sample_weight` draws the model's attention toward (or away
from) particular samples. It can be used if biases refer to how features are distributed
or relate to one another. For instance, if we suspect that race, age or socioeconomic
status of a patient determined if they got the new treatment at all, `sample_weight` can
re-balance the over- or under-representation of a certain group of patients and draw the
model to emphasize reducing training error on the higher weighted samples more.

One method to determine `sample_weight` values is inverse probability of treatment
weighting (IPTW) in observational studies (see Wilhelm's walkthrough with scikit-learn
[2]). Probabl Whiteboard Series has also published an exploration on the usefulness of
`sample_weight` from a different angle [3].

In practice, since `Ridge.fit` can consume `sample_weight`, you might reasonably try:

```python
cross_validate(ridge, X, y, cv=cv, sample_weight=sample_weight)
```

…and hit a wall:

```text
TypeError: got an unexpected keyword argument 'sample_weight'
```

In practice you often nest further. Maybe you want to `cross_validate` around a
`GridSearchCV` that tunes `Ridge`, with a scorer that can also take `sample_weight` and
a `GroupKFold` that needs `groups`. Before routing, that stack failed: `cross_validate`
had no way to forward `sample_weight` into the nested `fit` and `score` calls, even
though those methods support it. The same limitation blocked metadata from many
third-party libraries when combined with scikit-learn's cross-validation tools.

If we want fairer, less leaky models to predict the treatment effect for future
patients, we need metadata to move through several layers of other tools by contract.
Metadata Routing API was built to bridge exactly this gap: you can use it to get your
metadata to be used inside the functions that consume it.

---

## Using the metadata routing API

With metadata routing, the code stays close to what you already know. The orange boxed
snippets show you what you need to add to take advantage of the routing in experimental
mode:

![Slide showing the three routing steps: enable metadata routing, pass metadata at the
top level, and set requests where metadata is
consumed](/assets/images/posts_images/fig04_routing_api.png)

Figure 4: The three metadata routing steps: enable, pass at the top, request metadata
where it gets used. See scikit-learn's Metadata Routing User Guide [4] for a full
example. 

1. **Enable** the experimental feature. `set_config(enable_metadata_routing=True)` turns
   routing on. Disable it when you no longer need it.
2. **Pass** metadata once at the top-level tool (here `cross_validate`). That top-level
   object could also be a `Pipeline` or a meta-estimator (an estimator that takes
   another estimator as an argument).
3. **Request** metadata where it should be consumed, with `set_*_request`
   (`set_fit_request`, `set_score_request`, and so on). Grouped splitters such as
   `GroupKFold` already request `groups` by design, so you do not set that yourself.

In experimental mode, users need to use `set_*_request` methods everywhere a metadata
can be consumed. These methods exist to grant users maximum flexibility. In future
releases, these will come with default settings, so that users in the most common use
cases don't need to touch them anymore.

This is the core mental model: **pass at the top, request at the leaves**.

---

## Pipelines that transform validation sets

Metadata routing also unlocks a new feature that was impossible before and rescues data
scientists from awkward workarounds: **validation sets that are transformed alongside
`X`** in a `Pipeline`.

Some estimators such as `HistGradientBoostingClassifier` can split off a validation set
*inside* `fit` for validating early stopping. If used in a `Pipeline` with preprocessing
steps that were applied on the full matrix, that internal split leaks information from
the train set into the validation set. Validation data should be split *before*
transformation, then run through the same steps as training `X`.

`Pipeline`’s `transform_input` parameter (introduced in version 1.6) allows users to
define metadata that should be transformed along with `X` until a step consumes it.
[LightGBM](https://lightgbm.readthedocs.io/en/latest/index.html) estimators are now
compatible with this API. [XGBoost](https://xgboost.readthedocs.io/en/stable) does not
support `transform_input` yet at the time of writing.

The new feature allows users to pass a validation set of their liking through a
`Pipeline`, for instance by performing a `train_test_split` beforehand:

![Pipeline with transform_input=['X_val'] and
HistGradientBoostingClassifier.set_fit_request(X_val=True,
y_val=True)](/assets/images/posts_images/fig05_transform_input.png)

Figure 5: Passing `X_val` through a `Pipeline` with `transform_input` for early
stopping.

Here `X_val` is transformed like `X_train` at every pipeline step until
`HistGradientBoostingClassifier.fit` consumes it for early stopping.

---

## Recent updates and ongoing work

Metadata routing is still experimental, but it is pretty mature in practice. On top of
the pure routing, we continue developing features based on the metadata routing
mechanism. Some are already implemented; others are still in progress:

Already available since 1.9: 
- `TargetEncoder` can use grouped splitters
  ([#33089](https://github.com/scikit-learn/scikit-learn/pull/33089)) 

In progress: 
- Default requests, so users don't need explicit `set_*_request` for common cases
  ([#31413](https://github.com/scikit-learn/scikit-learn/issues/31413))
- Callbacks (e.g. `ScoringMonitor`) can accept metadata such as `X_val` and
  `y_val` ([#34137](https://github.com/scikit-learn/scikit-learn/issues/34137))
- Developer API for customized routing
  ([#34314](https://github.com/scikit-learn/scikit-learn/issues/34314)) (for further
  information see "Developing estimators compliant with metadata routing" [5])
- Visualization and debugging tools for metadata routing
  ([#31535](https://github.com/scikit-learn/scikit-learn/issues/31535))

Once Metadata Routing gets released as a stable feature, the user's code will look as
simple as it always was for default cases, except we can now pass metadata and it will
be used internally.

---

## Takeaway

Metadata routing turns "please somehow get this array into the right nested
`fit`/`predict`/`score` call" into a deliberate contract: pass values at the top and
request them where they are consumed. This unlocks many new use cases and a tighter
integration of scikit-learn compatible libraries in the ecosystem. The API is still
experimental, but worth trying if your real data is grouped, weighted, or otherwise
richer than `(X, y)`.

---

## References

[1] Stefanie Senger, [Scikit-learn’s Metadata Routing
  API](https://github.com/StefanieSenger/Talks/blob/main/2026_Update_on_Metadata_Routing/Update%20on%20Metadata%20Routing.pdf)
  (full deck of slides from talk at EuroSciPy 2026)

[2] Florian Wilhelm, [Causal Inference and Propensity Score
  Methods](https://florianwilhelm.info/2017/04/causal_inference_propensity_score/)
  (IPTW with scikit-learn)

[3] [Probabl Whiteboard Series: Improving models via
  subsets](https://www.youtube.com/watch?v=REIg5NH2SNc)

[4] [Metadata Routing in scikit-learn User Guide](https://scikit-learn.org/stable/metadata_routing.html)

[5] [Developing estimators compliant with metadata
  routing](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html) (scikit-learn docs)