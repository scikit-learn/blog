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

In the age of cloud computing and wide access to machine learning-based services, privacy is a major challenge. Adding end-to-end privacy to a collaborative machine learning use case sounds like a daunting task. Fortunately, cryptographic breakthroughs like fully homomorphic encryption (FHE) provide a solution. [A new demo](https://github.com/zama-ai/concrete-ml/tree/main/use_case_examples/federated_learning) shows how to leverage open-source ML tools to add privacy end-to-end using federated learning and FHE. This blog post explains how the demo works under the hood, combining scikit-learn, federated learning and FHE.

FHE is a technology that enables application providers to build cloud-based applications that preserve user privacy. Toolkits like [Concrete ML](https://github.com/zama-ai/concrete-ml) convert models to use FHE. These toolkits leverages modified model training algorithms based on scikit-learn to train FHE compatible models without requiring any knowledge of cryptography.

Concrete ML uses scikit-learn as a basis for building FHE compatible models due to scikit-learn’s excellent ease of use, extensibility, robustness and wide palette of tools for building, validating and tuning data pipelines. While deep learning is performant on unstructured data, it often requires hyper-parameter tuning to achieve high accuracy. On many use cases, especially on structured data, scikit-learn excels through the robustness of its training algorithms.

## Training a model locally and deploying it securely

When all training data is available to the data scientist, training is secure as no data leaves their machine and only inference needs to be secured when the model is deployed. However, training models for FHE secured inference imposes some constraints on model training. While in the past using FHE required cryptographic expertise, tools like Concrete ML abstract away the cryptography and make FHE accessible to data scientists. Furthermore, FHE adds computation overhead which means that machine learning models may need to be tuned for both accuracy and runtime latency. Concrete ML makes such tuning easy by leveraging parameter search using scikit-learn utility classes such as `GridSearchCV`.

To use Concrete ML to train a model locally the syntax is the same as for scikit-learn. Explanations can also be found in this [video tutorial](https://www.youtube.com/watch?v=p5Y25FWLrH0). For a logistic regression model on the Wisconsin Breast Cancer dataset you can follow these snippets. 

First, get the dataset, split and normalize it. 

```python
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = fetch_openml("wdbc")

x_train, x_test, y_train, y_test = train_test_split(
    dataset.data,
    dataset.target.astype("int"),
    test_size=0.2
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
```

Next, fit the Concrete ML logistic regression model which is a drop-in replacement of scikit-learn’s equivalent. An additional step, compilation, is necessary to produce an FHE computation circuit that performs the inference on encrypted data. Compilation, which is done by [Concrete](https://github.com/zama-ai/concrete), is the process of turning a program into its FHE equivalent, working directly over encrypted data.


```python
from concrete.ml.sklearn.linear_model import LogisticRegression

model = LogisticRegression(penalty="l2")
model.fit(X=x_train, y=y_train)
model.compile(x_train)
```

The compile step is where the FHE magic happens! It converts the computation expressed on cleartext floating point values to machine code that computes the same function on encrypted integers.

![](sklearn_blog_compile.png "Compilation to FHE").

Now test the model’s accuracy when executed on encrypted data. This model obtains ~99% accuracy. Like scikit-learn, Concrete ML supports [many other linear models](https://docs.zama.ai/concrete-ml/built-in-models/linear) such as SVMs, Lasso and ElasticNet and you can use them by simply changing the model class. Furthermore, all hyper-parameters of the equivalent scikit-learn models are supported (like `penalty` in the snippet above)


```python
from sklearn.metrics import accuracy_score

y_preds_clear = model.predict(x_test, fhe="execute")

print(f"The test accuracy of the model on encrypted data {accuracy_score(y_test, y_preds_clear):.2f}")
```

## Federated Learning for training data privacy

Oftentimes, in production systems with many users, a machine learning model needs to be trained on an aggregate of all of the users’ data, while preserving the privacy of each user. Common use-cases in this setting are digital health, spam detection, online advertising, or even simpler ones like next word prediction assistance.

Concrete ML can import models trained with federated learning (FL) by tools like [Flower](https://flower.dev/). To train the same model as above using FL, a client application and a server application must be defined. Let's define the training client logic, in this case for a single client. In a typical application multiple clients would have a split training.

```python
import flwr as fl
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
from sklearn.preprocessing import StandardScaler

model = LogisticRegression(
    penalty="l2",
    warm_start=True,  # prevent refreshing weights when fitting
)

dataset = fetch_openml("wdbc")

x_train, x_test, y_train, y_test = train_test_split(
    dataset.data,
    dataset.target.astype("int"),
    test_size=0.2
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model.coef_ = np.zeros((2, 30)) # 2 classes, 30 features
model.intercept_ = np.zeros((2,)) # 2 classes
model.classes_ = [0, 1] # class IDs

class FLClient(fl.client.NumPyClient):
    def get_parameters(self, config):
        return [model.coef_, model.intercept_]

    def fit(self, parameters, config):
        model.coef_, model.intercept_ = parameters
        model.fit(x_train, y_train)
        print(f"Training finished for round {config['server_round']}")
        return [model.coef_, model.intercept_], len(x_train), {}

    def evaluate(self, parameters, config):
        model.coef_, model.intercept_ = parameters
        loss = log_loss(y_test, model.predict_proba(x_test))
        accuracy = model.score(x_test, y_test)
        return loss, len(x_test), {"accuracy": accuracy}

 # Start Flower client
fl.client.start_numpy_client(server_address="0.0.0.0:8080",client=FLClient())
```

Finally, a typical Flower server instance must be created:

```python
import flwr as fl
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.coef_ = np.zeros((2, 30))
model.intercept_ = np.zeros((2,))

strategy = fl.server.strategy.FedAvg( 
    min_available_clients=1,
    min_fit_clients=1,
    on_fit_config_fn=lambda server_round: {"server_round": server_round},
)

fl.server.start_server(
    server_address="0.0.0.0:8080",
    strategy=strategy,
    config=fl.server.ServerConfig(num_rounds=5),
)
```

Putting those two snippets in two different files and running them simultaneously, will train the model using federated learning.

When training stops, the clients or the server can store the model to a file:

```python
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)
```

Once the model is trained, it can be loaded from the pickled file and converted to a Concrete ML model to enable privacy preserving inference. Indeed, Concrete ML can either train new models, as shown in the previous section, or convert existing ones, like the one created by FL. This conversion step, using the `from_sklearn_model` function, is used below on the model trained with federated learning. This [video](https://www.youtube.com/watch?v=dfXlOhw9-ic) further explains how to use this function.

```python
import pickle
import numpy as np

# 100 random vectors of 30 features. The training data is assumed standardized
compile_set = np.random.randn(100, 30).astype(float)

with open("model.pkl", "rb") as file:
    sklearn_model = pickle.load(file)

from concrete.ml.sklearn.linear_model import LogisticRegression
model = FHELogisticRegression.from_sklearn_model(sklearn_model, compile_set)
model.compile(x_train)
```

As for local training, evaluate the model on some test data:

```python
from sklearn.metrics import accuracy_score

y_preds_enc = model.predict(x_test, fhe="execute")

print(f"The test accuracy of the model on encrypted data {accuracy_score(y_test, y_preds_enc):.2f}")
```

All in all, with only a few lines of code, using scikit-learn, Flower and Concrete ML, it is possible to train a model and predict on new data, in a completely privacy-preserving way: the dataset pieces are kept private and the predictions are performed over encrypted data. The model trained here achieves 99% accuracy when executed on the encrypted Wisconsin Breast Cancer data.

## Conclusion

The most important steps of the full end-to-end private training demo based on Flower and Concrete ML were discussed above.  Compatibility with scikit-learn enables users of Concrete ML to use familiar programming patterns and facilitates compatibility with scikit-learn compatible toolkits like Flower. With only a few changes to the original scikit-learn pipeline, the examples in this article show how to add end-to-end privacy to training a classifier with federated learning and FHE.


