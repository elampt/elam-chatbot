# **Elam's Blog Chatbot**

This is a chatbot application built using **Streamlit** that provides answers based on the content of Elam's blog. The chatbot uses **FAISS** for efficient similarity search, **Sentence Transformers** for embeddings, and **Groq API** for generating responses.

---

## **Features**
- **Interactive Chatbot**: Users can ask questions, and the chatbot provides detailed answers based on the blog content.
- **Contextual Search**: Uses FAISS and Sentence Transformers to retrieve relevant content from Markdown files.
- **Citations**: Provides links to the original blog content as citations for the answers.
- **Streamlit Interface**: A user-friendly web interface for interacting with the chatbot.

---

## Screenshot
![image](https://github.com/user-attachments/assets/09ffa1be-1774-4a3f-b6c4-aef3bebacdad)

## Project Structure
    .
    ├── content                               
    │   ├── example.md                                          # Example Markdown file for chatbot knowledge base
    │   ├── ...        
    ├── embeddings.py                                           # Embedding generation and FAISS search logic
    ├── frontend.py                                             # Streamlit app (entry point for the chatbot)
    ├── groq_basic.py                                           # Chatbot backend logic using Groq API
    ├── requirements.txt                                        # Python dependencies required for the project
    ├── .streamlit
    │   ├── config.toml                                         # Streamlit configuration to disable file watcher
    ├── README.md                                               # Documentation for the project
    └── .gitignore                                              # This file contains the list of directories/files that need to be ignored


---

## **Setup Instructions**

---

## **Dependencies**

The project requires the following Python libraries:

- `streamlit` - For building the chatbot's web interface.
- `sentence-transformers` - For generating embeddings from the blog content.
- `faiss-cpu` - For efficient similarity search using FAISS.
- `python-dotenv` - For loading environment variables from a `.env` file.
- `langchain-groq` - For interacting with the Groq API to generate chatbot responses.
- `numpy` - For numerical operations and data handling.
- `torch` - For PyTorch-based operations (used by `sentence-transformers`).
- `huggingface-hub` - For downloading pre-trained models from Hugging Face.

---

# **System Architecture**

The chatbot system is designed with modular components to handle data processing, retrieval, response generation, and user interaction. Below is an overview of the architecture:

---

## **1. Data Processing Pipeline**
This component prepares the knowledge base for efficient retrieval and embedding generation:
- **Markdown Parsing**: Parses Markdown files from the `content/` directory.
- **Document Chunking**: Splits large documents into smaller, manageable chunks for embedding.
- **Embedding Generation**: Uses `Sentence Transformers` to generate vector embeddings for each chunk.

---

## **2. Vector Database**
Stores and retrieves embeddings for similarity search:
- **FAISS Integration**: A local vector database for efficient nearest-neighbor search.
- **Serialized Files**:
  - `embeddings.pkl`: Stores the generated embeddings.
  - `faiss_index.bin`: Stores the FAISS index for fast retrieval.

---

## **3. Retrieval-Augmented Generation (RAG) Implementation**
Enhances the chatbot's responses by retrieving relevant context from the knowledge base:
- **Document Retrieval**: Uses FAISS to find the most relevant chunks based on user queries.
- **Context Management**: Combines retrieved chunks into a coherent context for the chatbot.
- **Citation Tracking**: Tracks and deduplicates citations for the retrieved content.

---

## **4. LLM Integration**
Handles the core logic for generating responses:
- **Groq API Integration**: Uses the `ChatGroq` client to interact with the Groq API for response generation.
- **Conversation Management**: Maintains a conversation history to provide context-aware responses.
- **Multiple Provider Support**: Can be extended to support other LLM providers if needed.

---

## **5. UI Layer**
Provides a user-friendly interface for interacting with the chatbot:
- **Streamlit Interface**: A web-based UI for user input and chatbot responses.
- **User Interaction Handling**: Displays chat history, handles user queries, and shows citations.

---

## **Workflow**
1. **User Input**:
   - The user enters a query in the Streamlit interface.
2. **Intent Detection**:
   - The chatbot determines the intent (e.g., greeting, gratitude, or search).
3. **Document Retrieval**:
   - If the intent is "search," the system retrieves relevant content using FAISS.
4. **Response Generation**:
   - The chatbot generates a response using the Groq API, incorporating the retrieved context.
5. **Response Display**:
   - The response and citations are displayed in the Streamlit interface.

---

## **Key Components**
- **Data Processing**: `embeddings.py`
- **Chatbot Logic**: `groq_basic.py`
- **User Interface**: `frontend.py`
- **Knowledge Base**: Markdown files in the `content/` directory
- **Vector Database**: FAISS index (`faiss_index.bin`) and embeddings (`embeddings.pkl`)

---

This architecture ensures modularity, scalability, and efficient handling of user queries.





