import streamlit as st
import openai
import time

def chat_with_assistant(user_input, assistant_id):
    client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Create a Thread for the conversation
    thread = client.beta.threads.create()

    # Add User's message to the Thread
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )

    # Run the Assistant to respond using the provided assistant ID
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id
    )

    # Check the status of the Run and wait until it is completed
    while run.status != "completed":
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

    # Retrieve the Assistant's response
    messages = client.beta.threads.messages.list(thread_id=thread.id, order="asc")
    response = ""
    for message in messages.data:
        if message.role == "assistant":
            for content_item in message.content:
                if content_item.type == 'text':
                    response += content_item.text.value + "\n"
    return response if response else "No response from the assistant."

def streamlit_app():
    st.title("askSkagit Anything!")

    # Initialize conversation history in session state
    if 'history' not in st.session_state:
        st.session_state.history = ""

    user_input = st.text_input("Your message to the Assistant:", key="user_input")

    if st.button("Send"):
        if user_input:
            # Append user message to history
            st.session_state.history += f"You: {user_input}\n"
            
            # Your Assistant ID
            assistant_id = "asst_td65uaOhWG9zdSoRnKScbTY3"
            response = chat_with_assistant(user_input, assistant_id)
            
            # Append assistant response to history
            st.session_state.history += f"Assistant: {response}\n"

            # Clear the input box after sending
            st.session_state.user_input = ""

    # Display the conversation history
    st.text_area("Conversation History:", st.session_state.history, height=300)

# Run the Streamlit App
streamlit_app()
