from openai import OpenAI
import streamlit as st

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

def display_section(title, key):
    """
    Display a section with a question input and response area.
    """
    st.subheader(title)

    # Text input for user questions
    user_question = st.text_input("Ask a question:", key=f"input_{key}")

    # Button for sending the question
    if st.button("Submit", key=f"button_{key}"):
        # Assistant response
        assistant_id = "asst_td65uaOhWG9zdSoRnKScbTY3"
        response = chat_with_assistant(user_question, assistant_id)
        st.session_state[f"response_{key}"] = response

    # Display the assistant's response
    if f"response_{key}" in st.session_state:
        st.text_area("Response:", st.session_state[f"response_{key}"], key=f"response_area_{key}", height=100)

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
