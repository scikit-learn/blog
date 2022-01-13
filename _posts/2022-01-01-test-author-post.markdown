---
title: "Author Template"
date: January 4, 2022
categories:
  - Updates
tags:
  - Open Source
image:
  feature: posts_images/AFME2-photo.png
  thumb: posts_images/AFME2-photo.png

postauthors:
  - name: Test Author
    email: postauthor@gmail.com
    website: https://github.io
    image: "reshama_shaikh.jpeg"
  - name: Test Author 2
    email: postauthor2@gmail.com
    website: https://github.io
    image: /assets/images/author_images/reshama_shaikh.jpeg
---


<p> Test 1 </p>

<html>
{% for author in page.postauthors %}
{% assign postauthor = author | default: author %}
  {% assign name = postauthor.name %}
  {% assign email = postauthor.email %}
  {% assign website = postauthor.website %}
  {% assign image = postauthor.image %}

  {% if name %}
    {% capture author_name %}
      <a itemprop="sameAs" content="{{ postauthor.website }}" href="{{ postauthor.website }}" rel="me noopener noreferrer" style="vertical-align:top;"><img src="{{ '{{ postauthor.image }}' | relative_url }}" style="width:1em;margin-right:.5em;" alt="Author Icon" class="orcid-icon">{{ postauthor.name }}</a>
    {% endcapture %}
  {% else %}
    {% assign author_name = postauthor.name %}
  {% endif %}

  {% if email %}
    {% assign email = email | remove: "mailto:" %}
      {% capture email_link %} 
        <a href="mailto:{{ email }}" title='{{ email }}'><span><i class="elastic-fai fas fa-envelope"></i></span></a>
      {% endcapture %}
  {% else %}
    {% assign email_link = '' %}
  {% endif %}

{{ author_name }} {{ email_link }}{% unless forloop.last %}, {% endunless %}
{% endfor %}
</html>

Enter blog content here.

<div>
{% include postauthor.html %}
</div>

