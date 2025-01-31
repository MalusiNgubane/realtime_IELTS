import streamlit as st
from src.utils.session import init_session_state

def main():
    st.set_page_config(
        page_title="IELTS Speaking Practice",
        page_icon="🎙️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    init_session_state()
    
    # Main page content
    st.title("IELTS Speaking Practice")
    
    # App introduction
    st.write("""
    Welcome to IELTS Speaking Practice! Choose a mode from the sidebar to begin:
    - 📝 Practice Mode: Get instant feedback
    - 📊 Test Mode: Complete IELTS simulation
    """)

if __name__ == "__main__":
    main()