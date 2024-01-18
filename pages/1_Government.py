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
import help
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
