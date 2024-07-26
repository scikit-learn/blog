---
title: "Interview with Adam Li, scikit-learn Team Member"
date: July 24, 2024
categories:
  - Team
tags:
  - Open Source
featured-image: adam-li-interview.png

postauthors:
  - name: Reshama Shaikh
    website: https://reshamas.github.io
    image: reshama_shaikh.jpeg 
  - name: Adam Li
    website: https://adam2392.github.io/
    image: adam-li.jpeg
---

<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>


BIO:  Adam is currently a Postdoctoral Research Scientist at Columbia University in the Causal Artificial Intelligence Lab, directed by [Dr. Elias Bareinboim](https://causalai.net/). He is an [NSF-funded Computing Innovation Research Fellow](https://cifellows2021.org/2021-class/). He did his PhD in biomedical engineering, specializing in computational neuroscience and machine learning at Johns Hopkins University working with Dr. Sridevi V. Sarma in the [Neuromedical Control Systems group](https://sarmalab.icm.jhu.edu/). He also jointly obtained a MS in Applied Mathematics and Statistics with a focus in statistical learning theory, optimization and matrix analysis. He was fortunate to be a [NSF-GRFP fellow, Whitaker International Fellow](https://icm.jhu.edu/2017/03/20/adam-li-selected-for-nsf-graduate-research-and-whitaker-international-fellowships/#.YH2ZT6lKj0o), [Chateaubriand Fellow](https://icm.jhu.edu/2017/06/16/adam-li-icm-phd-student-selected-for-chateaubriand-fellowship/#.YH2Zi6lKj0o) and [ARCS Chapter Scholar](https://icm.jhu.edu/2020/07/20/adam-li-icm-phd-student-receives-arcs-scholarship/#.YH2ZbKlKj0o) during his time at JHU. Adam officially joined the scikit-learn team as a maintainer in July 2024.

- GitHub: [@adam2392](https://github.com/adam2392)
- LinkedIn: [@adam2392](https://www.linkedin.com/in/adam2392/)
- Website: [https://adam2392.github.io](https://adam2392.github.io/)

Link to scikit-learn contributions (issues, pull requests): 
- [FEA Add missing-value support for ExtaTreeClassifier and ExtaTreeRegressor](https://github.com/scikit-learn/scikit-learn/pull/27966)
- [DOC Fix tree explanation of tree_.value in example](https://github.com/scikit-learn/scikit-learn/pull/29331)
- [ENH Enable prediction of isolation forest in parallel](https://github.com/scikit-learn/scikit-learn/pull/28622)
- [ENH Adding estimators_samples_ attribute to forest models](https://github.com/scikit-learn/scikit-learn/pull/26736)
- [FEA SLEP006: Metadata routing for SelfTrainingClassifier](https://github.com/scikit-learn/scikit-learn/pull/28494)
- [FEAT SLEP006 permutation_test_score to support metadata routing](https://github.com/scikit-learn/scikit-learn/pull/29266)
- [FEA Categorical split support for DecisionTree*, ExtraTree*, RandomForest* and `ExtraTrees* #29437](https://github.com/scikit-learn/scikit-learn/pull/29437) 
- Issue: [Adding Oblique Trees (Forest-RC) to the Cythonized Tree Module](https://github.com/scikit-learn/scikit-learn/issues/20819)

1. __Tell us about yourself.__

    I currently live in New York City, where I work on theoretical and applied AI research through the lens of causal inference, statistical modeling, dynamical systems and signal processing. My current research is focused on telling a causal story, specifically in the case one has multiple distributions of data from the same causal system. For example, one may have access to brain recordings from monkeys and humans. Given these heterogeneous datasets, I am interested in answering: what causal relationships can we learn. This is known as the causal discovery problem, where given data, one attempts to learn what causes what. Another problem that I work on that is highly relevant to generative AI is the problem of causal representation learning. Here, I develop theory and train deep neural networks to understand causality among latent factors. Specifically, we demonstrate how to leverage multiple datasets and a causal neural network to generate data that is causally realistic. This can enable more robust data generation from general latent variable models.


1. __How did you first become involved in open source and scikit-learn?__

    I first got involved in open source as a user. I was making the switch from Matlab to Python and started using packages like numpy and scipy pretty regularly. In my PhD research, I dealt with a lot of electrophysiological data (i.e. EEG brain recordings).  I was writing hundreds of lines of code to load and preprocess data, and it was always changing based on different constraints.  That was when I discovered [MNE-BIDS](https://github.com/mne-tools/mne-bids), a Python package within the MNE framework for reading and writing brain recording data in a structured format. This changed my life because now my preprocessing and data loading code was a few lines of code that adhered to an open standard tested by thousands of researchers. I realized the value of open source, and began contributing in my spare time.


1. __We would love to learn of your open source journey.__

    I first started contributing to open-source in the [MNE](https://github.com/mne-tools) organization. This package implements data structures for the processing and analysis of neural recording data (e.g. MEG, EEG, iEEG data). I contributed over 70 pull requests in the MNE-BIDS package, and subsequently was invited to be a maintainer for [MNE-BIDS](https://github.com/mne-tools/mne-bids) and [MNE-Python](https://github.com/mne-tools/mne-python). Later one, I participated in a Google Summer of Code to port the connectivity submodule within MNE-Python to a new package, known as [MNE-Connectivity](https://github.com/mne-tools/mne-connectivity). I added new data structures, and algorithms for the sake of improving the feature developments for connectivity algorithms among neural recording data. Later on, I also worked with a team on porting a neural network architecture from Matlab to the MNE framework to automatically classify ICA derived components. This became known as [MNE-ICALabel](https://github.com/mne-tools/mne-icalabel). These experiences gave me the experience necessary to work in a large asynchronous team environment that is common in OSS. It also taught me how to begin contributing to an OSS project. This led me to scikit-learn.

    I first got involved in scikit-learn as a user, who was heavily interested in the decision tree model in scikit-learn (random forest, randomized trees). Here, I was interested in contributing a [new oblique decision tree model](https://github.com/scikit-learn/scikit-learn/issues/20819) that was a generalization of the existing random forest model. However, the code was not easily added to scikit-learn, and currently the decision to include it is inconclusive. Throughout this process, I learned about the challenges and intricacies of maintaining such a large OSS project as scikit-learn. It is not trivial to simply add new features to a large OSS project because code comes with a maintenance cost, and should fit with the current internal design. At this point in time, there were very few maintainers that were able to maintain the tree submodule, and as such new features are included conservatively.

    I was eager to improve the project to enable more exciting features for the community, so I began contributing to scikit-learn starting with smaller issues such as documentation improvements, or minor bug fixes to get acquainted with the codebase. I also refactored various Cython code to begin upgrading the codebase, especially in the tree submodule. Throughout this process, I identified other projects the maintainers team were working on, and also contributed there. For example, I added metadata routing to a variety of different functions and estimators in scikit-learn. I also began reviewing PRs for the tree submodule and metadata routing where I had knowledge. I also added missing-value support for extremely randomized tree models (called ExtraTrees in scikit-learn). This allows users to pass in data that contains missing values (encoded as `np.nan`) to ExtraTrees. Around this time, I was invited to join the maintainer team of scikit-learn. More recently, I have taken on the project to add [categorical data support](https://github.com/scikit-learn/scikit-learn/pull/29437) to the decision tree models, which will make random forests and extremely randomized tree models more performant and capable to handle real world settings where there is commonly categorical data. 


1. __To which OSS projects and communities do you contribute?__

    I currently primarily contribute to scikit-learn, [PyWhy](https://github.com/py-why/dodiscover) (a community for causal inference in Python), and also develop my own OSS project: [treeple](https://github.com/neurodata/treeple). Treeple is an exciting package that implements different decision tree models beyond those offered in scikit-learn with an efficient Cython implementation stemming from the scikit-learn tree internals.


1. __What do you find alluring about OSS?__

    OSS is so exciting because of the impact it has. Everyone from private projects to other OSS projects will use OSS. Any fixes to documentation, performance improvements, or new features will potentially impact the workflows of potentially millions of people. This is what makes contributing to OSS so exciting. Moreover, this impact ensures that best practices are usually carried out in these projects, and it’s a great playground to learn from the best, while giving back to the larger community.


1. __What pain points do you observe in community-led OSS?__
    
    Right now, community lead OSS moves very slowly in most places. This is for a number of very good reasons: i) not releasing buggy features that may impact millions of people, and ii) backwards compatibility. One of the challenges of maintaining a high-quality OSS project is that you would like to satisfy your users, who may all utilize different components of the project from different versions. As such, many community led OSS projects take a conservative approach when implementing new features and new ideas. However, there may be many exciting better features that are already known by the community, but still lack an OSS implementation.

    I think this can be partially solved by increased funding for OSS, so OSS maintainers and developers are able to dedicate more time to maintaining and improving the projects. In addition, I think this can be improved if more developers in the community contribute to said OSS projects. I hope that I have convinced you though that contributing to OSS is impactful and highly educational. 


1. __If we discuss how far OS has evolved in 10 years, what would you like to see happen?__

    I think more interoperability and integrated workflows for projects will make projects that utilize OSS more streamlined and efficient. For example, right now there are different array libraries (e.g. numpy, cupy, xarray, pytorch, etc.), which all support some manner of a n-dimensional array, but with a slightly different API. This makes it very painful to transition across different libraries that use different arrays. In addition, there are multiple dataframe libraries, such as pandas and polars, and this problem of API consistency also arises there.

    Some work has been made on the Array-API front to allow different array libraries to serve as backends given a common API. This will enable GPU acceleration for free without a single code change, which is great! This will be exciting because users will eventually only have to write code in a single way, and can then leverage any array/dataframe library that has different advantages and disadvantages based on the user use case. 


1. __What are your hobbies, outside of work and open source?__

    I enjoy running, trying new restaurants and bars, cooking and reading. I’m currently training for a half-marathon, where my goal is to run under 8 minutes per mile. I’m also trying to perfect a salad with an asian-themed dressing. In a past life, I was a bboy (breakdancer) for ten years until I stopped in graduate school because I got busy (and old). 

