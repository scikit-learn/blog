---
#### Blog Post Template ####

#### Post Information ####
title: "Community Voices: Interview with Thomas J. Fan, scikit-learn core maintainer"
date: November 4, 2026

#### Post Category and Tags ####
# Format in titlecase without dashes (Ex. "Open Source" instead of "open-source")
categories:
  - Team
tags:
  - Open Source
  - Machine Learning
  - Community

#### Featured Image ####
featured-image: community-voices/community-voices-thomasjfan.png

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

scikit-learn is one of the most widely used tools in data science, counting over 200 million downloads every month. It is often referred to as the Swiss Army knife of machine learning thanks to the versatility of its toolbox, including over 200 estimators and essential workflow tools like train_test_split and StandardScaler.

You may know scikit-learn as the Python library, but behind the code there is a global community that develops, maintains, and sustains it for the benefit of all data scientists all over the world.

Community Voices is our interview series where we introduce you to members of this community: the core maintainers, contributors, educators, community-builders, and many others. Each month, I'll sit down with a different person to hear how they got involved in scikit-learn, what they’re working on, what they're excited about, and how newcomers can get involved.

Community Voices continues Reshama Shaikh’s ([`@reshamas`](https://github.com/reshamas)) interviews with scikit-learn contributors, which have been published on the scikit-learn.org blog since 2017. Reshama no longer has the time to continue these interviews and, after syncing with her, I decided to jump in and continue her tradition. Thank you, Reshama, for all your work over the years. I'm honored to pick up where you left off!

## Interview with Thomas J. Fan

This month, I’m delighted to speak with Thomas J. Fan ([`@thomasjpfan`](https://github.com/thomasjpfan)), a scikit-learn core maintainer and Member of Technical Staff at Modal. Thomas has been involved in scikit-learn since 2018. It’s a pleasure to catch up with Thomas and hear about what he’s working on now.

**Cailean:** Hi Thomas! Tell us a bit about yourself and how you first got involved in scikit-learn.

**Thomas:** I work at [`Modal`](https://modal.com/), an AI infrastructure company, and I am based in NYC. I studied physics and mathematics, and I got into software engineering by contributing to open source projects. In 2018, I started contributing to scikit-learn by working on pandas interoperability and the ColumnTransformer, which lets you apply different preprocessing steps to different columns of a DataFrame. Through these contributions, I learned a lot about software engineering from the maintainers and the community. I have been a scikit-learn core contributor since 2019.

GitHub: [`@@thomasjpfan`](https://github.com/@thomasjpfan)
Wesbite: ['thomasjpfan.com'](thomasjpfan.com)
LinkedIn: [`@thomasjpfan`](https://www.linkedin.com/in/thomasjpfan/)

**Cailean:** Tell us about a feature in scikit-learn that you developed and are proud of. What is it and why does it matter for data scientists?

**Thomas:** I am proud of the set_output API, which lets scikit-learn transformers output DataFrames. Before this feature, transformers only output NumPy arrays, so column names were lost after the first preprocessing step. With set_output(transform="pandas"), a single transformer or a whole pipeline can output pandas or polars DataFrames with meaningful column names. Downstream estimators record these names in feature_names_in_, so you can match coefficients or feature importances to their features, and inspection tools, like partial dependence plots, can use the real column names.

**Cailean:** scikit-learn is a toolbox that covers the full spectrum of tools that a data scientist might need in their day to day, including over 200 estimators and tools for data preprocessing, cross validation, evals, and so on. In your opinion, what is the value of scikit-learn’s breadth for data scientists? 

**Thomas:** When you start out with the estimators and tooling in scikit-learn, you can be confident that everything works well together. Every tool shares the same API, so once you learn one, you know them all. For example, you can combine preprocessing and a model in a Pipeline, tune it with GridSearchCV, and evaluate it with cross-validation, without leaking data between folds.

> *That said, I can see a future where scikit-learn defines a very clear developer API surface, so that third-party estimators can be confident that they are compatible with the wider ecosystem.*

**Cailean:** scikit-learn is expanding beyond NumPy to support GPUs via the Array API and DataFrames via Narwhals. Could you briefly explain why this is being done and how the core team is managing the maintenance overhead?

**Thomas:** The Array API specification and Narwhals establish a unified interface for array libraries, like PyTorch and CuPy, and DataFrame libraries, like polars and pandas. By supporting them, the same code can run on different compute backends, like GPUs with PyTorch. This reduces maintenance overhead by avoiding separate code paths for each library, and array-api-compat helps keep our estimator code simple. However, it does add complexity. For example, an estimator that supports both may end up with three implementations of the same behavior: Narwhals-based, Array API, and native Cython.

**Cailean:** With advanced features like Metadata Routing and Array API support, how is the core team keeping pipelines hyper-flexible without sacrificing scikit-learn's famous beginner-friendly API?

**Thomas:** scikit-learn's simple fit, transform, and predict APIs stay the same even as more advanced features are added. Pipelines get their flexibility from composing these simple pieces with tools like Pipeline and ColumnTransformer, rather than from new APIs. Advanced features like Array API support are developed behind a feature flag, so beginners never encounter them unless they opt in with set_config(array_api_dispatch=True). Once Array API support becomes the default, you can get GPU acceleration by passing a PyTorch array into the same beginner-friendly API.

**Cailean:** While LLMs dominate the hype, scikit-learn remains the engine of enterprise data science. What is its role in a world focused on generative AI rather than random forests?

**Thomas:** Generative AI does not replace scikit-learn; it uses it. When coding agents perform data analysis, they write code that builds on the Python data science ecosystem, including scikit-learn. These libraries are the industry standard because they are well-tested and produce trustworthy, consistent results.

> *When a workflow needs a random forest, a coding agent does not need to waste tokens writing a performant random forest from scratch. It can install scikit-learn and use a battle-tested implementation instead.*

**Cailean:** Looking to the future, what's your prognosis for how data scientists’ workflows will change (if at all) in the next year, given the arrival of coding agents and tabular foundation models?

**Thomas:** In the next year, more domain experts will steer coding agents to derive insights from their data, letting them delegate more and ask more questions of their data. Tabular foundation models, like TabICL, also change the workflow: instead of spending hours tuning gradient-boosted trees, you get a strong baseline from a single fit call.

> *With less tuning, data scientists can focus more on framing the problem, engineering features, and evaluating results. However, these models run best on GPUs and their memory and prediction costs grow with the training data, so gradient-boosted trees remain the better choice for many workloads.*

**Cailean:** Given your prognosis, what are you the most excited about for data scientists in the next year? And which open question do you most want to see answered?

**Thomas:** I am most excited about data scientists bringing coding agents into their analysis toolset. When you give a coding agent read-only access to your data sources, it can explore and connect them to uncover insights you might not have found on your own. Coding agents can showcase their findings in polished HTML reports, and because they use the Python data stack, including scikit-learn, they leave behind reproducible code so you can verify every result. The open question I most want answered is how we can reliably evaluate and trust the conclusions coding agents draw from our data.

**Cailean:** If you could make one recommendation to a new contributor seeking to get involved in the scikit-learn community today, what would it be?

**Thomas:** There are many ways to contribute to the scikit-learn ecosystem! With the advent of coding agents, my recommendation is to use scikit-learn in creative and unexpected ways to solve a problem, write about it, and share it with others. This helps grow the community by showing each other what is possible with the tooling we have today. And along the way, if you run into a bug, submitting a bug report is a great way to help the project too.

## Contribute to Community Voices!
Community Voices celebrates all contributors to scikit-learn -- present and past, technical and non-technical. If you'd like to contribute, please go ahead and get in touch by creating an issue in https://github.com/scikit-learn/blog/issues 
