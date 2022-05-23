---
title: "Interview with Norbert Preining, scikit-learn Team Member"
date: May 22, 2022
categories:
  - Team
tags:
  - Open Source
featured-image: norbert-interview.png

postauthors:
  - name: Reshama Shaikh
    website: https://reshamas.github.io
    image: reshama_shaikh.jpeg 
  - name: Norbert Preining
    website: https://www.preining.info
    image: norbert.jpeg
---

<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

Norbert Preining joined the scikit-learn Team in June 2021. In this interview, learn more about Norbert's journey, immersion and passion in open source.  His contributions to open source span a lifetime -- see where scikit-learn fits into all this. 

1. __Tell us about yourself.__

    I have lived in a few countries, but for about 13 years I call Japan my home. Within Japan I am not in one of the big cities, but in the countryside. For most of my life I have worked in academics, doing research on mathematical logic. For 7 years now I have been in research and development (R&D) teams of companies here in Japan. First Accelia, then Fujitsu, now Mercari. My main research topics are mathematical logic, in particular proof theory and many-valued logics, computability, and software specification and verification. Within my current work areas I am mostly concerned with machine learning in a variety of facets, but mostly in unsupervised learning and most recently in search.

    - GitHub: [@norbusan](https://github.com/norbusan)
    - Twitter:  [@norbusan](https://twitter.com/norbusan)
    - LinkedIn: [@norbertpreining](https://www.linkedin.com/in/norbertpreining/)
    - Website: [preining.info](https://www.preining.info)


1. __How did you first become involved in open source?__

    I got my first computer when I was writing my master thesis, and back then a friend installed Linux on it for me. Since then I am a near-exclusive Linux user and learned to love the advantages of open source.

1. __We would love to learn of your open source journey.__

    I started contributing to OSS projects first within [TeX Live](https://www.tug.org/texlive/) (the biggest distribution of TeX & friends, available for all major and many minor operating systems) by providing builds for an arcane architecture (alpha-linux). Later on I departed on an adventure to bring TeX Live to Debian. For nearly 20 years I maintained TeX Live and many other packages related (and unrelated) to TeX in Debian (all the versions of TeX Live since 2005 till 2021 have been packaged by me), until this year I passed on the torch to Hilmar Preuße, who has helped me over the last years a lot. During all these years I have also contributed to and headed quite a few other OSS projects.

1. __How did you get involved in scikit-learn?__

    I have been using scikit-learn on and off for my AI/ML projects. During my time at Fujitsu I was the representative of Fujitsu in the scikit-learn Consortium, and started to organize development sprints in Japan, as well as contributing myself code to scikit-learn.

1. __Can you share your experience with open source sprints that you have organized or participated in?  Any lessons learned?__

    I have organized two scikit-learn development sprints in Japan ([Spring 2021](https://www.fujitsu.com/jp/about/research/article/202104-devsprint.html) and [Autumn 2021](https://www.fujitsu.com/jp/about/research/article/202111-devsprint2021a.html)), and participated in similar events a few times. For me the biggest problem is the "advertising part" - where/how to motivate people to participate. Having organized scientific conferences with hundreds to thousands of participants, the actual sprint organization was always rather relaxed a job for me, though. What I liked a lot during development sprints are pair programming options - sitting together with someone else and working on a project together. There is always to learn from someone else, and having access to different perspectives or opinions usually shapes up the coding considerably.

1. __To which OSS projects and communities do you contribute?__

    The biggest contribution was to the TeX Live project, where I am the responsible author for the whole infrastructure, the TeX Live manager, and large parts of the server-sided tooling. Another considerable part is for the Japanese TeX Developer Community, where I have contributed several tools to make life for Japanese users of LaTeX more convenient. Within [FOSSASIA](https://fossasia.org), a global organization dedicated to open source and open hardware with base in Asia, I have worked and led the SUSI.AI project (privacy aware smart assistant and smart speaker based on Raspi). For Debian I have packaged practically everything related to TeX, several other packages, and in the last years I renovated the complete KDE/Plasma stack which was lacking behind. Other contributions of larger parts are to the Shotwell photo editor (the whole comment system), the Linux Onedrive client, and a few more things here and there.

1. __What advice or tips you have for people starting out in your field of work?__

    I am not sure what "my field of work" is, though ;-) If you want to start doing OSS, find a project you are using, and a pain point you want to fix, and start coding. Even without knowing the language in the beginning, one can soon contribute. I never heard of ObjC before, but contributed quite some code to [Shotwell](https://wiki.gnome.org/Apps/Shotwell). I never heard about D before until I started developing features for Onedrive. Just get started and learn on the way.

1. __What do you find alluring about OSS?__

    What I find alluring about OSS is that I can fix things I don't like. I also like the "give and take" attitude: I receive a lot of things for free, excellent programs often surpassing their commercial counterparts by far. But I can also give back to the community: there are many ways to do this, even as a non-programmer, giving back is possible: improvement of documentation, community work, resource management, good bug reports, ...

1. __What pain points do you observe in community-led OSS?__

    Politics has taken a far too great hold in many communities, where protecting stakeholders is more important than protecting the developers. This has the effect that the diversity of opinions is badly strangled in many places. But I guess that is a consequence of the growing importance of OSS, and also reflects the general tendencies in societies.

    Another pain point is the well known discrepancy between "*take* and give" from big companies. Often core components are developed by small groups in their spare time and huge infrastructures rely on that, without sufficiently honoring this fact. 


1. __If we discuss how far OS has evolved in 10 years, what would you like to see happen?__

    I would like to see a more robust development system: things like malware injection into Python library or Javascript library repositories need to be dealt with, otherwise trust in open source as a viable and stable alternative will not grow.
    
    Another wish for the next few years - related to scikit-learn in the sense that it is a Python library - is a better development experience with Python. Tooling is still a pain, version incompatibilities between Python releases (even between point releases), loads of tools that all try to do similar things, to name two main pain points. Juggling every day with 3 versions of Python via pyenv, several venvs for projects, and three different tools to install/maintain is what I would like to see disappear.


1. __What are your favorite resources, books, courses, conferences, etc?__

    I love to learn from books, so I have accumulated a lot of technical books, most of mine are from [Manning Publications](https://www.manning.com) (I am not affiliated with them!). There are two books I come back to again and again: [Structure and Interpretation of Computer Programs](https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs#:~:text=Structure%20and%20Interpretation%20of%20Computer%20Programs%20(SICP)%20is%20a%20computer,Wizard%20Book"%20in%20hacker%20culture.) (Abelson/Sussman) and the [Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) (Thomas/Hunt). I think the two are pearls to be read again and again. On the more practical side, Knuth's [Art of Computer Programming](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming) is a great treasure.
    
    I have tried online video courses, but this is less of a format for me. Q&A sites on the net are of course a great resource, but be aware that simply copy paste will lead in most cases to bad bugs (or even worse, bed bugs). Only if I have understood the code from there, I will reuse it in my own programs.

    Comment from Reshama:  
        >When I was first learning Python, I made the painful and *very time-consuming* mistake of doing that, copying version 2 code into my version 3 script and not understanding why it did not work, initially. Unfortunately, StackOverflow answers do not include versions of libraries. 


1. __What are your hobbies, outside of work and open source?__

    I love to go to the mountains, and that is serious mountaineering. I have worked as a professional mountain guide (UIAGM) for some years, mostly in France and Switzerland, and I also do some professional guiding work here in Japan. Besides that, going out with friends into the mountains (rock climbing, ice climbing, ski touring, traditional mountaineering, and the discipline special to Japan/Taiwan/Korea: shower climbing, ...) gives my head breathing room. Of course, with a small kid at home the mountains have become a bit smaller, and less present, though. So now with my family there is a lot of camping, going to the seaside, skiing in winter, and traveling (hopefully again soon also outside of Japan!).

<figure>
 <img src="/assets/images/posts_images/norbert-japan.png" alt="photo of a man hiking" max-width="50%" max-height="50%" /> 
 <figcaption>
 Photo credit: <a href="https://www.preining.info">Norbert Preining</a>
 </figcaption>
</figure>