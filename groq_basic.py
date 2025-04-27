import os
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from embeddings import search  # Import the search function from embeddings.py

# Load the environment variables from .env file
load_dotenv()

# Set up the API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

# Initialize the ChatGroq client
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.5,
    max_retries=3
)


# Define intents for chatbot
intents = {
    "greeting": ["hello", "hi", "good morning", "good afternoon", "good evening"],
    "gratitude": ["thank you", "thanks", "much appreciated"],
}


# Detect user intent
def detect_intent(user_input):
    user_input = user_input.lower().strip()
    for intent, phrases in intents.items():
        for phrase in phrases:
            # Match whole words only using regex
            if re.search(rf"\b{re.escape(phrase)}\b", user_input):
                return intent
    return "search"  # Default to "search" if no intent matches


def convert_to_blog_url(file_path):
    # Define the base URL for your blog
    base_url = "https://elampt.github.io/"
    
    # Remove the local directory prefix
    relative_path = file_path.replace("/Users/elam/Work/Projects/Bubble/content/", "")
    
    # Remove the .md extension
    relative_path = relative_path.replace(".md", "")
    
    # Replace spaces with hyphens and encode special characters
    url_path = relative_path.replace(" ", "-")
    
    # Return the full URL
    return base_url + url_path


# Define the chatbot function
def chatbot(user_input, conversation_history):
    # Ensure the system message is included in the conversation history
    system_message = {
        "role": "system",
        "content": "You are a helpful assistant that provides detailed answers questions based on the provided context. "
                   "Do not include any information that is not in the contextk, do not display any specific file or locations. "
                   "If the context is insufficient, respond with 'I don't have enough information to answer that.'"
    }
    if not any(msg["role"] == "system" for msg in conversation_history):
        conversation_history.insert(0, system_message)

    # Detect intent
    intent = detect_intent(user_input)

    if intent == "greeting":
        chatbot_response = "Hello! How can I assist you today?"
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": chatbot_response})
        return chatbot_response, None
    elif intent == "gratitude":
        chatbot_response = "You're welcome! Let me know if there's anything else I can help with."
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": chatbot_response})
        return chatbot_response, None

    # If intent is "search", proceed with the search logic
    try:
        results = search(user_input, top_k=3)  # Retrieve top 3 relevant files and their content
        if results:
            max_context_length = 1000  # Maximum total length for all snippets
            snippet_length = max_context_length // len(results)  # Divide equally among results

            context = "\n\n".join(
                [f"File: {result[0]}\nContent: {result[1][:snippet_length]}..." for result in results]
            )
            citations = "\n".join(
                [f"- {convert_to_blog_url(result[0])} (Score: {result[2]:.4f})" for result in results]
            )
        else:
            context = "No relevant files found."
            citations = "No sources available."

        # Deduplicate citations based on URLs
        citation_list = citations.split("\n")
        unique_urls = {}
        for citation in citation_list:
            # Extract the URL (everything before the space and score)
            url = citation.split(" (Score:")[0].strip("- ").strip()
            if url not in unique_urls:
                unique_urls[url] = citation  # Keep the full citation string

        # Reconstruct deduplicated citations
        citations = "\n".join(unique_urls.values())

        conversation_history.append({"role": "system", "content": f"The following context is provided:\n\n{context}"})
        conversation_history.append({"role": "user", "content": user_input})

        response = llm.invoke(conversation_history)
        chatbot_response = response.text()


        conversation_history.append({"role": "assistant", "content": chatbot_response})
        return chatbot_response, citations
    except Exception as e:
        return f"Sorry, something went wrong: {e}", None


# Run the chatbot loop
if __name__ == "__main__":
    print("Chatbot: Hello! I am your assistant. Type 'exit' to end the chat.")
    
    # Initialize conversation history
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant. Use only the provided context to answer the user's question. "
                   "Do not include any information that is not in the context. If the context is insufficient, "
                   "respond with 'I don't have enough information to answer that.'"}
    ]
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        chatbot_response, citations = chatbot(user_input, conversation_history)
        print(f"Chatbot: {chatbot_response}")
        if citations:
            print(f"\nCitations:\n{citations}")