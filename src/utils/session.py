import streamlit as st
from datetime import datetime

def init_session_state():
    """Initialize session state variables."""
    if 'user_responses' not in st.session_state:
        st.session_state.user_responses = []
    if 'scores' not in st.session_state:
        st.session_state.scores = {
            "Grammar": [],
            "Vocabulary": [],
            "Fluency": []
        }
    if 'current_section' not in st.session_state:
        st.session_state.current_section = 'introduction'
    if 'start_time' not in st.session_state:
        st.session_state.start_time = datetime.now()