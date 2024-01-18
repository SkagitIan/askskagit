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

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="askSkagit",
        page_icon="",
    )

    st.title("Welcome to askSkagit")

    # Introduction
    st.write("""
    askSkagit, your specialized assistant for Skagit Valley, Washington. Powered by OpenAI technology, askSkagit offers a wealth of information about our local community.
    """)

    # For Residents and Visitors
    st.subheader("For Residents and Visitors")
    st.write("""
    Whether you're a resident or visitor, you'll find detailed insights on our rich history, current events, and vibrant community life.
    """)

    # Up-to-date Local Information
    st.subheader("Up-to-date Local Information")
    st.write("""
    We continuously integrate and analyze various local sources, including PDFs, web data, and official documents, ensuring you have the most up-to-date information at your fingertips.
    """)

    # Discover Skagit Valley
    st.subheader("Discover Skagit Valley")
    st.write("""
    Discover Skagit Valley with askSkagit – your guide to the heart of Washington State.
    """)

if __name__ == "__main__":
    run()
