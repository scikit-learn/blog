---
#### Blog Post Template ####

#### Post Information ####
title: "Blog Post Template"
date: January 4, 2022

#### Post Category and Tags ####
# Format in titlecase without dashes (Ex. "Open Source" instead of "open-source")
categories:
  - Updates
tags:
  - Open Source
  - Machine Learning

#### Featured Image ####
featured-image: jml.png

#### Author Info ####
# Can accomodate multiple authors
# Add SQUARE Author Image to /assets/images/author_images/ folder
postauthors:
  - name: First Author
    website: https://github.com
    email: author@email.com
    image: author.jpeg 
---
<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

Enter blog content here.
