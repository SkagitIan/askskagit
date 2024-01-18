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
    """"Introducing askSkagit for Government Data Access in Skagit County: Your central hub for all local municipality information.
    Merging various data sources from Skagit County's local governments, askSkagit simplifies your search for government data. 
    Whether you're looking for budget reports, policy documents, or public service information, 
    askSkagit provides a unified, user-friendly platform. With this integration, residents, businesses, 
    and visitors can easily navigate through a comprehensive collection of local government data, making 
    information accessibility in Skagit County more efficient and convenient than ever.""""
)

