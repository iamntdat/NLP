# 🧠 Lab 4: Word Embeddings with Word2Vec & GloVe

## 1. Introduction

This lab explores **word embedding techniques** in Natural Language Processing (NLP), focusing on **GloVe** and **Word2Vec**.  
Word embeddings represent words as dense numerical vectors that capture **semantic meaning** and **relationships** between words.

The notebook demonstrates:
- Loading and using **pre-trained GloVe embeddings**
- Measuring **semantic similarity** between words
- Finding **most similar words**
- Creating **simple document embeddings**
- Visualizing embeddings using **PCA** and **t-SNE**
- Training a **Word2Vec model from scratch**
- Comparing embedding methods and discussing results

---

## 2. Environment Setup

Required libraries:
- `gensim`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `nltk`

```bash
pip install gensim numpy scikit-learn matplotlib tqdm nltk
```

---

## 3. Loading Pre-trained Word Embeddings (GloVe)

We use the **GloVe Wiki Gigaword 50-dimensional model** via `gensim.downloader`.

**Model details:**
- Vocabulary size: **400,000 words**
- Vector dimension: **50**

This model is trained on large-scale corpora and captures rich semantic relationships.

---

## 4. Exploring Word Vectors and Similarity

### 4.1 Word Vector Inspection

Each word is represented as a 50-dimensional vector.  
For example, the vector of the word **"king"** contains numerical values encoding semantic information.

### 4.2 Cosine Similarity

Cosine similarity is used to measure semantic closeness between words.

**Observed results:**
- `king` – `queen`: **high similarity**
- `king` – `man`: **moderate similarity**
- `computer` – `keyboard`: **strong domain-related similarity**

📌 **Observation:**  
Words with similar meanings or usage contexts have higher cosine similarity scores.

---

## 5. Finding Most Similar Words

Using the `most_similar()` method, we retrieve the top related words.

Examples:
- **computer** → computers, software, technology
- **love** → dream, life, dreams
- **city** → town, downtown, cities

This confirms that embeddings effectively capture **semantic neighborhoods**.

---

## 6. Simple Document Embeddings

A simple document embedding is created by:
1. Tokenizing the sentence
2. Converting words to lowercase
3. Averaging the embeddings of known words

Example sentence:
> *"The queen rules the country"*

The resulting document vector:
- Has the same dimension as word vectors (50)
- Represents the **overall semantic meaning** of the sentence

📌 **Limitation:**  
This method ignores word order and syntax but provides a quick semantic summary.

---

## 7. Visualization of Word Embeddings

### 7.1 PCA (Principal Component Analysis)

- Linear dimensionality reduction
- Preserves maximum variance
- Provides a coarse but interpretable 2D projection

**Observation:**  
Related words (e.g., *king, queen, man, woman*) appear closer together.

---

### 7.2 t-SNE (t-distributed Stochastic Neighbor Embedding)

- Nonlinear method
- Better at preserving local clusters
- Ideal for semantic visualization

⚠️ **Error Explanation:**  
The error  
> *"perplexity must be less than n_samples"*  

occurs because:
- The perplexity value is too large for the number of words
- `perplexity < number_of_samples` is required

📌 **Fix:**  
Reduce perplexity (e.g., `perplexity=5`) when visualizing small datasets.

---

## 8. Training a Word2Vec Model from Scratch

A small **Word2Vec model** is trained using a toy dataset.

**Training setup:**
- Vector size: 50
- Window size: 3
- Epochs: 100
- min_count: 1

Despite the small dataset, the model successfully learns:
- king ↔ queen
- apple ↔ orange
- computer ↔ python / java

📌 **Observation:**  
Word2Vec can learn semantic relationships **purely from context**, even with limited data.

---

## 9. Comparison of Methods

| Method      | Description | Strengths | Weaknesses |
|------------|------------|-----------|------------|
| **GloVe** | Global co-occurrence-based embeddings | Pre-trained, fast, strong semantic structure | Static, not context-aware |
| **Word2Vec** | Neural-based skip-gram / CBOW model | Learns domain-specific meanings | Needs large corpora |
| **PCA** | Linear dimensionality reduction | Fast, interpretable | Loses nonlinear structure |
| **t-SNE** | Nonlinear visualization | Reveals clusters well | Sensitive to parameters, non-deterministic |

---

## 10. Discussion

- Both **GloVe** and **Word2Vec** are **static embeddings**: one vector per word.
- They cannot distinguish meanings in different contexts (e.g., *bank*).
- Modern NLP models (BERT, GPT, Transformers) address this limitation with **contextual embeddings**.
- However, classic embeddings remain valuable due to:
  - Simplicity
  - Efficiency
  - Strong performance for similarity and visualization tasks

---

## 11. Conclusion

This lab demonstrates:
- How word embeddings encode semantic meaning
- How similarity and clustering emerge from vector space representations
- The practical differences between pre-trained and custom-trained embeddings

Word embeddings remain a foundational concept in NLP and are essential for understanding more advanced language models.

---

## 12. References

- Pennington et al., *GloVe: Global Vectors for Word Representation*
- Mikolov et al., *Efficient Estimation of Word Representations in Vector Space*
- Gensim Documentation
- scikit-learn Documentation

