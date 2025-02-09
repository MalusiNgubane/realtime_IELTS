# File: src/utils/navigation.py

import streamlit as st

def render_sidebar():
    """
    Creates a consistent sidebar with contact information.
    Navigation is handled by Streamlit's native page system.
    """
    with st.sidebar:
        st.markdown("---")
        st.write("📩 support@ielts-practice.com")
