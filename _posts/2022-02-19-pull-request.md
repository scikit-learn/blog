---
title: "Three Components for Reviewing a Pull Request"
date: February 19, 2022
categories:
  - Community
tags:
  - Open Source
postauthors:
  - name: Thomas J. Fan
    website: https://github.com/thomasjpfan
    image: thomas_fan.jpeg
---

<div>
  {% include postauthor.html %}
</div>

A pull request is a method for submitting contributions to a software project. Maintainers or contributors review these pull requests to discuss the proposed changes and help ensure the changes meet the project guidelines and quality standards. In this talk, we will learn about three components for reviewing a pull request:

1. The mechanics of code review on GitHub.
2. The social aspects of code review and how to effectively give feedback.
3. The technical aspects of reviewing a pull request.

The [slides](https://thomasjpfan.github.io/data-umbrella-2021-reviewing-prs/#/) for this presentation are available.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dyxS9KKCNzA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Outline
- [00:00:00](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=0s) Reshama introduces Data Umbrella
- [00:05:20](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=320s) Thomas begins talk 
- [00:06:35](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=395s) Terms: pull request, reviewer, contributor, merged  
- [00:07:12](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=432s) PART 1: Mechanics of Code Review. Why code review?  
- [00:19:10](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1150s) Browsing Code in GitHub  
- [00:21:50](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1310s) shift+click: highlight multiple lines  
- [00:22:18](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1338s) GitHub b: blame, tells last contributor to the code
- [00:23:12](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1392s) Overview of Mechanics
- [00:24:12](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1452s) Q: How does a suggestion get incorporated into the code? how to sync local repo?
- [00:27:02](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1622s) PART 2: Social Aspects of Reviewing a Pull Request
- [00:27:58](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1678s) Tip 1 for giving feedback: Ask, don't tell
- [00:28:46](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1726s) Tip 2 for giving feedback: Offer alternative implementations
- [00:29:56](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1796s) Tip 3 for giving feedback: Explain why code should be changed
- [00:39:56](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2396s) DRY: Don't Repeat Yourself; refactor, having common logic in multiple places, rewrite code so you have same funtionality, but this makes code more maintainable
- [00:31:50](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1910s) Avoid using derogatory terms
- [00:32:32](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1952s) Tip 4: Be humble, assume everyone is intelligent and well-meaning
- [00:33:15](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=1995s) Tip 5: Ask for clarification
- [00:34:11](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2051s) Tip 6: Communicate which ideas you do not feel strongly about
- [00:35:02](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2102s) Tip 7: Try to leave a positive comment
- [00:35:33](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2133s) Tip 8: Thank contributors for their work
- [00:35:56](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2156s) General Social Aspects
- [00:36:37](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2197s) Disagreement
- [00:37:39](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2259s) Talk synchronously (talk, take notes, update PR with notes to document discussion)
- [00:38:45](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2325s) Overview of Social Aspects
- [00:39:05](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2345s) PART 3: Technical Aspects
- [00:39:52](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2392s) Presentation: how your PR is presented? description of PR
- [00:42:00](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2520s) Was unrelated code changed?
- [00:42:55](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2575s) Is the PR easy to review?
- [00:44:45](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2685s) Engineering, Technical Aspects
- [00:44:58](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2698s) Every change should be intentional
- [00:45:10](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2710s) Offer ways to simplify or improve code
- [00:46:20](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2780s) Does the change maintain backwards compatibility
- [00:48:42](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2922s) Performance optimizations, require benchmarks
- [00:49:32](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=2972s) Is there documentation?
- [00:51:05](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=3065s) Code comments
- [00:52:15](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=3135s) Testing! (are there tests, and more)
- [00:54:08](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=3248s) What does it mean when CI tests fail?
- [00:55:42](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=3342s) It's ok to make mistakes
- [00:56:53](https://www.youtube.com/watch?v=dyxS9KKCNzA&t=3413s) Q&A

## About the Speaker
Thomas J. Fan is a maintainer for scikit-learn, an open-source machine learning library for Python. He leads the scikit-learn project by designing the project’s roadmap, giving feedback to contributors, and implementing new features. Fan also is a maintainer for skorch, a scikit-learn compatible library that wraps PyTorch. He has a Masters in Mathematics from NYU and a Masters in Physics from Stony Brook University. During his academic studies, Fan researched quantum computation and condensed matter physics.
