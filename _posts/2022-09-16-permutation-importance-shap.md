---
title: "Explaining machine learning models with permutation importance and SHAP"
date: September 16, 2022

categories:
  - Technical
tags:
  - Machine Learning

featured-image: jml.png

postauthors:
  - name: Lucy Liu
    website: https://twitter.com/lucyleeow
    email: lliu@quansight.com
    image: lucyliu.jpeg
---

<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>


Understanding why a machine learning model produces an output is useful for a
variety of reasons; user trust, bias detection, debugging and opportunity
to improve the model. A number of methods have been developed to aid model
interpretation, which are particularly useful for complex models. In this post
we will compare two methods; permutation importance, implemented in
scikit-learn, and SHAP (**SH**apley **A**dditive ex**P**lanations).

## Permutation importance

Permutation importance uses the decrease in model score, after shuffling
the values of a feature, to measure how important each feature is. It can
be calculated using the scikit-learn function
[`permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance):

```python
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

# Only use a subset of the california housing dataset to speed up
# computation
cal_housing = fetch_california_housing()
y = cal_housing.target[::10]
X = pd.DataFrame(data=cal_housing.data[::10, :], columns=cal_housing.feature_names)
X.head()

# Split data into training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=7)

# Fit the model with our training subset
reg = RandomForestRegressor(max_depth=10, n_jobs=2, random_state=7)
reg.fit(X_train, y_train)

# Calculate permutation importances on the test subset using the default score
# metric of `RandomForestRegressor`: R²
perm_import = permutation_importance(
    reg, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)
sorted_idx = perm_import.importances_mean.argsort()

# Plot decrease in R² value for each permutation
fig, ax = plt.subplots()
ax.boxplot(
    perm_import.importances[sorted_idx].T,
    vert=False,
    labels=X.columns[sorted_idx],
)
ax.set_title("Permutation Importances")
fig.tight_layout()
plt.show()
```

![Boxplot of permutation importances](/assets/images/posts_images/permutation_importances.png)

The above plot shows that `MedInc` (median income) causes by far the biggest
drop in R² score whereas `AveBedrms` and `Population` seem to have
almost no effect.

**Considerations**

* Permutation importance is linked to the score metric used, thus selecting
  an appropriate metric for your needs is essential.
* Permutation importance can be calculated with either the training or
  testing subset and each provides different information about the model.
  Using the training subset shows what the model has learned to use for
  making predictions. Using the testing subset shows what is actually useful
  when making predictions on novel data. Features that the model is able to
  use to overfit on the training data will appear more important when using
  the training data than the testing data. This can be seen in
  [this scikit-learn example](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)
  where random features are added into the dataset.
* Permutation importance depends on the true `y` to quantify the ability
  of features to contribute to correct predictions, contrary to SHAP which
  quantifies the ability of features to contribute to changes to the
  decision function, irrespective of whether this improves the accuracy of
  the model.

**Advantages**

* Permutation importances are easy to interpret and provide information on
  the global importance of each feature.
* Permutations can be performed on original feature values or transformed
  feature values. Consequently importances would be either interpreted
  in the original feature space or the transformed feature space.
  In scikit-learn this is achieved by either using an estimator or a
  [`pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
  as input to the `permutation_importance` function.
  Only estimators are accepted as arguments in the SHAP package, meaning
  importance values would need to be interpreted in the transformed
  feature space.
* Permutation importances are error ratios, where 1 means no
  difference between error with and without permutation. This means
  these values are comparable between different models and problems.

**Disadvantages**

* Feature permutation destroys all dependency between features. This means
  the permutation importance value represents the combination of
  the main effect and any interaction effects with other features. Take
  for example two features that interact with each other. The interaction
  effects would be 'accounted for' twice, once in the importance value of
  each feature. This means that the decrease in score from permuting each
  feature would not add up to equal the overall decrease in score from
  permuting all features, unless there were no interaction effects between
  features.
* Permutation importance assumes independence between features. The effect
  is that the 'importance' is split between correlated features. See
  [this scikit-learn example](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)
  for a demonstration of this.
* Permutation can result in unrealistic data points.
* Permutation importances can only be used to compute a global "explanation",
  a decomposition of the impact of different features for a full dataset.
  Unlike SHAP, it cannot provide local "explanations" for individual samples.

## SHAP

Shapley values are an idea from coalition game theory to fairly attribute
value to players of a cooperative game. Applying this method to model
explanations, the features become the players and shapley values attribute the
prediction output of the model amongst the features. It is calculated as the
average marginal contribution of each feature, across all possible feature
combinations. These values satisfy a number of good properties and are thus
deemed a fair way to 'split' the prediction output between the features.

SHAP are shapley values of a conditional expectation function of the original
model, attributing to each feature the change in model prediction when
conditioning on that feature. They can be interpreted as how much a
feature contributes to the prediction, for a specific sample, compared to the
average prediction for the dataset. SHAP values are represented as a linear model
(additive feature attribution method) of feature subsets. Practically, the
predicted outcome is evaluated for all possible subsets of features, with and
without the feature in question. This allows SHAP to account for interaction
effects between features but makes computation very expensive as the number of
possible feature subsets increases exponentially. A number of
approximation methods have been proposed, including the model-agnostic
KernelSHAP and model-specific TreeSHAP. KernelSHAP combines the concepts of
LIME (local surrogate model of feature importance) and shapley values.
It calculates the predictions for a sample when different subsets of
the features are 'missing', simulating missingness via  a background
value for that feature. These predictions are then used to
fit a linear model whose predictions match that of the original model as
closely as possible. The coefficients of the linear 'explanation' model are
the SHAP values. TreeSHAP is designed for tree-based models and uses
the difference between the conditional expectation of feature subsets with and
without the feature of interest to estimate SHAP values.

Several SHAP approximation methods are implemented in the Python library
`SHAP <https://github.com/slundberg/shap>`_. SHAP methods implementated here
support models from various packages, including scikit-learn, XGBoost and Keras.
Below is an example using the SHAP package and a scikit-learn estimator.

```python
import shap

# By default `Explainer` will select the best algorithm to estimate SHAP,
# given the model passed. Below we are passing a tree based model so the
# algorithm used will be TreeSHAP
explainer = shap.Explainer(reg)
# Calculate SHAP values for test data set
shap_values = explainer(X_test)
```

`shap_values` is an 'explanation object'. Some useful attributes include:

* `values`: the SHAP values
* `base_values`: the global mean prediction
* `data`: the data the SHAP values have been calculated for

SHAP values for each feature and each data point of `X_test` are calculated.
We can see that `values` is the same shape as `X_test`:

```python
print(f"SHAP values shape: {shap_values.values.shape}")
print(f"X_test shape: {X_test.shape}")
```

gives:

```
SHAP values shape: (516, 8)
X_test shape: (516, 8)
```

Exploring the SHAP values of the first data point using `shap.plots.waterfall`:

![Waterfall plot of SHAP values](/assets/images/posts_images/shap_waterfall.png)

The SHAP values for each feature 'pushes' the mean prediction (the expected
value) higher (positive SHAP value) or lower (negative SHAP value).
The SHAP values for one data point should sum to the difference between the
prediction output by our model `reg` and the `base_value`:

```python
prediction = reg.predict(X_test.iloc[[0]])
print(
  "Difference between model prediction and base value: "
  f"{(prediction - shap_values.base_values[0])[0]:.2f}"
)
print(f"Sum of SHAP values: {shap_values[0].values.sum():.2f}")
```

```
Difference between model prediction and base value: -1.13
Sum of SHAP values: -1.13
```

We can also plot a summary of all the SHAP values:

![Waterfall plot of SHAP values](/assets/images/posts_images/shap_beeswarm.png)

In the plot above, each dot represents the SHAP value of one feature and one
sample. The features are ordered from most important (highest mean absolute
SHAP value) at the top to least important at the bottom. Note that the dots
cluster around 0 (no contribution) more and more as you go down. The dots are
also colored by the value of the feature. Looking at the `MedInc` feature,
you can clearly see that as feature value increases, SHAP value generally
increases as well.

**Advantages**

* This method allows you to compute feature importances for individual
  samples (local explanations). This can then be extended to global
  explanations by statistically summarizing local explanations in some
  way (e.g., taking average)
* Interaction effects are accounted for, unlike in permutation importances.
  For each sample, the contribution of each feature add up to the overall
  prediction, as shown above.

**Disadvantages**

* SHAP are very computationally expensive, especially when there
  are a large number of features (as possible combinations of
  features exponentially increases). SHAP methods do differ in their computation
  times though, for example TreeSHAP is able to compute SHAP values in
  polynomial time while KernelSHAP does it in exponential time.
* SHAP also assumes independence between features. Similar to
  permutation importance, the result is that 'contributions' will be split
  between correlated features.
* Certain SHAP methods (e.g., KernalSHAP) rely on evaluating the model on
  data points outside of the actual data distributon, which can be unrealistic.
* For certain feature distributions, the SHAP values of non-additive models may
  uninformative.
* SHAP does not take into account model performance. It would thus
  be valuable to first assess model performance before investigating
  feature importances using this method.

## Comparison

In practice, both methods will generally order features similarly in terms
of their importance in a model. If you compare with the permutation importance
plot with the beeswarm SHAP plot, you will notice that the order of features is
roughly the same. However, there are some important differences and practical
considerations between the methods summarized below:

| SHAP                                         | Feature importance                                   |
|----------------------------------------------|------------------------------------------------------|
| Model-agnostic                               | Model-agnostic                                       |
| Provides local and global importances        | Provides global importance only                      |
| Assumes independence between features        | Assumes independence between features                |
| Accounts for interaction between features    | Does not account for interaction<br>between features |
| Computationally expensive                    | Less computationally expensive                       |
| Does not take model performance into account | Takes model performance into account                 |

The last point is of particular interest. SHAP values quantify the contribution
of each feature to the prediction output, irrespective of whether this improves
the model accuracy, unlike permutation importances. This can be seen in the
example below where we add some noise to our target (`y`) and allow our model
to overfit. For permutation importances, there is a clear difference between
the importance (reduction in R²) between the test set and the train set. This
is because the model was allowed to overfit, resulting in better performance
on the train set than the test set, leading to higher importance values.

```python
# Add noise
y_noise = y + np.random.normal(0, y.std(), y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y_noise, random_state=7)

# fit the model, increasing `max_depth` to overfit the model
reg = RandomForestRegressor(max_depth=100, n_jobs=2, random_state=7)
reg.fit(X_train, y_train)

# calculate permutation importances on the test subset
perm_import_test = permutation_importance(
    reg, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)
sorted_idx_test = perm_import_test.importances_mean.argsort()
# calculate permutation importances on the train subset
perm_import_train = permutation_importance(
    reg, X_train, y_train, n_repeats=10, random_state=42, n_jobs=2
)

# Function for creating side by side boxplots
def plot_boxplots(test_data, train_data, method, legend_loc):
    fig, ax = plt.subplots(figsize=(10, 7))
    # Plot test importances
    box_test = ax.boxplot(
        test_data,
        positions=1 + np.arange(test_data.shape[1]) * 2.2,
        vert=False,
        patch_artist=True,
        manage_ticks=False,
        medianprops={"color": "white", "linewidth": 0.5},
        boxprops={"facecolor": "blue"},
    )
    # Plot train importances
    data = shap_values_train.values
    box_train = ax.boxplot(
        train_data,
        positions=1.6 + np.arange(train_data.shape[1]) * 2.2,
        vert=False,
        manage_ticks=False,
        patch_artist=True,
        medianprops={"color": "white", "linewidth": 1},
        boxprops={"facecolor": "darkgoldenrod"},
    )
    ax.set_title(f"{method} (noisy target & overfit model)", fontsize=15)
    plt.yticks(
      1.4 + np.arange(data.shape[1]) * 2.2, X.columns[sorted_idx_test], fontsize=12
    )
    ax.legend(
        [box_train["boxes"][0], box_test["boxes"][0]],
        ["Test", "Train"],
        loc=legend_loc,
        fontsize=15,
    )
    fig.tight_layout()
    plt.show()

# Plot boxplot
plot_boxplots(
  perm_import_test.importances[sorted_idx_test].T,
  perm_import_train.importances[sorted_idx_test].T,
  "Permutation Importances",
  "lower right",
)
```

![Side-by-side boxplot of permutation importances in overfit model](/assets/images/posts_images/permutation_importances_overfit.png)

If we use the overfit model and calculate SHAP values for the test and train
set, we can see that SHAP values are very similar between the test and train
sets. It is advisable to evaluate the performance of your model before
calculating SHAP values.

```python
# Calculate SHAP value for train and test sets
explainer = shap.Explainer(reg)
shap_values_test = explainer(X_test)
shap_values_train = explainer(X_train)
# Plot boxplots
plot_boxplots(
  shap_values_test.values, shap_values_train.values, "SHAP", "upper right"
)
```

![Side-by-side boxplot of SHAP values in overfit model](/assets/images/posts_images/SHAP_overfit.png)

## References

* Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model
  predictions. Advances in neural information processing systems, 30.
* Lundberg, S. M., Erion, G. G., & Lee, S. I. (2018). Consistent individualized
  feature attribution for tree ensembles. arXiv preprint arXiv:1802.03888.
* Sundararajan, M., & Najmi, A. (2020, November). The many Shapley values for
  model explanation. In International conference on machine learning
  (pp. 9269-9278). PMLR.
* Aas, K., Jullum, M., & Løland, A. (2021). Explaining individual predictions
  when features are dependent: More accurate approximations to Shapley values.
  Artificial Intelligence, 298, 103502.
* Kumar, I. E., Venkatasubramanian, S., Scheidegger, C., & Friedler, S.
  (2020, November). Problems with Shapley-value-based explanations as feature
  importance measures. In International Conference on Machine Learning
  (pp. 5491-5500). PMLR.
* Molnar, Christoph. "Interpretable machine learning. A Guide for
  Making Black Box Models Explainable", 2019.
  https://christophm.github.io/interpretable-ml-book/
