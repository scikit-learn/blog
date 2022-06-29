---
title: "Understanding Gradient Boosting as a Gradient Descent"
date: June 6, 2019
categories:
  - Technical
tags:
  - Gradient boosting

featured-image: gbdt.png

postauthors:
  - name: Nicolas Hug
    website: https://github.com/NicolasHug
    image: nicolas_hug.jpg 
usemathjax: true
---
<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

There are a lot of resources online about gradient boosting, but not many of them explain how gradient boosting relates to gradient descent. This post is an attempt to explain gradient boosting as a (kinda weird) gradient descent.

I’ll assume zero previous knowledge of gradient boosting here, but this post requires a minimal working knowledge of gradient descent.

__Let’s get started!__

For a given sample $$ \mathbf{x}_i $$, a gradient boosting regressor yields
predictions with the following form:

$$ \hat{y}_i = \sum_{m = 1}^{\text{n_iter}} h_m(\mathbf{x}_i), $$

where each $$ h_m $$ is an instance of a base estimator (often called weak learner, since it usually does not need to be extremely accurate). Since the base estimator is almost always a decision tree, I’ll abusively use the term GBDT (Gradient Boosting Decision Trees) to refer to gradient boosting in general.

Each of the base estimators $$ h_m $$ isn’t trying to predict the target $$ y_i $$. Instead, the base estimators are trying to predict gradients. This sum $$ \sum_{m = 1}^{\text{n_iter}} h_m(\mathbf{x}_i) $$ is actually performing a gradient descent.

Specifically, it’s a gradient descent in a functional space. This is in contrast to what we’re used to in many other machine learning algorithms (e.g. neural networks or linear regression), where gradient descent is instead performed in the parameter space. Let’s review that briefly.

Read the full blog post on Nicolas' blog:
<span style="background-color: #CAE9F5;">  [Understanding Gradient Boosting as a gradient descent](http://nicolas-hug.com/blog/gradient_boosting_descent) </span>
