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

# Streamlit App for the chatbot interface.
def streamlit_app():
    st.title("Chat with an AI Assistant")

    # Create a column layout for the input field and send button.
    col1, col2 = st.columns([5, 1])

    # Store the user input in a text_input field within col1.
    with col1:
        user_input = st.text_input("Your message to the Assistant:", key="input")

    # Create a 'Send' button within col2.
    with col2:
        send_button = st.button("Send")

    # Container to display the conversation.
    chat_container = st.container()

    # Session state to store the conversation history.
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    # When the 'Send' button is clicked, process and display the message.
    if send_button and user_input:
        # Add user's message to the conversation history.
        st.session_state.conversation.append("You: " + user_input)

        # Your Assistant ID
        assistant_id = "asst_td65uaOhWG9zdSoRnKScbTY3"
        
        # Get the response from the assistant and add it to the conversation.
        response = chat_with_assistant(user_input, assistant_id)
        st.session_state.conversation.append("Assistant: " + response)

        # Clear the input field after sending the message.
        st.session_state["input"] = ""

    # Display the conversation history.
    for message in st.session_state.conversation:
        chat_container.write(message)

# Run the Streamlit App
if __name__ == "__main__":
    streamlit_app()
