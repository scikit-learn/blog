---
#### Blog Post Template ####

#### Add Post Information ####
title: "Blog Post Template"
date: January 4, 2022

#### Add Post Category and Tags ####
# Format in titlecase without dashes (Ex. "Open Source" instead of "open-source")
categories:
  - Updates
tags:
  - Open Source

#### Featured Image ####
featured-image: jml.png

#### Author Info ####
# Add SQUARE Author Image to /assets/images/author_images/ folder
postauthors:
  - name: First Author
    website: https://github.com
    email: author@email.com
    image: author.jpeg 
---
<div>
  <img src="/blog/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

Enter blog content here.
