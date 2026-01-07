---
#### Blog Post Template ####

#### Post Information ####
title: "Enhancing user experience through interactive inspection"
date: January 6, 2026

#### Post Category and Tags ####
# Format in titlecase without dashes (Ex. "Open Source" instead of "open-source")
categories:
  - Updates
tags:
  - Open Source
  - Funding
  - Diversity
  - Machine Learning

#### Featured Image ####
featured-image: jml.png

#### Author Info ####
# Can accomodate multiple authors
# Add SQUARE Author Image to /assets/images/author_images/ folder
postauthors:
  - name: Dea María Léon
    website: https://deamarialeon.com
    email: deamarialeon@gmail.com
---
<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>


User experience (UX) has always been an important focus for `scikit-learn`. 
As we know, UX encompasses many aspects, but here we will focus specifically on 
how easy it is for the user to understand `scikit-learn` models during development, 
especially while using tools like jupyter notebooks. 

Initial work to allow users to inspect their models interactively began in 2019, 
when Thomas J. Fan introduced HTML visualizations for estimators. 
He continued to build on this foundation with additional improvements 
in subsequent contributions.

In the summer of 2023, an issue was opened by Gaël Varoquaux outlining 
several potential enhancements to the HTML displays. These ideas stemmed from 
direct interactions with users, which clearly highlighted the need for 
further work in this area. Unfortunately, due to a lack of resources, 
the issue remained open for approximately a year and a half.

This was until the end of 2023, when Guillaume Lemaitre applied for a NumFOCUS 
grant, that the broader topic of Predictive model evaluation and inspection was 
formalized. Enhancing user experience through interactive inspection is an 
essential part of this effort and falls within the scope of the grant.

The grant was awarded to `scikit-learn`and it is from the Chan Zuckerberg 
Initiative (CZI) through its Essential Open-Source Software for Science 
(EOSS) program. It is funded by Wellcome and administered by NumFOCUS. 
Thanks to this financial support, work is well underway. And several objectives
from the said issue have already been completed. 
[See the grant application here.](https://github.com/scikit-learn/
administrative/blob/master/czi_eoss_proposal/EOSS6-0000000551_202312181059.pdf)

The first part was introduced in`scikit-learn` 1.7 version. A parameters table
was added to the HTML representation of models, displaying parameter names 
and their corresponding values. Non-default parameters—those explicitly set by 
the user—are highlighted. In addition, a copy-to-clipboard button is available 
for each parameter name. The parameters table is collapsed by default and 
can be opened by the user.

This feature was further enhanced in version 1.8, with tooltips providing 
documentation for each parameter, as well as links to the online documentation.

More features are now being implemented. In particular, users will be able to 
visualize feature names and values, display fitted attributes and further improve 
the overall appearance of the interactive displays.

