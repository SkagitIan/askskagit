# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="Government Data Access in Skagit County", page_icon="📈")
st.markdown("# Government Data Access in Skagit County")
st.sidebar.header("Local Governments")
st.write(
    """Introducing askSkagit for Government Data Access in Skagit County: Your central hub for all local municipality information.
    Merging various data sources from Skagit County's local governments, askSkagit simplifies your search for government data. 
    Whether you're looking for budget reports, policy documents, or public service information, 
    askSkagit provides a unified, user-friendly platform. With this integration, residents, businesses, 
    and visitors can easily navigate through a comprehensive collection of local government data, making 
    information accessibility in Skagit County more efficient and convenient than ever.
    """
    )

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
    st.title("Government Assistant")

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
