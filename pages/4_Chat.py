import streamlit as st
import openai
import time

# This function handles the chat interaction with the OpenAI assistant.
def chat_with_assistant(user_input, assistant_id):
    # Initialize the OpenAI client with the API key from Streamlit secrets.
    client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Create a Thread for the conversation.
    thread = client.beta.threads.create()

    # Add the user's message to the Thread.
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )

    # Run the Assistant to respond using the provided assistant ID.
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id
    )

    # Wait until the run is completed, checking the status.
    while run.status != "completed":
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

    # Retrieve the Assistant's response and format it.
    messages = client.beta.threads.messages.list(thread_id=thread.id, order="asc")
    response = ""
    for message in messages.data:
        if message.role == "assistant":
            for content_item in message.content:
                if content_item.type == 'text':
                    response += content_item.text.value + "\n"
    return response if response else "No response from the assistant."

def send_message():
    """Send the message and clear the input field."""
    user_input = st.session_state.user_input
    if user_input:
        # Add user's message to the conversation history.
        st.session_state.conversation.append("You: " + user_input)

        # Your Assistant ID
        assistant_id = "asst_td65uaOhWG9zdSoRnKScbTY3"
        
        # Get the response from the assistant and add it to the conversation.
        response = chat_with_assistant(user_input, assistant_id)
        st.session_state.conversation.append("Assistant: " + response)

        # Clear the input field.
        st.session_state.user_input = ""

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
