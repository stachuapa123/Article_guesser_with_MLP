#German Article Predictor

An experimental machine learning project designed to evaluate how well neural networks can predict the definite articles (*der, die, das*) of German nouns. This project leverages **TensorFlow** and pre-trained word embeddings from **FastText**.

## 🎯 Project Goals

* **Evaluate Embedding Semantics:** Investigate whether pre-trained vector embeddings inherently capture information about German grammatical gender. This is an interesting NLP challenge because German articles are notoriously irregular and often decoupled from real-world logic (for example, the word for "girl", *das Mädchen*, is grammatically neutral, not feminine).
* **Test Network Architectures:** Observe and analyze how basic neural network models perform at predicting these articles when utilizing one-hot positional encoding.

## 🛠️ Tech Stack
* **Framework:** TensorFlow
* **NLP Tools:** FastText (Embedding Matrix), Self implemented One-Hot Positional Encoding
