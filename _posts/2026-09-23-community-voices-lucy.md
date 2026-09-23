---
#### Blog Post Template ####

#### Post Information ####
title: "Community Voices: Interview with Lucy Liu, scikit-learn core maintainer"
date: September 23, 2026

#### Post Category and Tags ####
# Format in titlecase without dashes (Ex. "Open Source" instead of "open-source")
categories:
  - Team
tags:
  - Open Source
  - Machine Learning
  - Community

#### Featured Image  featured-image: jml.png ####

#### Author Info ####
# Can accomodate multiple authors
# Add SQUARE Author Image to /assets/images/author_images/ folder
postauthors:
  - name: Cailean Osborne
    website: https://github.com/ccosborne
    email: cailean@probabl.ai
    image: cailean-osborne.png
---
<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

*This post was originally published on the [Probabl blog](https://blog.probabl.ai/community-voices-lucy-liu).*

scikit-learn is one of the most widely used tools in data science, counting over 200 million downloads every month. You may know it as the Python library, but behind the code there is a global community that develops, maintains, and sustains it for the benefit of all data scientists all over the world.

Community Voices is an interview series where we introduce you to members of this community – maintainers, contributors, educators, community-builders, and many others. Each month we'll sit down with a different person to hear how they got involved in scikit-learn, what they’re working on, what they're excited about, and how newcomers can get involved.

Community Voices continues Reshama Shaikh’s (@reshamas) interviews with scikit-learn contributors, which have been published on the scikit-learn.org blog since 2017. Reshama no longer has the time to continue these interviews and, after syncing with her, we decided to jump in and continue her tradition.Thank you, Reshama, for all your work over the years — we’re honored to pick up where you left off!

## Interview with Lucy Liu

To kick off Community Voices , we're delighted to speak with Lucy Liu (@lucyleeow), a scikit-learn core maintainer and software engineer at Quansight Labs. Lucy has led much of the work bringing array API support to scikit-learn. Longtime readers of the scikit-learn blog will recognize her: Reshama interviewed Lucy back in 2022, and Lucy published an update about array API adoption in scikit-learn in March this year.

So it's a pleasure to catch up with Lucy and hear about what she’s working on now.

**Cailean:** Hi Lucy! Please tell us a bit about yourself.

**Lucy:** I currently live in Australia and am a software engineer at Quansight Labs. I primarily work on scikit-learn but also contribute to or have contributed to Sphinx-Gallery, array-api-strict and napari. My introduction to programming came through R, which I used for bioinformatics research during my master's degree. It became clear to me fairly early on that I was more interested in software and tool development than biomedical science. Luckily I was able to transition to more software focused roles. At Quansight Labs I get to work alongside many other maintainers in the scientific python ecosystem, helping improve the software that researchers and data scientists rely on.

GitHub: @lucyleeow
LinkedIn: @lucy-jp-liu

**Cailean:** How did you first get involved in scikit-learn?

**Lucy:** Unlike many contributors who were users first, I started working on scikit-learn via my role at INRIA, where many scikit-learn core developers used to work. My role involved working on RAMP, a platform for collaborative data science, and contributing to open source. I saw the latter as an amazing opportunity to both contribute to the ecosystem and learn from talented open source maintainers, particularly as I had only authored small solo packages previously.

I started with contributing to Sphinx-Gallery, which was a great introduction as it is a small project. Later, I also began contributing to scikit-learn, where I could combine my interests in statistics and software engineering. I've continued maintaining both projects ever since.

**Cailean:** How would you explain the value of scikit-learn for data scientists to a non-technical reader?

**Lucy:** scikit-learn offers a complete toolkit for the data analysis pipeline, from data preprocessing to model training, model evaluation, and visualization. There are three things, in my view, that make it valuable.

First, the documentation, which provides clear explanations, sound guidance, and useful references.

Second, its judicious balance of choice and flexibility. scikit-learn has been very deliberate about what is included, favoring algorithms that are old enough to be stable and cited often enough to be broadly considered reliable, standard methods. This avoids overwhelming the user with choice, while still providing an ecosystem of extensions (e.g., scikit-learn-extra) for niche and expert needs.

Finally, it is thoroughly tried and tested. The large user base, long history, and dedicated maintainers means that most bugs have been fixed or at the very least documented.

**Cailean:** Tell us about a scikit-learn feature that you’ve developed and that you're proud of. What is it and why does it matter for data scientists?

**Lucy:** This would definitely be adding array API support to scikit-learn metrics and estimators. scikit-learn was originally written for NumPy which is geared towards single-core CPU execution. With array API support however, users can pass arrays from any array library implementing the standard, including PyTorch and CuPy. This makes scikit-learn more flexible, allowing users to benefit from array library features, namely GPU acceleration, with almost no change in their code.

Since this work spans much of the codebase, it has prompted us to look at the code holistically and make improvements beyond array API support. It has led to refactoring, increased consistency and improved testing structure. Although these improvements are not always visible to users (and are rarely glamorous), it’s invaluable for keeping a large, long-live project like scikit-learn healthy over the long term.

**Cailean:** What’s your top priority for the coming year that data scientists should watch out for?

**Lucy:** Continued work on adding array API support, particularly around testing infrastructure and defining consistent and predictable behavior when arrays come from different libraries. For example, for cost efficiency a user may want to train a model on a GPU-backed array but use a CPU-backed array to make predictions. The goal is to make scikit-learn more flexible while ensuring its behavior remains predictable and unsurprising.

**Cailean:** I know an important topic for you is the community and supporting contributors. Could you share what you think it means to have a healthy open source community and how you’re going about that in scikit-learn?

**Lucy:** Every open source community looks different, but in scikit-learn I believe a healthy community is one that supports and mentors new contributors, some of whom eventually become maintainers themselves. This ongoing growth is essential, as maintainers naturally move on over time - whether they finish their PhD, take on new commitments, or their interests shift elsewhere.

Now that LLMs have made opening pull requests (PRs) quite easy, it’s become clear that we need to be more intentional in identifying people who are genuinely interested in contributing to the scikit-learn community. This is something we are still grappling with, similar to many other open source projects.

We have spent more time thinking about what we want the contributor pipeline to look like and have made several changes to support this. This includes updating our contributing documentation to highlight the value of non-code contributions and encourage contributors to work on issues they genuinely care about, instead of “good first issues” which don’t arise often. Contributing to a large project often requires significant effort and waiting for reviews, so we think it's better when contributors are motivated by the problem they are solving. We have also clarified which issues are ready for contributions and added a section to our PR template where new contributors can introduce themselves. This helps us build relationships with human contributors, and minimize time spent on unsupervised LLM-generated contributions. 

**Cailean:** If you could make 1 recommendation to a new contributor seeking to get involved in the scikit-learn community today, what would it be?

**Lucy:** Take some time to review pull requests (PRs)! It is a great way to learn the project's norms, both in terms of the codebase and community interactions. It also helps you appreciate the effort involved in reviewing PRs and understand how you can make the process easier for reviewers as an author.

## Contribute to Community Voices!
Community Voices celebrates all contributors to scikit-learn -- present and past, technical and non-technical. If you'd like to contribute, please go ahead and get in touch by creating an issue in https://github.com/scikit-learn/blog/issues 