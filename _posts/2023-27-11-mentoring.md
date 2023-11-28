---
title: "My mentored internship at scikit-learn"
date: November 27, 2023

categories:
  - Diversity
tags:
  - Internship
  - Diversity
  - Inclusiveness


postauthors:
  - name: Stefanie Senger
    email: stefanie.senger@posteo.de
    website: https://github.com/StefanieSenger 
    image: "stefanie-senger.jpeg"
    
  - name: François Goupil
    email: francois.goupil@inria.fr
    website: https://github.com/francoisgoupil
    image: "francois_goupil.jpeg"
---
<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

## How it is to be an Intern at scikit-learn

My name is Stefanie Senger, and I recently concluded a five-month mentored internship at scikit-learn, that had been funded by NumFocus as a Small Development Grant with a clear focus on fostering diversity in open-source projects. The idea to couple a grant with mentorship traces back to Maren Westermann's initiative. She envisioned a pathway to integrate more female coders into scikit-learn through internships and support. Scikit-learn would profit from fresh perspectives and some disruption. I was the guinea pig for an initial experiment, as Maren later told me.


## Starting the Internship

As someone transitioning from a non-technical background to coding, working on scikit-learn was a big thing for me. I had participated in and taught at a data science boot camp, searching diligently for a first role in the field. I never doubted I could tackle more difficult tech challenges over time, but I knew there was much to learn. Scikit-learn had a heavy-tech aura to me, and when I discovered the internship ad, I just thought: this. I was genuinely taken aback when accepted for the role, though. There are many more experienced people looking for such an opportunity, after all.

When I got to know better both my mentors, Adrin Jalali and Guillaume Lemaitre, it became quickly clear that only effort was required, and I could ask them any question along the way. I felt very welcome in the community, also by the other people I interacted with on GitHub.


## What I Worked on

I began by working on documentation and examples such as "Multi-class AdaBoosted Decision Trees," to make those more comprehensive and helpful for users. Then some maintenance tasks on the code that were repetitive so I could find out what to do from other contributors' pull requests. Guillaume discovered that one AdaBoost algorithm required deprecation, and it fell on me to execute this. I had never looked at such a huge code base with so many layers of abstraction, and I had to learn quite some more Python to be able to go ahead. I even got the opportunity to present an "Intro to scikit-learn" workshop at EuroSciPy, the European conference on the scientific use of Python in Basel, where I also got to know many other contributors and people from the scikit-learn team at Inria.

Adrin introduced me to the challenging task of implementing a new feature for metadata routing, developed over many years by the scikit-learn community. It allows users to set metadata, such as sample weights, in meta estimators, that can be routed to sub-estimators and other algorithms that are able to consume it. This was partly uncharted territory and meant finding solutions where there was no predefined path and adapting tests to match the expected behavior. In the last two months of my internship, I implemented metadata routing into some meta-estimators, which was tremendously difficult but, once accomplished, has nourished my professional confidence since.


## Mentorship in Action

Let me describe how the mentoring worked because Guillaume's and Adrin's support was invaluable. They would both literally drop their tasks when I had questions and right away hint me in the right direction. I met Adrin twice a week, and we would co-work while I would throw questions at him. Guillaume was available remotely, and I knew he would jump into a video call with me when I needed help. They both gave reviewing my PRs a priority, and I got feedback on my work regularly.

It was essential to have mentors signaling that it's okay to be learning and to propose tasks to me. If I had come into the project individually, I might have hesitated to take on most of the issues I ended up working on, fearing that my skills were insufficient and that I would hinder the progress of the project rather than help it. The mentoring setting gave me a justification to try things that I wasn't sure if I could do.


## Becoming a Community Member

Looking ahead, I will continue contributing to scikit-learn. As I've gotten to know quite a few of the other contributors in person, I now feel part of the community. I know they care about values like openness and diversity, that I share, and while acknowledging the complexity of the code base, I know what I can learn from taking on issues and the sense of accomplishment when merging my solution into the main branch. And I love contributing to something meaningful, which is something I had always sought.
