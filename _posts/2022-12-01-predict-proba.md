---
#### Blog Post Template ####

#### Post Information ####
title: "What to expect from `predict_proba`"
date: December 1, 2022

#### Post Category and Tags ####
# Format in titlecase without dashes (Ex. "Open Source" instead of "open-source")
categories:
  - Updates
tags:
  - Machine Learning

#### Featured Image ####
featured-image: uncertainty_ahead.jpeg

#### Author Info ####
# Can accomodate multiple authors
# Add SQUARE Author Image to /assets/images/author_images/ folder
postauthors:
  - name: Alexandre Perez-Lebel
    website: https://perez-lebel.com
    email: alexandre.perez@inria.fr
    image: alexandre_perez.jpeg
---
<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

Enter blog content here.

In classification, many situations call for estimated probabilities beyond class labels. For example in decision making, cost sensitive learning or causal inference.
These probability estimates are typically accessible from the `predict_proba` method of scikit-learn's classifiers.

However, the quality of the estimated probabilities must be validated to provide trustworthiness, ensure fairness and robustness to operating conditions.
To be reliable, the estimated probabilities must be close to the true underlying posterior probabilities of the classes `P(Y=1|X)`.

Similarly to validating a discriminant classifier through accuracy or ROC curves, tools have been developed to evaluate a probabilistic classifier.
Calibration is one of them [1-4]. Calibration is used as a proxy to evaluate the closeness of the estimated probabilities to the true ones. Many recalibration techniques have been developed to improve the estimated probabilities (see [scikit-learn's user guide on calibration](https://scikit-learn.org/stable/modules/calibration.html)).

It is important to highlight that calibration only captures part of the error on the estimated probabilities. The remaining term is the grouping loss [5]. Together, the calibration and grouping losses fully characterize the error on the estimated probabilities.
However, estimating the grouping loss is a harder problem than calibration as its estimation involves directly the true probabilities. Recent work have focused on approximating the grouping loss through local estimations of the true probabilities [6].


When working with scikit-learn's classifiers, users must be equally as cautious on results obtained from `predict_proba` as on results from `predict`. Both output estimated quantities (probabilities and labels respectively) with no guarantees on their quality. In both case, model's quality must be assessed with appropriate metrics: expected calibration error, brier score, accuracy, AUC.


## References

<style>
ol > li::marker {
  content: "[" counter(list-item) "]\2003";
}
</style>

<ol>
  <li>Platt, J. C. (1999). Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods. ADVANCES IN LARGE MARGIN CLASSIFIERS, 61--74.</li>
  <li>Zadrozny, B., & Elkan, C. (2001). Obtaining calibrated probability estimates from decision trees and naive bayesian classifiers. Icml, 1, 609–616.</li>
  <li>Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. International Conference on Machine Learning, 1321–1330.</li>
  <li>Minderer, M., Djolonga, J., Romijnders, R., Hubis, F., Zhai, X., Houlsby, N., Tran, D., & Lucic, M. (2021). Revisiting the calibration of modern neural networks. Advances in Neural Information Processing Systems, 34.</li>
  <li>Kull, M., & Flach, P. (2015). Novel decompositions of proper scoring rules for classification: Score adjustment as precursor to calibration. Joint European Conference on Machine Learning and Knowledge Discovery in Databases, 68–85.</li>
  <li>Perez-Lebel, A., Le Morvan, M., & Varoquaux, G. (2022). Beyond calibration: estimating the grouping loss of modern neural networks. arXiv. <a href="https://doi.org/10.48550/arXiv.2210.16315">https://doi.org/10.48550/arXiv.2210.16315</a></li>
</ol>

