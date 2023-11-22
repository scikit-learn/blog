---
title: "End-to-end privacy for scikit-learn model training and inference"
date: November 22, 2023

#### Post Category and Tags ####
# Format in titlecase without dashes (Ex. "Open Source" instead of "open-source")
categories:
  - Blogs
tags:
  - Open Source
  - Machine Learning
  - Privacy Preserving Machine Learning
  - Fully Homomorphic Encryption
  - Federated Learning
  - Privacy

#### Featured Image ####
featured-image: privacy-preserving-ml.jpg

#### Author Info ####
# Can accomodate multiple authors
# Add SQUARE Author Image to /assets/images/author_images/ folder
postauthors:
  - name: Andrei Stoian
    website: https://github.com/zama-ai/concrete-ml
    email: andrei.stoian@zama.ai
    image: andrei_stoian.jpeg

---
<div>
  <img src="/assets/images/posts_images/{{ page.featured-image }}" alt="">
  {% include postauthor.html %}
</div>

In the age of cloud computing and wide access to machine learning-based services, privacy is a major challenge. Adding end-to-end privacy to a collaborative machine learning use case sounds like a daunting task. Fortunately, cryptographic breakthroughs like fully homomorphic encryption (FHE) provide a solution. Zama’s [new demo](https://github.com/zama-ai/concrete-ml/tree/main/use_case_examples/federated_learning) shows how to leverage open-source ML tools to add privacy end-to-end using federated learning and FHE. This blog post explains how the demo works under the hood, combining scikit-learn, federated learning and FHE.

FHE is a technology that enables application providers to build cloud-based applications that preserve user privacy and [Concrete ML](https://github.com/zama-ai/concrete-ml) is a machine learning toolkit that converts models to use FHE. Concrete ML leverages the powerful and robust model training algorithms in scikit-learn to train FHE compatible models without requiring any knowledge of cryptography.

Concrete ML uses scikit-learn as a basis for building FHE compatible models due to scikit-learn’s excellent ease of use, extensibility, robustness and wide palette of tools for building, validating and tuning data pipelines. While deep learning is performant on unstructured data, it often requires hyper-parameter tuning to achieve high accuracy. On many use cases, especially on structured data, scikit-learn excels through the robustness of its training algorithms.

## Training a model locally and deploying it securely

When all training data is available to the data scientist, training is secure as no data leaves their machine and only inference needs to be secured when the model is deployed. However, training models for FHE secured inference imposes some constraints on model training. While in the past using FHE required cryptographic expertise, tools like Concrete ML abstract away the cryptography and make FHE accessible to data scientists. Furthermore, FHE adds computation overhead which means that machine learning models may need to be tuned for both accuracy and runtime latency. Concrete ML makes such tuning easy by leveraging parameter search using scikit-learn utility classes such as `GridSearchCV`.

To use Concrete ML to train a model locally the syntax is the same as for scikit-learn. Explanations can also be found in this [video tutorial](https://www.youtube.com/watch?v=p5Y25FWLrH0). For a logistic regression model on MNIST simply run the following snippets:

```
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

mnist_dataset = fetch_openml("mnist_784")

x_train, x_test, y_train, y_test = train_test_split(
    mnist_dataset.data,
    mnist_dataset.target.astype("int"),
    test_size=10000,
)
```

Next, fit the Concrete ML logistic regression model which is a drop-in replacement of scikit-learn’s equivalent. An additional step, compilation, is necessary to produce an FHE computation circuit that performs the inference on encrypted data. Compilation, which is done by [Concrete](https://github.com/zama-ai/concrete), is the process of turning a program into its FHE equivalent, working directly over encrypted data.


```
from concrete.ml.sklearn.linear_model import LogisticRegression

model = LogisticRegression(penalty="l2")
model.fit(X=x_train, y=y_train)
model.compile(x_train)
```

Now test the model’s accuracy when executed on encrypted data. This model obtains around 92% accuracy. Like scikit-learn, Concrete ML supports [many other linear models](https://docs.zama.ai/concrete-ml/built-in-models/linear) such as SVMs, Lasso and ElasticNet and you can use them by simply changing the model class. Furthermore, all hyper-parameters of the equivalent scikit-learn models are supported (like `penalty` in the snippet above)


```
from sklearn.metrics import accuracy_score

y_preds_clear = model.predict(x_test, fhe="execute")

print(f"The test accuracy of the model on encrypted data {accuracy_score(y_test, y_preds_clear):.2f}")
```

## Federated Learning for training data privacy

Oftentimes, in production systems with many users, a machine learning model needs to be trained on an aggregate of all of the users’ data, while preserving the privacy of each user. Common use-cases in this setting are digital health, spam detection, online advertising, or even simpler ones like next word prediction assistance.

Concrete ML can import models trained with federated learning (FL) by tools like [Flower](https://flower.dev/). To train the same model as above using FL, a client application and a server application must be defined. First, the clients are identified by a `partition_id` which is a number between 0 and the number of clients. To split the MNIST dataset and get the current client’s slice use Flower `federated_utils` package:

```
(X_train, y_train) = federated_utils.partition(X_train, y_train, 10)[partition_id]
```

Now define the training client logic:

```
import flwr as fl
from sklearn.linear_model import LogisticRegression

# Create LogisticRegression Model
model = LogisticRegression(
    penalty="l2",
    warm_start=True,  # prevent refreshing weights when fitting
)

federated_utils.set_initial_params(model)

class MnistClient(fl.client.NumPyClient):
        def get_parameters(self, config):  # type: ignore
            return federated_utils.get_model_parameters(model)

        def fit(self, parameters, config):  # type: ignore
           federated_utils.set_model_params(model, parameters)
           model.fit(X_train, y_train)
           print(f"Training finished for round {config['server_round']}")
     return federated_utils.get_model_parameters(model), len(X_train), {}

   def evaluate(self, parameters, config):  # type: ignore
       federated_utils.set_model_params(model, parameters)
       loss = log_loss(y_test, model.predict_proba(X_test))
       accuracy = model.score(X_test, y_test)
            return loss, len(X_test), {"accuracy": accuracy}

 # Start Flower client
fl.client.start_numpy_client(
  server_address="0.0.0.0:8080",
  client=MnistClient()
)
```

Finally, a typical Flower server instance must be created:

```
model = LogisticRegression()
federated_utils.set_initial_params(model)
strategy = fl.server.strategy.FedAvg()

fl.server.start_server(
    server_address="0.0.0.0:8080",
    strategy=strategy,
    config=fl.server.ServerConfig(num_rounds=5),
)
```

When training stops, the clients or the server can store the model to a file:

```
   with open("model.pkl", "wb") as file:
        pickle.dump(model, file)
```

Once the model is trained, it can be loaded from the pickled file and converted to a Concrete ML model to enable privacy preserving inference. Indeed, Concrete ML can either train new models, as shown in the previous section, or convert existing ones, like the one created by FL. This conversion step, using the `from_sklearn_model` function, is used below on the model trained with federated learning. This [video](https://www.youtube.com/watch?v=dfXlOhw9-ic) further explains how to use this function.

```
   with path_to_model.open("rb") as file:
        sklearn_model = pickle.load(file)

compile_set = numpy.random.randint(0, 255, (100, 784)).astype(float)

sklearn_model.classes_ = sklearn_model.classes_.astype(int)

from concrete.ml.sklearn.linear_model import LogisticRegression
model = LogisticRegression.from_sklearn_model(sklearn_model, compile_set)
model.compile(compile_set)
```

As for local training, evaluate the model on some test data:

```
from sklearn.metrics import accuracy_score

y_preds_enc = model.predict(x_test, fhe="execute")

print(f"The test accuracy of the model on encrypted data {accuracy_score(y_test, y_preds_enc):.2f}")
```

All in all, with only a few lines of code, using scikit-learn, Flower and Concrete ML, it is possible to train a model and predict on new data, in a completely privacy-preserving way: the dataset pieces are kept private and the predictions are performed over encrypted data. The model trained here achieves 92% accuracy when executed on encrypted data.

## Conclusion

The most important steps of the full end-to-end private training demo based on Flower and Concrete ML were discussed above. You can find [all the sources](https://github.com/zama-ai/concrete-ml/tree/main/use_case_examples/federated_learning) in our open-source repository. Compatibility with scikit-learn enables users of Concrete ML to use familiar programming patterns and facilitates compatibility with scikit-learn compatible toolkits like Flower. With only a few changes to the original scikit-learn pipeline, the examples in this article show how to add end-to-end privacy to training a classifier on MNIST with federated learning and FHE.



