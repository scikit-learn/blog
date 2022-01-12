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

postauthor: Test Author

post-author:
 - name: Test Author
   website: https://github.io
 - name: Test Author 2
   website: https://github.io
   
authors:
  - name: Event Author 1
    email: eventauthor1@gmail.com
  - name: Event Author 2
    email: eventauthor2@gmail.com
---

Authors:
<div id="html" markdown="0">
  {% include post-authors.html event=page %}
</div>

Enter blog content here.

<div>
  {% include event-authors.html event=page %}
</div>
