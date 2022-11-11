---
title: "Pandas DataFrame Output for sklearn Transformers"
date: November 8, 2022
categories:
  - Technical
tags:
  - performance
featured-image: pandas_output_sklearn_transformers.PNG

postauthors:
  - name: Sangam SwadiK
    website: https://www.linkedin.com/in/sangam-swadi-k/
    image: sangam_swadik.jpg 
---

<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

## Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/5bCg8VfX2x8" title="Pandas DataFrame Output for sklearn Transformers" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Upcoming feature in release 1.2
Starting with the next release of [scikit-learn](https://github.com/scikit-learn/scikit-learn) (v1.2), pandas dataframe output will be available for all sklearn transformers! This will make running pipelines on dataframes much easier and provide better ways to track feature names. Previously, mapping a transformed output back into columns would be cumbersome as it might not be a one-to-one mapping in cases of complex preprocessing (e.g., polynomial features).

The pandas dataframe output feature for transformers solves this by tracking features generated from pipelines automatically. The transformer output format can be configured explictly for either **numpy** or **pandas** output formats as shown in [sklearn.set_config](https://scikit-learn.org/dev/modules/generated/sklearn.set_config.html#sklearn.set_config) and the sample code below.
```python
from sklearn import set_config
set_config(transform_output = "pandas")
```

See the sample notebook, [pandas-dataframe-output-for-sklearn-transformer.ipynb](https://github.com/scikit-learn/blog/blob/main/assets/notebooks/sklearn-pandas-df-output.ipynb) and documentation for a more detailed example and usage.

## Links to documentation and example notebook
- [Pandas output for transformers documentation](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py) 
- [pandas-dataframe-output-for-sklearn-transformer.ipynb](https://github.com/scikit-learn/blog/blob/main/assets/notebooks/sklearn-pandas-df-output.ipynb)


## Reporting bugs
We'd love your feedback on this. In case of any suggestions or bugs, please report them at
[scikit-learn issues](https://github.com/scikit-learn/scikit-learn/issues)

Thanks 🙏🏾 to maintainers: [**Thomas J. Fan**](https://github.com/thomasjpfan), [**Guillaume Lemaitre**](https://github.com/glemaitre) , [**Christian Lorentzen**](https://github.com/lorentzenchr) !!