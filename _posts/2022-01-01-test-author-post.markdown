---
title: "Author Template"
date: January 4, 2022
categories:
  - Updates
tags:
  - Open Source

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

<div>
  {% include event-authors.html event=page %}
</div>


<div id="html" markdown="0">
  {% include post-authors.html event=page %}
</div>

Enter blog content here.
<div id="html" markdown="0">
  {% include postauthortemp.html %}
</div>
