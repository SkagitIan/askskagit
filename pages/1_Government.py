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

import streamlit as st

def display_information():
    st.title("Community Information Hub")

    st.header("Key Topics and Services")

    # Property Taxes and Assessments
    st.subheader("Property Taxes and Assessments")
    st.write("""
    - Questions about how property taxes are calculated.
    - Assessment processes.
    - Deadlines for tax payments.
    """)
    display_section("Property Taxes and Assessments", "taxes")

    # Building and Zoning Permits
    st.subheader("Building and Zoning Permits")
    st.write("""
    - Inquiries about obtaining permits for new construction, renovations, or zoning regulations.
    """)
    display_section("Building and Zoning Permits", "permits")

    # Public Safety and Law Enforcement
    st.subheader("Public Safety and Law Enforcement")
    st.write("""
    - Questions related to local police services, crime statistics, and public safety initiatives.
    """)
    display_section("Building and Zoning Permits", "permits")

    # Waste Management and Recycling
    st.subheader("Waste Management and Recycling")
    st.write("""
    - Queries about garbage pick-up schedules, recycling programs, and waste disposal guidelines.
    """)
    display_section("Waste Management and Recycling", "waste")

    # Local Legislation and Policy
    st.subheader("Local Legislation and Policy")
    st.write("""
    - Questions about current local laws, upcoming legislation, and citizen participation in local governance.
    """)
    display_section("Local Legislation and Policy", "legal")

    # Public Transportation
    st.subheader("Public Transportation")
    st.write("""
    - Information on public transportation options, schedules, and fare rates.
    """)
    display_section("Public Transportation", "transpo")

    # Public Works and Infrastructure
    st.subheader("Public Works and Infrastructure")
    st.write("""
    - Inquiries about road maintenance, public utilities, and ongoing infrastructure projects.
    """)
    display_section("Public Works and Infrastructure", "works")

    # Community Events and Programs
    st.subheader("Community Events and Programs")
    st.write("""
    - Information about local events, recreational programs, and community services.
    """)
    display_section("Community Events and Programs", "events")

    # Schools and Education
    st.subheader("Schools and Education")
    st.write("""
    - Questions about local public schools, educational programs, and school district policies.
    """)
    display_section("Schools and Education", "schools")

    # Health and Social Services
    st.subheader("Health and Social Services")
    st.write("""
    - Information about local health services, social welfare programs, and support services.
    """)
    display_section("Health and Social Services", "health")

    # Business Licensing and Regulations
    st.subheader("Business Licensing and Regulations")
    st.write("""
    - Queries about starting a business, business licenses, and local commercial regulations.
    """)
    display_section("Business Licensing and Regulations", "license")

    # Environmental Conservation
    st.subheader("Environmental Conservation")
    st.write("""
    - Questions about local environmental policies, conservation efforts, and sustainability initiatives.
    """)
    display_section("Environmental Conservation", "enviro")

    # Voting and Elections
    st.subheader("Voting and Elections")
    st.write("""
    - Information on voter registration, election dates, and polling locations.
    """)
    display_section("Voting and Elections", "voting")

    # Housing and Urban Development
    st.subheader("Housing and Urban Development")
    st.write("""
    - Inquiries about affordable housing, urban planning, and development projects.
    """)
    display_section("Housing and Urban Development", "housing")

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
