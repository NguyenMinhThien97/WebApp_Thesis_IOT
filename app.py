import streamlit as st
from st_pages import Page, show_pages, add_page_title
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

st.set_page_config(
    page_title="Smart Agriculture",
    page_icon="🌿"
)
# Specify what pages should be shown in the sidebar, and what their titles and icons
show_pages(
    [
        Page("home_page.py", "Smart Agriculture", "🌿"),
        Page("setting_page.py", "Setting", "✏️"),
    ]
)
# adds the title and icon to the current page
add_page_title()

