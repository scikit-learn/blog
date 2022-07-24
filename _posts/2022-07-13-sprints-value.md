---
title: "The Value of Open Source Sprints, the scikit-learn Experience"
date: July 13, 2022
categories:
  - Events
tags:
  - Open Source
  - Sprints
  - Community
featured-image: sprints-value2.png

postauthors:
  - name: Reshama Shaikh
    website: https://reshamas.github.io
    image: reshama_shaikh.jpeg 
---

<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

With contributions from: Gaël Varoquaux, Andreas Mueller, Olivier Grisel, Julien Jerphanion, Guillaume LeMaitre

## Top Line Summary

Sprints are **working sessions to contribute to an open source library**. The goals and achievements differ between Developer and Community sprints.  The long-term impact of open source sprints, particularly community events, is not easily quantifiable or measurable.  Positive outcomes of sprints have slowly been emerging, and for that reason, to realize the value of open source sprints requires playing the “long game”.

## Introduction

The [scikit-learn](https://scikit-learn.org/dev/index.html) project has a long and extraordinary legacy of open source sprints.  Since 2010, when its [first public version](https://en.wikipedia.org/wiki/Scikit-learn) was released, there have been as many as [45 sprints organized](https://blog.scikit-learn.org/sprints/). The number 45 is a lower bound, since there are likely more sprints that have not been listed. 

To date, more than 2400 people have contributed to [scikit-learn](https://github.com/scikit-learn/scikit-learn).  The number of contributors to scikit-learn exceeds those of other related libraries such as numpy, scipy and matplotlib, with the exception of [pandas](https://github.com/pandas-dev/pandas), which has a greater number of contributors (See Appendix A).

The public discourse on open source has expanded to explore topics of sustainability, funding models, and diversity and inclusion, to name a few.  A *reasonable*, yet *difficult to answer* question that has been posed is: 
>*<span style="background-color: #CAE9F5;">
What is the effectiveness of sprint models and what is the long-term engagement as a result of these sprints?
</span>*



Due to technological limitations of GitHub and privacy concerns, we do not hold precise data on how many scikit-learn contributors connected to the project via a sprint. We have no formal data collection process which records statistics on how many sprint participants are recurring or information on their contributions to other open source projects or other long term positive ripple effects.  A scientific look at the correlation between the number of sprints and contributors is beyond the scope of this article.  What we *will examine* in this article are the **objectives, results and aspirations** of running the scikit-learn sprints.

<span style="background-color: #CAE9F5;">The queries from other open-source projects requesting guidance on sprints and diversity and inclusion have been increasing.</span> We share these experiences and lessons learned with the community, potential funders and open source project maintainers, particularly those projects which are nascent in their quest to build community, sustainability and diversity and inclusion.  

## Outline

In this article we examine the following:
- What is a “sprint”?
- What are the differences between “Developer” and “Community” sprints?
- What are the goals of the open source sprints?
- What value do open source sprints bring to the project and community?
- What are the aspirations of the scikit-learn project, in terms of connecting with the community?

## Definition of a scikit-learn Sprint

A scikit-learn sprint has traditionally been an event where contributors come together to work on issues in the scikit-learn repository.  A sprint can be as short as a few hours, or last over several days, even a week or longer.  They may be in-person, online, hybrid or partially asynchronous.  Sprints may be organized by the developers of the library, community groups (such as Meetups), scheduled alongside scientific or Python conferences, or even at home with a few friends.  They can more simply and less dauntingly be described as
<span style="background-color: #CAE9F5;">
working sessions to contribute to the open source library.            
</span>

## Developer vs Community Sprint

We distinguish between a Developer (Dev) and Community sprint because the goals and results differ significantly between the two.  

**Developer (Dev) Sprint**

A Developer, or “Dev”, sprint is one that is typically organized by the maintainers of the library.  A Dev sprint is one where the developers or maintainers of the library gather to work on issues and to discuss the resolution of ongoing complex issues. This also provides the team an opportunity to focus on tasks related to the long-term roadmap of the project.

The first early Dev sprints were organized at Inria. The first [major Dev sprint](https://github.com/scikit-learn/scikit-learn/wiki/Past-sprints#granada-19th-21th-dec-2011) was held in Granada after the NIPS 2011 conference (now renamed NeurIPS). It was the first time that most of the team had met in real life after months or years of online collaboration, and over a dozen developers participated.   Later, Dev sprints were often hosted in the offices of partnering tech companies, typically from 3 to 7 days, once a year, in pre-COVID times.

**Community Sprint**

A Community sprint can be a collaboration by individuals, by affinity communities such as Meetup Groups (Data Umbrella, PyLadies, etc.), by conferences (SciPy, PyCon, PyData Global, JupyterCon, etc.).  A Community sprint is one that is with the general public and it may be beginners, experts, or a combination of both.

For scikit-learn, the early Community sprints were alongside the [SciPy conferences](https://conference.scipy.org) and the practice has continued for over a decade.

At a Developer sprint, a contributor may work on a PR that has been ongoing for three months.  Conversely, Community sprints require curated issues which newcomers can complete in a shorter period of time (such as 1 day, or 1 day with 1-2 months follow-up).

The landscape of Dev and Community sprints with other [scientific python](https://scientific-python.org/calendars/) libraries is unknown.

## Goals of the Sprints

### Goals of Dev Sprints
- To get maintainers in one room to efficiently discuss open issues and pull requests
- To move along contributions in a synchronous fashion
- To foster existing collaborations with external developers synchronously
- To build rapport: Maintainers reside in various continents and the in-person sprints build rapport within the team. Social interactions are critical in having a productive team. 
- To foster collaborations with the project’s corporate sponsors (members of the [scikit-learn Consortium](https://scikit-learn.org/stable/about.html#funding))

### Goals of Community & Beginner Sprints

- To broaden the project’s contributor base
- To build community and connect the project maintainers with its users
- To obtain interactive feedback from new scikit-learn users and contributors
- To onboard new contributors to scikit-learn and PyData generally
- To onboard new contributors who would become recurring contributors
- To collaborate with community groups to increase diversity of contributor base with intentional outreach
- To strengthen and support existing contributors in order to maintain recurring community contributors

## scikit-learn Team Members Who Connected to the Project Via a Sprint

It is notable that a number of the current maintainers of the library found their way to the project via a sprint.  Additionally, some members of the Contributor Experience Team connected to the scikit-learn project via the sprints.

### Olivier Grisel

[Olivier Grisel](https://github.com/ogrisel) has been a contributor and maintainer for more than 12 years. Olivier met [Gaël Varoquaux](https://github.com/GaelVaroquaux) at a local conference organized in Paris by the French speaking Python users group [AFPy.org](https://www.afpy.org).  After chatting 5 minutes about toy ML experiments in Python, Gaël invited Olivier to join the [first sprint organized at Inria](https://web.archive.org/web/20101118052247/http://fseoane.net/blog/2010/scikitslearn-coding-spring-in-paris/) in March 2010:

Olivier shares:
>At the time, scikit-learn coding sprints gathered only 6 people sitting around a table with some wifi and a coffee machine :)

<figure>
 <img src="/assets/images/posts_images/2010sprint.jpg" alt="5 men sitting around a table coding on their computers" max-width="20%" max-height="20%" /> 
 <figcaption>
 First scikit-learn sprint, Paris, March 2010; Photo credit: <a href="https://fa.bianp.net/pages/about.html">Fabian Pedregosa</a>; (from left to right): Fabian Pedregosa, Gael Varoquaux, Olivier Grisel, Alexandre Gramfort
 </figcaption>
</figure>

### Andreas Mueller
[Andreas Mueller](https://github.com/amueller) has been a maintainer of the project since 2011. He joined a sprint at a conference because he was a user and wanted to contribute.  He [shares in a 2017 interview](https://mlconf.com/blog/interview-andreas-muller-lecturer-columbia-university-core-contributor-scikit-learn-reshama-shaikh/):  
>While working on my Ph.D. in computer vision and learning, the scikit-learn library became an essential part of my toolkit.  My initial participation in open source began in 2011 at the NeurIPS conference in Granada, Spain, where I had attended a [scikit-learn sprint](https://github.com/scikit-learn/scikit-learn/wiki/Past-sprints#granada-19th-21th-dec-2011). The scikit-learn release manager at the time had to leave, and the project leads asked me to become release manager; that’s how it all got started.

<figure>
 <img src="/assets/images/posts_images/sprint-neurips-2011.jpeg" alt="men at a happy hour" max-width="20%" max-height="20%" /> 
 <figcaption>
 NeurIPS Granada, Spain scikit-learn sprint, March 2011; Photo credit: <a href="http://gael-varoquaux.info">Gael Varoquaux</a>; (from left to right): Vlad Niculae, Mathieu Blondel, Bertrand Thirion, James Bergtra, Jake VanderPlas, Andreas Mueller, Alexandre Gramfort
 </figcaption>
</figure>


### Julien Jerphanion
[Julien Jerphanion](https://github.com/jjerphan) participated in a [sprint in February 2019 at AXA](https://scikit-learn.fondation-inria.fr/scikit-learn-sprint-in-paris/) as a first time contributor while interning at Dataiku. The sprint provided Julien an opportunity to experience scikit-learn and meet the maintainers.  Prior to the sprint, he had only used the library in a few projects. He contributed code, reviews, and documentation since March 2021, joined Inria in April 2021 and in October 2021, Julien became a core developer.

### Vlad Niculae
Vlad Niculae's path to a maintainer was via first a scikit-learn mailing list post, then GSoC (Google Summer of Code) internship, and then the [EuroSciPy 2011](https://fa.bianp.net/blog/2011/scikit-learn-euroscipy-2011-coding-sprint-day-one/) sprint.

>The team encouraged me to attend and helped me arrange it. The sprint was instrumental in broadening my focus from the small module I was contributing to the entire library. Co-locating the sprint and the conference this way was great -- it gave me a chance to meet not just the scikit-learn team (small at the time, and incredibly welcoming to me!) but also the broader SciPy ecosystem, including NumPy, IPython [Jupyter Notebook] devs. It helped me understand the scientific Python world a lot better.

### Other Maintainers
There are [other maintainers](https://scikit-learn.org/dev/about.html#people) and emeritus contributors who had participated in a Developer or Community sprint along their journey with the scikit-learn team, such as emeriti Gilles Loupe and Thouis (Ray) Jones.

### Reshama Shaikh
[Reshama Shaikh](https://github.com/reshamas) has organized nine scikit-learn [community sprints](https://www.dataumbrella.org/sprints) from 2017 to 2021. She first contributed code and documentation fixes to scikit-learn in September 2018. In September 2020, she was invited to join the scikit-learn team. 

In her PyConDE  PyData Berlin keynote from April 2022, [5 Years, 10 Sprints, a scikit-learn Open Source Journey](https://blog.dataumbrella.org/pyconde-keynote-reshama), she shares a history and progression of the Community sprints. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZUqJaCWPvmk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Juan Martín Loyola
[Juan Martín Loyola](https://github.com/jmloyola) started [contributing to scikit-learn](https://blog.scikit-learn.org/team/jml-interview/) as preparation for the [Data Umbrella Latin America, June 2021](https://blog.dataumbrella.org/data-umbrella-afme2-2021-scikit-learn-sprint-report ) sprint.  He continued to contribute prolifically after the sprint, and he was invited to join the team in December 2021.  Given his location in Argentina, he will be providing support at the [2022 SciPy Latin America](https://www.scipy.lat/es/scipycon.html) sprint.  

### Second Degree Impact
[Lauren Burke](https://github.com/laurburke) joined the scikit-learn Communications Team in November 2021 at the recommendation of Reshama Shaikh, and this can be considered a network effect. This demonstrates that sprints can result in valuable contributions other than code.


## Sprints: Observed Impact and Lessons Learned 
 
There are a number of observed favorable outcomes from the sprints for both the project and contributors.
 
**Onboarding**

The sprints help the community discover the open source process and get started with contributing.

**Building community**

Sprint participants, whether one-time or recurring, become ambassadors for the project.

**Open source workflow knowledge**

Users learn a range of tools such as: virtual environment setup, version control systems (i.e. Git), testing (flake8, pytest, continuous integration) and unit tests.  They also learn software development best practices.  For many users of scikit-learn, the sprint is the first time they navigate through the codebase and structure of scikit-learn, dig into functions and learn about errors.  They develop experience in collaborative open source workflow.  For employers, letting their team contribute to open-source might be a plus as they learn how to collaborate properly and learn about the internals of the library.  The sprint experience assists contributors in developing a [wider set of technical skills](https://academiccommons.columbia.edu/doi/10.7916/D89G70BS) that can be shared across projects, networking, on to jobs and more.


**Overcoming barriers to entry**

The sprints, as a “hands-on working session”, provide an avenue for potential contributors to overcome common barriers to entry, particularly “getting started”, and moving from the *possibility* to an *actuality* stage.

**Providing an avenue for advanced contributions**

As sprints provide an on-ramp for new contributors, it similarly provides an opportunity for returning contributors to advance their contributing skills to the next level in a structured environment and with mentorship.  

**Building confidence**

The sprints help to build <span style="background-color: #CAE9F5;">confidence</span> for both new and returning contributors.

Gaël shares:
>I believe those sprints helped resourceful people (like Juan Martín) to gain confidence and provide valuable contributions (especially reviews).
 
**Increase open-source literacy**

The sprints are a forum for users to gain a greater understanding of how an open source project functions and for the user/contributor to learn of an actual contribution, from start to finish.
 
**Value of synchronous interaction**

Typically, open source contributions to scikit-learn occur on the GitHub repository in asynchronous fashion, over several weeks or months. The sprints provide real-time synchronous interaction.  This experience provides more direct access to technical assistance and feedback to the contributor, which is more efficient and engagin.  
 
Julien shares:
>I think having a setup like this [beginner/community sprint] is valuable for first time contributors because they can synchronously get specific information they would hardly have got otherwise. To me, this allow giving feedback which is immediate, specific and exact, making contributing to open-source enjoyable and preventing frustration: giving such feedback is what we should aim for and in this regard this setup is convenient.

### Online Sprints

Since the start of the pandemic, Data Umbrella has organized [4 online sprints](https://blog.dataumbrella.org/tags/#sprint-report).  Additionally, there were 2 online sprints with [SciPy](https://www.scipy2020.scipy.org/sprints-schedule) and [EuroPython](https://wiki.python.org/moin/EuroPython2020/Sprints).   

These have been the observed benefits of the online sprints, which began in 2020 due to the global pandemic:  

**Networking**

Online sprints make it easier to meet new people with different backgrounds.

**International collaboration**

Collaborating with affinity communities can attract more candidates from various backgrounds. In particular, online sprints help break geographical barriers.

**Pair programming**

The pairing of contributors seems to work well. Pair programming was consistently ranked as a positive experience by online sprint participants.

**Increases accessibility**

The use of online tools makes it possible to interact with people
who would not have joined community events traditionally organized in
North America or western Europe e.g. because of the travel costs and
complexity of obtaining a visa in time.  Attending the online events is probably also less disruptive for people with young children.

For the scikit-learn project itself, it made it possible to "recruit" a couple of new recurring  contributors who attend regular office hours after the original sprints.

**Office Hours**

The scikit-learn project has regular office hours which are hosted on Discord.  

Olivier shares:
>Actually the fact that we now have community office hours on Discord is probably a consequence of us attending the Data Umbrella online sprints.

>I think they [the sprints] were the most interesting online events I attended during
the COVID-19 crisis when all traditional on-site tech events were canceled. In particular the active planning by the Data Umbrella team for participants to work in pairs with audio rooms on Discord + a central help desk audio room worked really well.

>The pre-sprint and post-sprint office hours also made it possible to limit the time spent on helping fix setup issues compared to what we experience in traditional sprints. They also forced us as maintainers to review and fix our documentation before the event.

**Creation of supplementary resources in different media types**

Data Umbrella coordinated the creation of a series of videos and transcripts that provided learning materials for the community to prepare for the sprint.  These resources are available to the public and have a wide reach:

This is the [Contributing to scikit-learn](https://www.youtube.com/playlist?list=PLBKcU7Ik-ir-b1fwjNabO3b8ebs9ez5ga
) list of videos that were created for the sprints:  
- Andreas Mueller: [Crash Course in Contributing to scikit-learn](https://youtu.be/5OL8XoMMOfA) 
- Reshama Shaikh:  [Example of scikit-learn Pull Request](https://youtu.be/PU1WyDPGePI) 
- Andreas Mueller: [Sprint FAQs](https://youtu.be/p_2Uw2BxdhA)
- Thomas Fan: [3 Components for Reviewing a Pull Request](https://youtu.be/dyxS9KKCNzA)
- Melissa Weber Mendonca: [Sphinx for Python Documentation](https://youtu.be/tXWscUSYdBs)

<figure>
<a href="https://www.youtube.com/playlist?list=PLBKcU7Ik-ir-b1fwjNabO3b8ebs9ez5ga"></a>
 <img src="/assets/images/posts_images/sprint-videos.png" alt="list of videos" max-width="30%" max-height="30%" /> 
 <figcaption>
 Photo credit: <a href="https://reshamas.github.io">Reshama Shaikh</a>
 </figcaption>
</figure>


## Aspirations for Future scikit-learn Sprints
 <span style="background-color: #CAE9F5;">
One of the primary goals of the Community sprints was to onboard new contributors who would become recurring contributors.  This goal has generally not been realized.  scikit-learn is a complex and advanced project, and a one-time sprint does not provide sufficient opportunity and support to sprint participants to become recurring contributors.</span> A few sprint participants have progressed to become returning contributors, and it is a very small number relative to the number of sprint participants.

Onboarding a first-time contributor takes time. People who are contributing for the first time need to go through a lot of information simultaneously regarding both technical and organizational aspects of contributions.  People may run into unexpected issues at the start depending on their
setup and experience, might get frustrated and or discouraged and might not
report the problem they are having (thinking it is their fault). Pre-event office hours have been successful at alleviating some of these roadblocks, for those sprint participants who have completed their pre-work.

Here are some adjustments that can be made in the future to reach the goal of recruiting recurring contributors:  
- Provide mentoring
- Improve onboarding process
- Improve issues definitions
- Have sprints alongside tutorials
- Expand types of contributions that new contributors can make
- Have smaller sprint events

**Mentoring**  
Sprints may not be sufficient for onboarding people. Mentoring is needed to take to the next level, and mentoring relationships can be established during sprint events.

**Improve the onboarding process**

While the scikit-learn project has improved significantly in the past few years as a result of feedback and learnings from the sprints, there is still room for improvement.
  
The scikit-learn project is complex, the contributor learning curve is steeper, and it has been getting more difficult to contribute to scikit-learn.

**Improve issues definitions**

There are 1600+ [issues](https://github.com/scikit-learn/scikit-learn/issues) in the GitHub repository.  Issues can be better defined and it would be valuable to break the issues into smaller steps which would be more approachable.

**Sprints alongside tutorials**

Scheduling sprints alongside tutorial sessions would be conducive in allowing users to connect the open source tool use cases with the motivation and product vision of scikit-learn.

**Expand types of contributions**

While the sprints have typically focused on documentation and code contributions, the project needs support in other areas. There is a backlog of [open issues](https://github.com/scikit-learn/scikit-learn/issues) (1600+ !) and [open pull requests](https://github.com/scikit-learn/scikit-learn/pulls) (650+).  The project needs support in triaging issues and reviewing pull requests.  It would be beneficial to have sprint contributors work on increasingly complex issues.

Julien shares from personal experience:
>In particular and in my opinion, reviewing pull requests is as valuable as authoring them. I also find it a preferable way to learn about scikit-learn internals rather than solving issues.

**Have smaller sprints**  

Julien suggests:
>Would sprints with a really small number of people (e.g. 2 mentees per mentor) be
more valuable in the long term? Personally, I would prefer mentoring one or two
people closely instead (ideally in-person) as I think it is more achievable, enjoyable
and fruitful experience (this is something I am trying to do at the moment when I can
get some time but I currently have limited of it).
 
>Finally, I would also really treasure having in-person sprints [in Paris] with external (recurring)
contributors (with a specific expertise) on advanced subjects when it is possible in the future.

## Conclusion

### Connecting and Supporting scikit-learn

To connect with the scikit-learn project, these are the most active social media platforms:  
- Twitter:  [@scikit_learn](https://twitter.com/scikit_learn)
- LinkedIn:  [@scikit-learn](https://www.linkedin.com/company/scikit-learn/)

It is most welcome for users to “star” the code repository on GitHub: [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
 
Our office hours, in addition to public developers and triage meetings are all posted on our [Community Calendar](https://blog.scikit-learn.org/calendar/).  
 
The next Community sprint may be held at [EuroScipy 2022](https://www.euroscipy.org/2022/index.html) in Basel Switzerland in early September.   Information on past and [upcoming sprints](https://blog.scikit-learn.org/sprints/) are shared on our community site. 
 
 
### Contributing to scikit-learn
 
To contribute to scikit-learn, we have resources available here:  
- [English](https://scikit-learn.org/dev/developers/contributing.html)
- [Spanish](https://qu4nt.github.io/sklearn-doc-es/)
 
There are additional resources for contributing:  
- [Contributing Videos](https://www.youtube.com/playlist?list=PLM-1QqX7UksT6tREbR-n9Mhup0OoRBU34)
- [English, Spanish and some Portuguese language transcripts](https://github.com/data-umbrella/data-umbrella-scikit-learn-sprint)



## Appendix A: GitHub Contributors Comparison of Libraries

A comparison of the contributor base to other related libraries in the same space (updated July 2022):
- [pandas](https://github.com/pandas-dev/pandas): ~2600
- [scikit-learn](https://github.com/scikit-learn/scikit-learn): ~2400 contributors
- [numpy](https://github.com/numpy/numpy): ~1300 contributors
- [matplotlib](https://github.com/matplotlib/matplotlib):  ~1150
- [scipy](https://github.com/scipy/scipy): ~1170

## References

- [Behind the Scenes: What It Takes to Run Data Umbrella’s scikit-learn Open Source Sprints](https://eventfund.codeforscience.org/behind-the-scenes-what-it-takes-to-run-data-umbrellas-scikit-learn-open-source-sprints/)
- Data Umbrella [sprint reports](https://blog.dataumbrella.org/tags/#sprint-report)
- Data Umbrella community [sprint blogs](https://blog.dataumbrella.org/tags/#sprint-blog)
- [Interview with Maren Westermann: Extending the Impact of the scikit-learn Sprints to the Community](https://blog.dataumbrella.org/mwestermann-sprints-experience)
- [Interview with scikit-learn Triage Team Member: Juan Martín Loyola](https://blog.dataumbrella.org/jmloyola-opensource-experience)
- Emily Thompson: [Planning a beginner open source sprint day for data scientists
](https://medium.com/@ethompso28/planning-a-beginner-open-source-sprint-day-for-data-scientists-163b6aa7087f)
- Adrin Jalali: [scikit-learn Sprint at Nairobi, Kenya (2019)](https://adrin.info/scikit-learn-sprint-at-nairobi-kenya.html)