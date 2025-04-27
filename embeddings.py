import os
import pickle
import faiss
import numpy as np
import re
from sentence_transformers import SentenceTransformer

# Dynamically download the model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Check if embeddings and FAISS index already exist
if os.path.exists("embeddings.pkl") and os.path.exists("faiss_index.bin"):
    # Load embeddings, metadata, and FAISS index
    with open("embeddings.pkl", "rb") as f:
        embeddings, metadata = pickle.load(f)
    index = faiss.read_index("faiss_index.bin")
else:
    # Directory containing the .md files
    content_dir = '/Users/elam/Work/Projects/Bubble/content'

    # Step 1: Read and split files into sections
    section_metadata = []  # List to store metadata (file path and content)

    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Split content into sections (e.g., by paragraphs)
                    sections = content.split("\n\n")  # Split by double newlines
                    for section in sections:
                        if section.strip():  # Ignore empty sections
                            section_metadata.append({
                                "file_path": file_path,
                                "content": section.strip()  # Store section content
                            })

    # Step 2: Compute embeddings for all sections
    embeddings = []
    metadata = []
    for idx, section in enumerate(section_metadata):
        embeddings.append(model.encode(section["content"]))  # Use section content for embedding
        metadata.append({
            "file_path": section["file_path"],
            "content": section["content"]  # Store section content in metadata
        })

    # Convert embeddings to a NumPy array
    embeddings = np.array(embeddings).astype('float32')

    # Step 3: Create a FAISS index
    dimension = model.get_sentence_embedding_dimension()  # Use this to get the embedding size
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)  # Add embeddings to the index

    # Save embeddings, metadata, and FAISS index to disk
    with open("embeddings.pkl", "wb") as f:
        pickle.dump((embeddings, metadata), f)
    faiss.write_index(index, "faiss_index.bin")

# Step 4: Search for similar files
def search(query, top_k=5):
    query_embedding = model.encode(query).astype('float32').reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    
    # Convert distances to similarity scores
    similarities = 1 / (1 + distances)
    
    # Retrieve metadata for top results
    results = []
    for i in range(top_k):
        idx = indices[0][i]
        results.append((
            metadata[idx].get("file_path", "Unknown file"),  # Handle missing file_path
            metadata[idx].get("content", "No content available"),  # Handle missing content
            similarities[0][i]  # Use similarity score instead of distance
        ))
    return results

# Example usage
if __name__ == "__main__":
    user_query = input("Enter your query: ")
    results = search(user_query)
    print("\nTop results:")
    for file_path, content, score in results:
        print(f"File: {file_path}, Score: {score:.4f}")
        print(f"Content: {content[:200]}...")  # Print the first 200 characters of the content
