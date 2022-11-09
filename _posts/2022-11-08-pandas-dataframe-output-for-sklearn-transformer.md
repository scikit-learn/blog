---
title: "Pandas DataFrame output for Sklearn Transformers"
date: November 8, 2022
categories:
  - Technical
tags:
  - Sklearn-Transformers
featured-image: pandas_output_sklearn_transformers.PNG

postauthors:
  - name: Sangam Swadi K
    website: https://www.linkedin.com/in/sangam-swadi-k/
    image: sangam_swadik.jpg 
---

<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

## Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/5bCg8VfX2x8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Upcoming feature in release 1.2
Starting next release(v1.2) Scikit-learn provides the ability for the outputs of Scikit-learn transformers to be either in Numpy or Pandas format by configuring it explicitly.Previously, mapping a transformed output back into columns would be cumbersome as it might not be a one-to-one mapping because of complex preprocessing (e.g: Polynomial features ).
The next release(v1.2) Pandas output for transformers maps the transformed features into corresponding names/how they were created automatically.This would be useful for more complex preprocessing pipelines.

## Links to Sample notebook and usage:
- [Pandas output for transformers](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py) 
- [Sample notebook](https://github.com/scikit-learn/blog/blob/main/assets/notebooks/sklearn-pandas-df-output.ipynb)