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

postauthor:
  name: Test Author
  email: postauthor@gmail.com

post-author:
 - name: Test Author
   website: https://github.io
 - name: Test Author 2
   website: https://github.io

---
{% include postauthor.html %}

Authors:
<div>
  {% include postauthor.html %}
</div>


<div>
  {% include postauthor.html event=page %}
</div>



<div>
  {% include post-authors.html event=page %}
</div>

Enter blog content here.
