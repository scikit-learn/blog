---
title: "scikit-learn and Hugging Face join forces"
date: October 13, 2022

categories:
  - Updates
  - Community
tags:
  - Open Source

featured-image: HFxsklearn.png

postauthors:
  - name: Lysandre Debut
    email: lysandre@huggingface.co
    website: https://github.com/LysandreJik
    image: "lysandre_debut.jpg"
  - name: François Goupil
    email: francois.goupil@inria.fr
    website: https://github.com/francoisgoupil
    image: "francois_goupil.jpeg"
---
<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>


[Hugging Face](hf.co) is happy to announce that we're partnering with [scikit-learn](https://scikit-learn.org/stable/index.html) to further our support of the machine learning tools and ecosystem.

At Hugging Face, we've been putting a lot of effort into supporting deep learning, but we believe that machine learning as a whole can benefit from the tools we release. With statistical machine learning being essential in this field and scikit-learn dominating statistical ML, we're excited to partner and move forward together.

As of September 2022, the Hugging Face Hub already hosts nearly 4,000 tabular classification and tabular regression model checkpoints, and we strive for this trend to continue.

<div>
  <video   preload="auto" autoplay loop muted="muted" volume="0"> 
  <source src="/assets/videos/HFxsklearn.mp4" type="video/mp4"> 
  </video>
</div>

## Support to the scikit-learn consortium

Starting June 2022, Hugging Face is now an official sponsor of the scikit-learn consortium . Through this support, Hugging Face actively promotes the development and sustainability of sklearn. As a sponsor of the scikit-learn consortium hosted at the Inria foundation, we'll now participate in the scikit-learn consortium technical committee

## Development support 
To help  sustaining the development of the library , we're happy to welcome Adrin Jalali and Benjamin Bossan to the Hugging Face team. Adrin is a core developer of scikit-learn as well as [fairlearn](fairlearn.org), while Benjamin is the author of the [skorch](https://github.com/skorch-dev/skorch) library and is now a contributor to scikit-learn.

Hugging Face is happy to support the development of scikit-learn through code contributions, issues, pull requests, reviews, and discussions.

## Integration to and from the Hugging Face Hub

["Skops"](https://github.com/skops-dev/skops) is the name of the framework being actively developed as the link between the scikit-learn and the Hugging Face ecosystems. With Skops, we hope to facilitate essential workflows:

- The ability to push scikit-learn models on the Hugging Face Hub
- The possibility to try out models directly in the browser
- The automatic creation of model cards, to improve model documentation and understanding
- The ability to collaborate with others on machine learning projects

### Snapshot of your work

Working at the intersection of scikit-learn and the Hub offers challenges linked to the two platforms. One of these challenges is secure persistence: the ability to serialize models in a secure, safe manner.

scikit-learn models (estimators, predictors, ...) are usually saved using pickle, which is notorious for not being a secure format. Sharing scikit-learn models in this format exposes receivers to potentially malicious data which could execute arbitrary code when run.

That's where secure persistence comes in: as the Hugging Face Hub aims to provide a platform for models, the ability to share safe, secure objects is essential. We've been working on adding secure persistence for scikit-learn models in [skops#128](https://github.com/skops-dev/skops/pull/128) and [skops#145](https://github.com/skops-dev/skops/pull/145)([doc preview](https://skops--145.org.readthedocs.build/en/145/persistence.html)). Instead of serializing using pickle, the object's contents are put into a zip file with an accompanying schema JSON file.

Read about the Skops library in the following blog post: [Introducing Skops](https://huggingface.co/blog/skops).

## Improving interoperability

Skops is an example of an integration of scikit-learn within our tools, but it is not the only example! We will strive to integrate with the rest of our ecosystem so that Hugging Face users may benefit from using scikit-learn tools and vice-versa.

An example is the `evaluate` library, dedicated to efficiently evaluating machine learning models and datasets. We aim for this tool to natively support [scikit-learn metrics](https://github.com/huggingface/evaluate/issues/297) in its API.

---

Through these efforts, we hope to kickstart a lasting relationship between the two ecosystems and provide simple, efficient bridges to lower the barrier of entry. We believe that educating and sharing models is the best way to foster inclusive machine learning from which all can benefit. We're excited to partner with scikit-learn for this endeavor.
