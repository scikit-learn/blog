---
title: "Interview with Virgil Chan, scikit-learn Team Member"
date: November 26, 2025
categories:
  - Team
tags:
  - Open Source
featured-image: 

postauthors:
  - name: Reshama Shaikh
    website: https://reshamas.github.io
    image: reshama_shaikh.jpeg 
  - name: Virgil Chan
    website: https://virchan.github.io
    image: virgil-chan.jpg
---

<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

BIO: Virgil Chan is currently a Forward Deployed Engineer - Pre-Sales at Union.ai. Before that, he worked as a consultant in the San Francisco Bay Area, specialising in predictive data analytics and machine learning. Earlier, he studied mathematics before moving into data science. Virgil joined the scikit-learn team as a Contributor Experience Team member in December 2024.

- GitHub: [@virchan](https://github.com/virchan)
- LinkedIn: [@virgil-chan](https://www.linkedin.com/in/virgil-chan-0a65b11b8)
- Website: [https://virchan.github.io](https://virchan.github.io)

1. __Tell us about yourself.__

    My name is Virgil, and I'm currently working as a Forward Deployed Engineer – Pre-Sales at Union.ai. Based in San Jose, California, I previously worked as a consultant, using libraries from the scientific Python ecosystem on data science and machine-learning projects, including medical data analysis, traffic-network prediction, and model evaluation. Before deciding that computers are more fun, I was doing mathematical research in topology.

1. __How did you first get involved in open source?__

    I first got involved in open source during the COVID-19 lockdown. I used that time to study Python programming, data science, analytics, and machine learning, and that's when I discovered libraries like NumPy, Pandas, scikit-learn, NetworkX, and TensorFlow. Once I became more confident in my skills, I started working as a consultant and used these libraries to deliver data-driven solutions for clients.

1. __We would love to learn of your open source journey.__

    I was transitioning from academia into software development, and I quickly learnt that companies valued hands-on experience more than an advanced degree. At the same time, the rise of GPU-driven workloads and LLM-based solutions made my earlier consulting projects look less impressive on paper. I ended up stuck in the infinite loop of no-job-no-experience.

    Even though I came from a non-traditional background, and my resume didn't match what recruiters and ATS systems usually look for, I've always believed that my experience is something I can build myself. Since companies weren't keen on training junior developers, open source became one of the not-so-many viable paths. I started looking for a project where I could grow, be useful, and apply my academic training in a meaningful way. That search naturally led me to scikit-learn.

1. __How did you get involved in scikit-learn?__

    My first PR to scikit-learn ([scikit-learn/scikit-learn#27913](https://github.com/scikit-learn/scikit-learn/pull/27913)) was a classic "good first issue": adding the URL of a scikit-learn example to the relevant places in the documentation. I opened it in December 2023 and it was merged into the main branch in March 2024. Maren helped me navigate the codebase and understand the CI workflow, which gave me a solid foundation for later contributions. Even though I'm now more experienced with the contributing workflow, I still revisit that PR from time to time to remind myself of the challenges first-time contributors face, and how I can support them.

    My next PR ([scikit-learn/scikit-learn#29709](https://github.com/scikit-learn/scikit-learn/pull/29709)) was more technical, fixing a bug in the (root) mean squared log error function. The expected behaviour was to check that inputs were in the domain of $\log(1 + x)$, but the implementation at the time checked the domain of $\log(x)$ instead. It was one of the few issues I fully understood and knew how to solve, so I volunteered to create a PR. Adrin reviewed it and mentored me throughout the process. Once everything looked good and the CI passed, he asked me to add array API support to the function. And that's where the fun began.

    I had no idea what the array API was, but I already had the habit of reading discussions and merged PRs in my spare time. With a bit of Googling, I quickly understood what needed to be done and the broader importance of the array API project. In fact, completing the array API project has become one of my mid-term goals for my scikit-learn work. Under the guidance of Adrin, Guillaume, Olivier, and Omar, my PRs improved, and contributing became even more rewarding because of how supportive the maintainers were. I also started reviewing PRs, especially from first-time contributors working on the same "good first issue" I began with. In December 2024, I joined the scikit-learn team.

    I'm honoured that the team welcomed me and trusted me with more responsibility, such as representing scikit-learn at the [Scientific Python Developer Summit in May 2025](https://scientific-python.org/summits/developer/2025/), [implementing temperature scaling as a new feature (with Christian)](https://github.com/scikit-learn/scikit-learn/pull/31068), and having the ability to run [CUDA CI](https://betatim.github.io/posts/github-action-with-gpu/) myself. It feels good to pass the same positivity I received back into the community.

1. __To which OSS projects and communities do you contribute?__

    I'm also interested in scaling machine-learning algorithms, so I've been exploring CUDA and cuML as well.

1. __What is alluring about OSS?__

    Open source fosters a collaborative environment where everyone wins: end-users, maintainers, and contributors. Because it is volunteer-driven, it becomes easier to recognise that the problem itself is the problem, the bug or the issue, rather than the people involved. As a result, the usual institutional complications, such as power or ego struggles, conflicts of interest over funding, or pressure from deadlines, are far less likely to drag the project down. People have more freedom to focus on solving problems, which creates an ideal environment for exploration, experimentation, collaboration, learning, and growth.

    Open source has given me the chance to grow, develop new skills, and broaden my perspective, something I've been battling since finishing college. By trading my time for responsibility, I've found open source to be a meaningful and genuinely rewarding experience.

1. __What are your favorite resources, books, courses, conferences, etc?__

    I found the [interview between scikit-learn and Code for Thought](https://www.youtube.com/watch?v=dMbWkAosBVA) on YouTube. The maintainers shared their open-source journeys from how they got started to how they became involved in scikit-learn, which I found inspiring and motivating. For example, I can't agree more with Gael's point that "open source should be spontaneous" and that "a diversity of opinion will make better software." I also learned from Adrin that I could get more involved in the project by becoming the second reviewer for a PR, which gave me the confidence to start reviewing PRs. I think this interview can help people understand the project from a more human and non-technical perspective.

1. __What are your hobbies, outside of work and open source?__

    If I'm done with work and house chores, I usually listen to music. I enjoy classical music (Mozart, Brahms, Rachmaninoff, etc.), and I'm currently getting more exposure to Chopin's work. I also like Rock 'n' Roll (Led Zeppelin, Eric Clapton, Deep Purple, etc.), and I find that AC/DC can "push me to eleven" whenever I'm stuck at work.

    I also enjoy reading novels. At the moment I'm reading The Silmarillion by Tolkien, and my to-read list keeps growing.

    I like hanging out with cats as well. I volunteer with an animal rescue group in San Jose, where I help care for the cats in their sanctuary and assist at adoption fairs.