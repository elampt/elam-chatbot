# Objective
To create a chatbot for https://elampt.github.io/ which answers user questions based on the content on the website and should return citations along with the answers

# Project Breakdown

1. Load the entire .md files from GitHub
 2. Convert the data into Embeddings
 3. Store the Embeddings in a Vector Store
 4. Convert the User Queries into Embeddings and store int the same Vector Store
 5. Build a RAG system (To retrieve similar Embeddings to that of User Query)
 6. Build a ChatBot that integrates the RAG system, user queries and AI model to respond the the user

# Challenges

1. Auto updating of the blog content in the Vector Store instead of manually converting them each time
2. .md file to URL mapping. The file directory of Git contents differ from the URL's of the blog content ✅
3. ChatBot UI design and Integration to the existing GitHub blog page
4. Add Chat History ✅
5. Calling / Searching the vector store for every user query is not scalable. Some user questions may not need the searching of vector store. So, need to find a solution for this ✅


## Research To Be Done
**Focus mainly on Open Source/ Free Platforms**
### Converting Data into Embeddings
Option 1: **Sentence Transformers** (Hugging Face) with **chromadb** embedding function
	all-MiniLM-L6-v2 model
Option 2: **Instructor Embeddings** (Hugging Face)
Option 3: **Gensim** (Word2Vec/Doc2Vec)

### Pick a Vector Store
Option 1 (Simpler choice): ChromaDB 
Option 2: FAISS (Facebook AI Similarity Search)


### Pick a GenAI model for building the ChatBot and implementing the RAG system
* Groq model provider

### Pick a Front-end UI component for the ChatBot
* Gradio
* Streamlit

# Project Build-Up
1. Creation of vector store with embeddings for the data in .md files (Using S**entence Transformers** Library) by breaking each .md files into sections(To improve the granularity and relevance of the search results). Also convert the query into embedding, use cosine similarity or Euclidean distance to retrieve the embedding most similar to the query embedding
2. Use Faiss (Facebook AI Similarity Search) to store the embeddings to make the retrieval more efficient
3. Creation of a basic ChatBot with **ChatGroq** and **Langchain**
4. Inclusion of the embedding retrieval code inside the ChatBot user Query:
	When the user inputs a query in the ChatBot, the query will be converted into an embedding, the embedding most similar to the query embedding will be retrieved from the Faiss index. This will be given as the context to the ChatBot, with the help of this context, the AI ChatBot will answer to the user's query (**RAG** concept is applied here
5. Inclusion of Chat Memory
6. **Intent Detection** logic addition. The previous version of code used to search the vector store for all the user queries for relevant answers. But, sometimes the user query could be simple greeting ("Hi", "Good Morning") or gratitude ("Thank You"), in such cases we need not call the **search** function to search for embeddings in the vector store
7. File directory to Blog URL mapping
8. Create UI with Streamlit and host the ChatBot in Streamlit cloud