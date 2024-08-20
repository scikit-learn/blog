---
title: "Code, outreach, and beyond: my scikit-learn internship experience"
date: August 15, 2024

categories:
  - Team
tags:
  - Internship
  - Open Source


postauthors:
  - name: Emily Chen
    email: emily@probabl.ai
    website: https://github.com/EmilyXinyi 
    image: "emily_chen.jpeg"
    
  - name: François Goupil
    email: francois.goupil@inria.fr
    website: https://github.com/francoisgoupil
    image: "francois_goupil.jpeg"
---
<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

## Who am I? 

It’s Emily here! I am a Chinese-Canadian from Toronto, Canada, currently studying electrical and computer engineering at the University of Toronto. I recently completed a three-month internship in Paris, funded by [Probabl](https://probabl.ai/), focusing on the technical development of scikit-learn, as well as outreach to expand the scikit-learn community in China and beyond. 


## What I worked on

There are two distinctly different components of my work, namely open source development and community outreach. 

### Open Source Developement

I started my contributions by adapting certain metrics (tweedie, mean absolute percentage error etc.) to be Array API compatible under the guidance of my mentor, Olivier. The Array API standard is a cross-library API for array operations on Python, which is designed to improve interoperability and consistency across different array libraries. This also means that scikit-learn algorithms written in NumPy for CPU can work on other hardwares (GPU) with PyTorch or CuPy, greatly improving performance. As I gained more familiarity with the scikit-learn codebase and Array API, I began working on adapting “larger” functions to be Array API compatible, which means a lot more fundamental, a lot more dependencies, a lot more challenging, and a lot more fun. 

I also happened to be the only one on the team using a Mac with Intel chips, which means I was tasked with reproducing issues detected unique to this setup. Under the guidance of Loïc, I learned a lot about scikit-learn’s lockfiles, the CI pipeline, and identifying and fixing issues when they occur. 

### Chinese Community Outreach

China has the second largest user group of scikit-learn. As a community, we believe that we can be more inclusive to ease Chinese contribution and do what is necessary to recruit more Chinese contributors. Therefore, I need to find out who and where scikit-learn is being used, if there are other platforms (outside of GitHub) that development is happening, because GitHub tends to be very slow in China, and establish scikit-learn’s official presence in the Chinese community. 

It was my first time being in this type of role, so it was lots of exploring, reaching out to representatives of the Chinese chapter at different companies/communities, translation work, and learning how the business side of Chinese social media works. After these three months, a network has been established between scikit-learn and various Chinese entities, including companies with open source projects, open source communities, and data science training and certification programs. I will be representing scikit-learn at [KubeCon + CloudNativeCon + AI_Dev](https://events.linuxfoundation.org/kubecon-cloudnativecon-open-source-summit-ai-dev-china/) in Hong Kong, where I will be meeting with some of the Chinese network in-person, establishing new connections, and looking for more collaboration opportunities. 


## Interacting with my mentors and co-workers 

The support from my mentors was invaluable. My mentor, Olivier, explained ongoing scikit-learn projects to me in extreme detail on my very first day, and walked me through my first PR from beginning to end on my third. Throughout my internship, Olivier was always available online, and provided thorough feedback on all of my PRs. Whenever I found a task that I would like to try but seemed somewhat challenging, Olivier was always supportive and provided me with advice whenever I needed. Because of this, I gained a better understanding of scikit-learn, Array API, and my technical skills have improved too. 

I also had weekly Peer Programming sessions with Loïc and Stefanie, where my piled-up questions from the week outside of Array API would be answered, and I would almost always learn something new about developer tools or programming fundamentals. 

On the Chinese community outreach side, it has always been with the scikit-learn communications team. Here I must give a special shoutout to manager François, who is also part of the communications team, for always being supportive and believing in my outreach efforts, especially because I was nervous doing this kind of task and using Chinese in a professional context for the first time. I also got to interact with [Charlie](https://charlie-xiao.github.io/) (yes, the core-dev Charlie), who is located in China and helped me tremendously with tasks that require physical presence. 


## My vision for scikit-learn in China in the future

I am very optimistic about scikit-learn’s presence in China, and I am very excited to see where it leads to. The scikit-learn communications team and I are in the process of creating official (and verified!) accounts on Chinese social media platforms, which will establish scikit-learn’s online presence. As our network with Chinese entities becomes more mature, scikit-learn and its partners will jointly webinars online and eventually events in-person in China too. .


## Special thanks 

My internship would not have been possible without Probabl, the official operating brand of scikit-learn. Probabl funded my internship, and the Probabl team made me feel so welcomed and comfortable in my position. Everyone is nice, open, and extremely supportive. I could honestly say that this is the best internship experience I have had, and I will be missing this team so much next year as I completed my final year of university. 

### PS: bits and pieces caught on camera 
Vlog: [Internship in 1 minute](https://www.tiktok.com/t/ZGe363yG4/)

<figure>
 <img src="/assets/images/posts_images/paris_office_view.JPG" max-width="20%" max-height="20%" />
 <figcaption>
 The Paris Montparnasse office has the best views
 </figcaption>
</figure>

<figure>
 <img src="/assets/images/posts_images/polaroid.png" max-width="20%" max-height="20%" />
 <figcaption>
 Best office vibes (this is on our HR's desk)
 </figcaption>
</figure>

<figure>
 <img src="/assets/images/posts_images/pytorch_premier.png" max-width="20%" max-height="20%" />
 <figcaption>
 When I went to the PyTorch documentary premiere with my co-worker
 </figcaption>
</figure>

<figure>
 <img src="/assets/images/posts_images/pic_on_probabl_wall.png" max-width="20%" max-height="20%" />
 <figcaption>
 My picture on the Probabl wall 
 </figcaption>
</figure>
