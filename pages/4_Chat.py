import streamlit as st
import openai
import time
from help import *

def streamlit_app():
    st.title("Chat with an AI Assistant")

    # Initialize conversation in session state if not present.
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    # Initialize user input in session state if not present.
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    # User input field
    user_input = st.text_input("Your message to the Assistant:", key="user_input")

    # Send button with a callback function.
    send_button = st.button("Send", on_click=send_message)

    # Container to display the conversation.
    chat_container = st.container()

    # Display the conversation history.
    for message in st.session_state.conversation:
        chat_container.write(message)

# Run the Streamlit App
if __name__ == "__main__":
    streamlit_app()
