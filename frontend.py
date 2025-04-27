import streamlit as st
from groq_basic import chatbot  # Import the chatbot logic
import time
import asyncio

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

# Streamlit app title
st.title("Elam's Blog Chatbot")
st.markdown("### Ask me anything!")

# Display chat messages from history on app rerun, excluding system messages
for message in st.session_state.messages:
    if message["role"] != "system":  # Exclude system messages
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Truncate the conversation history to the last 10 messages
    truncated_history = st.session_state.messages[-10:]

    # Call the chatbot logic and get the response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        citations = None

        # Call the chatbot logic from groq_basic.py with truncated history
        response, citations = chatbot(prompt, truncated_history)

        # Preprocess the response to remove unwanted boilerplate text
        unwanted_phrases = [
            "According to the provided context, ",
            "Based on the context provided, ",
            "With respect to the context, "
        ]
        for phrase in unwanted_phrases:
            response = response.replace(phrase, "")

        # Simulate stream of response with milliseconds delay
        for chunk in response.split():
            time.sleep(0.05)
            full_response += chunk + " "
            message_placeholder.markdown(full_response + "▌")
    
        # Finalize the response
        message_placeholder.markdown(response)


    # Add chatbot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # If citations are available, display them
    if citations:
        st.session_state.messages.append({"role": "assistant", "content": f"Citations:\n{citations}"})
        with st.chat_message("assistant"):
            st.markdown(f"Citations:\n{citations}")