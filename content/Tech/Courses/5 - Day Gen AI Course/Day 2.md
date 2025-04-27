# Embeddings and Vector Stores/ Databases

# Podcast

**Embeddings** are basically a cheat sheet for the machines for understanding the meaning of text, images and all kind of data. They store semantic information
- Low dimensional numerical representations of almost anything. They are basically designed to capture the under-lined meaning and relationships of different pieces of data

## Why are Embeddings important ?
- Efficiency, we can represent any kind of data within an embedding
- Capture how similar or different two pieces of data are
- Lower dimension -> Large scale processing

## Applications of Embeddings:
**Retrieval and Recommendations:**
	Google search: First, we pre-compute embeddings for billions of web pages. When we do a google search, the query gets converted into an embedding too. Finally, we find the web pages whose embeddings are the nearest neighbors to the query embedding in the vector space. The closer the embeddings are in the vector space, the more semantically similar they are

**Joint Embeddings :**
	They are all about handling multimodal data. Let's say we want to search a video based on a text description. Joint Embeddings allow us to map both the text and the images into the same embedding space, making it possible to compare between different types of data

## Effectiveness of Embeddings
* **Precision :** Precision is all about how many of the retrieved items are actually relevant
* **Recall :** The proportion of all the relevant items we actually manage to find
* **Normalized Discounted Cumulative Gain (or) NDCG :** Gives higher scores when the most relevant items are at the very top of the results list
*  **Practical considerations for choosing an Embedding model :**
	* Model Size
	* Embedding Dimensionality
	* Latency
	* Cost
## Retrieval Augmented Generation (RAG):
The concept highlights the use of embeddings to find relevant information from a knowledge base and then use that information to boost the prompts that we give to the language model. This helps the language model to provide more accurate and relevant responses

**This involves a Two Step Process**
**Step 1 :** To create an index. This involves breaking down our documents into chunks, generating embeddings for each chunk using a document encoder, storing those embeddings in a vector database
**Stage 2 :** When a user asks a question. We go into the query processing stage, we first take the user's question, turn it into an embedding using a query encoder, then perform a similarity search in the vector database to find the chunks whose embeddings are closest to the query embedding

## Types of Embeddings
**Text Embeddings :** 
Helps us represent words, sentences, paragraphs and even entire documents
1. Tokenization: Breaking down a text string into smaller meaningful units called tokens. Each token in our entire data set gets assigned a unique numerical ID (**One Hot Encoding**)

**Word Embeddings:**
Dense, fixed length vectors that aim to capture the meaning of individual words, like how each words relate to each other semantically 

**Word2Vec technique** : 
	Uses **CBOW** (Predict the target word given surrounding context) or **Skip Gram** (Predict surrounding context words given a single target word.)
	**Limitation :** Captures local relationships between words within a small window of context
**Glove Technique :**
	 Tries to capture more global information about how words co-occur
	 * Builds a co-occurrence matrix which basically counts how often each word appears in the context of every other word in the entire dataset

**Document Embeddings:**
Representing the meaning of larger chunks of text
* **LSA (Latent Semantic Analysis)** uses a matrix of word counts and documents, applies dimensionality reduction
* **LDA (Latent Dirichlet Allocation)**

**Image Embeddings:**
Can get Image embeddings by training **CNN** or **Vision Transformers** on large image datasets

**Multimodal Embeddings**

**Structured Data Embeddings**
* For a table, we can use dimensionality reduction techniques like PCA to create embeddings for each row

**Graph Embeddings**

## Training of Embedding models
* Many modern embedding models use the dual encoder architecture (An encoder for the query and an encoder for the documents/images or the data we're working with)
* They are trained using contrast loss (Pulling similar embeddings closer and vice versa)
* **Pre-Training :** Training the model on a massive dataset to learn the general represent
* **Fine-Tuning :** On a smaller, more task specific dataset for our specific application 

## Vector Search
Searching through our embeddings efficiently at scale
* Finding items based on their meaning
* We first compute embeddings for all our data, store those embeddings in a vector database, then embed the query into the same space and find the data items whose embeddings are closest to the query embeddings
* Can use **Approximate Nearest Neighbor (ANN)** to speed up the search for match
	* Locality Sensitive Hashing: Uses hash functions to map similar items to the same bucket, so we only have to search within those buckets
	* Tree based methods: Recursively partitioning the search space
* **HNSW** technique

**Vector Database :** Traditional databases aren't built for this kind of high dimensional data and similarity based queries. Vector Database are specifically built for this

## Application
1. Information Retrieval
2. Recommendation Systems
3. Semantic Text similarity
4. Classification
5. Clustering
6. RAG