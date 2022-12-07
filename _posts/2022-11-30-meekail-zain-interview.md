---
title: "Interview with Meekail Zain, scikit-learn Team Member"
date: November 30, 2022
categories:
  - Team
tags:
  - Open Source
featured-image: meekail-zain-interview.png

postauthors:
  - name: Reshama Shaikh
    website: https://reshamas.github.io
    image: reshama_shaikh.jpeg 
  - name: Meekail zain
    website: https://www.linkedin.com/in/meekail-zain-02a412a2/
    image: meekail-zain.jpg
---

<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

Posted by [Sangam SwadiK](https://www.linkedin.com/in/sangam-swadi-k/)

Meekail Zain is a computer science PhD student at University of Georgia (USA), a member of Quinn Research Group and a software engineer at Quansight. Meekail officially joined the scikit-learn team as a maintainer in October 2022.

1. __Tell us about yourself.__

    I’m currently attending the University of Georgia, pursuing a PhD in computer science. My area of research predominantly focuses on deep learning, generative modeling, and statistical approaches to clustering. I’m in my third year, and at the time of writing about to begin my comprehensive exams.

    - GitHub: [@Micky774](https://github.com/Micky774)
    - LinkedIn: [@meekail-zain](https://www.linkedin.com/in/meekail-zain-02a412a2/)

1. __How did you first become involved in open source and scikit-learn?__

    I first got involved as a user, as most people do. NumPy was a recurring day-to-day library for me, and scikit-learn was a de-facto necessity for several graduate courses. Originally I never really imagined being able to get to a point where I could affect change in these libraries since they seemed so well-established!

1. __We would love to learn of your open source journey.__

    My journey really kicked off when I went to work at Quansight and received funding through the [NASA Roses grant](https://numfocus.medium.com/numfocus-projects-receive-nasa-grants-deee374e7a57) to be able to dedicate time to contributing to scikit-learn. It was a huge jump from what I had known up until that point. I learned Python very informally in order to be able to use PyTorch to develop/deploy models for my research, and had little-to-no experience with things like continuous integration or strong API. At first I felt incredibly intimidated and unqualified, but at the same time absolutely thrilled that I was in a position to learn so many new things!
    *<span style="background-color: #CAE9F5;">
    I started working on really simple changes to get used to the contribution workflow — things like removing excess whitespace and fixing typos
    </span>*
    — and then graduated to slightly more complex tasks. Eventually I got to the point where I started to “understand” small corners of the codebase and could actually offer help on new issues because of that familiarity. After that,*<span style="background-color: #CAE9F5;"> I started reviewing others’ pull requests (PRs) and offering feedback in an unofficial capacity</span>*, as well as taking on more challenging tasks across the codebase. That process of growth and escalation is still ongoing, and truly I hope it never ends.

1. __To which OSS projects and communities do you contribute?__

    NumPy, scikit-learn, and scipy. Right now it is heavily skewed towards scikit-learn with numpy being second most, but I’m hoping to take some more time to work on scipy in the near future!

1. __What advice or tips you have for people starting out in your field of work?__

    *<span style="background-color: #CAE9F5;">Find a way to enjoy the feeling of being surrounded by things that you haven’t yet mastered</span>*. If you aim for growth — and indeed I think we all should — then you’ll find that you spend the majority of your time surrounded by things that you don’t quite understand, and the natural reaction to that is frustration and intimidation. If you can somehow convince yourself to also be excited by such an environment, you’ll find yourself growing every single day. Nobody starts off knowing everything :)

1. __What do you find alluring about OSS?__

    This is a tough one, there are many amazing points. If I had to select just a few, it would be (in no particular order):
    - The growth potential
    - The community
    - The impact

    I’ve already discussed the growth potential so I’ll leave it at that.

    The **community** is fantastic as well! On every project the community base has its own unique personality of sorts, and they are all wonderful! It’s amazing being able to see recurring users that post interesting issues, or take a stab at opening more complex PRs (pull requests). There’s a strong sense of companionship with the people that are also trying to improve the same project as you! It’s akin to a very niche club in high school. It’s a wonderful experience finding people obsessed with the same cool project as you are.

    Finally, the **impact**. At the end of the day, the work we do has some serious consequences. Each project is essential to so many different workflows and enables brilliant researchers and software engineers to build complex systems and solutions to cutting edge problems. It’s sometimes surreal to think about how essential some of these projects really are.

1. __What pain points do you observe in community-led OSS?__
    
    *<span style="background-color: #CAE9F5;">Consensus is difficult</span>*. This is a double-edged sword, since it carries some benefits too. With community-lead OSS, changes at every scale need to meet _some_ kind of consensus.*<span style="background-color: #CAE9F5;"> This ensures that the changes are well thought out and provides a layer of safety since the chance of uncaught mistakes propagating goes down with the number of people carefully reviewing changes</span>* (for the most part). 

    For example, in scikit-learn a PR with changes to code needs to meet a lazy consensus where two official reviewers (currently just core developers) explicitly approve, and no other official reviewer officially disapproves. Going a bit further up, a new feature request in a project could require the consensus of several core developers that are well-versed in the topic area. Large systemic changes manifest in the form of [SLEPs](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep_template.html) (scikit-learn enhancement proposals) which require a ⅔ consensus across all core developers. Above even that, there are cross-community discussions where the idea of a “consensus” itself isn’t always really clear.

    This system is a critical one, but there are important issues intrinsic to it that need to be addressed. For example, who gets to contribute to a consensus at each scale? What qualifications does one need, and how do we codify that? There’s also the intrinsic tradeoff where the stronger the consensus required, the less likely it is that changes will be adopted. This is by design since wide-reaching changes need to be held to high standards, but it does also mean that occasionally even for narrow-scoped problems no solution will be reached despite options being raised that are better than the status quo.

1. __If we discuss how far OS has evolved in 10 years, what would you like to see happen?__

    I can’t speak to its evolution in the past 10 years, since I am still fairly new to OSS overall, but *<span style="background-color: #CAE9F5;">I would like to see systematic data-driven analysis on contributor’s needs</span>*. Different OSS projects have issued contributor surveys in the past, but in general I think a lot of emphasis is placed on the feedback given from users in meta issues or over community calls. While that is definitely helpful, there’s a lot of extrapolation that takes place when projects try to determine the needs of their contributor base like this.

    Some questions I would love to see studied include:
    - What distribution does the expertise of the contributor base follow?
    - What are the greatest bottlenecks at each level of expertise?
    - Aside from expertise, are there other socio-economic or general demographics that exhibit consistent bottlenecks? (e.g. access to hardware)
    - How do we create informed and effective DEI policies from this information?
    
    *<span style="background-color: #CAE9F5;">
    OSS projects thrive and prosper based on their community, so I would love to see more systematic research on community needs and pain points.</span>*

1. __What are your favorite resources, books, courses, conferences, etc?__

    I absolutely adore [“Probability and Statistics” by Evans and Rosenthal](https://www.utstat.toronto.edu/mikevans/jeffrosenthal/). It does a fantastic job of constructing a lot of otherwise daunting statistical concepts from very elementary ideas. It is my favorite book to recommend to eager students that do not have a rigorous foundation in probability and statistics, since this book does a great job of building up the reader’s intuition and making everything feel natural and derived, rather than arbitrarily defined.

    Regarding conferences, I have to go with [SciPy](https://conference.scipy.org/)! I was definitely scared going into the conference thinking that I would be the least-qualified person in every room and that I’d have nothing to talk about. I realized very quickly that there is _always_ something to talk about, and qualifications don’t matter. It’s a gathering of super passionate people that are each eager to talk about the things that interest them, so regardless of whether you’re an expert or a beginner, they will _happily_ explain things to you. Every single attendee has some area, no matter how specific, that they can talk about for hours. That genuine interest and excitement felt rejuvenating and reminded me why I love OSS so much.

1. __What are your hobbies, outside of work and open source?__

    I really enjoy hiking, camping and playing DnD (Dungeons & Dragons)! Camping especially is an important hobby for me since whenever I have a computer in reach I feel inclined to check my GitHub notifications, so the occasional total disconnect for a weekend is a fantastic tool for me to give myself a break with no pressure of “I _could_ work on that new feature right now…”

    If you have ever had difficulty with relaxing because of that little voice in your head that says “How dare you relax? You could be doing _this_ and _that_ right now!” then I highly recommend going camping, even just for one night! When that voice strikes during camping, I retort “Ah but you see, I don’t have my laptop, so I _can’t_ work on that right now. All I can do right now is relax.” and suddenly the anxiety washes away :)