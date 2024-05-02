---
#### Blog Post Template ####

#### Post Information ####
title: "Note on Inline Authorship Information in scikit-learn"
date: May 4, 2024

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

Historically, scikit-learn's files have included authorship information similar
to the following format:

```python
# Authors: Author1, Author2, ...
# License: BSD 3 clause
```

However, after a series of discussions which you can see in detail in [this
issue]( https://github.com/scikit-learn/scikit-learn/pull/28799), we could list
the following caveats to the status quo:

- Authorship information was not up-to-date and in most cases, but not always,
  reflect the original authors of the file;
- It was unfair to all other contributors who have been contributing to the
  code-base;
- One can check the real authors and the history of the authors of any part of
  the code-base using `git blame` and other `git` tools.

Therefore we came to the conclusion to standardize all authorship information to
mention "The scikit-learn developers", and have the license notice as:

```python
# Authors: The scikit-learn developers
# License: BSD-3-Clause
```

The change is to happen gradually in the coming months after April 2024.
