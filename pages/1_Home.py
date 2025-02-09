import streamlit as st
from src.utils.navigation import render_sidebar

# Page configuration
st.set_page_config(page_title="IELTS Speaking Practice", page_icon="🎙️", layout="wide")

# Hide default menu and footer
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>", 
            unsafe_allow_html=True)

# Add contact info to sidebar
render_sidebar()

# Main content
st.title("IELTS Speaking Practice")
st.header("Welcome! 🚀")

# Additional context about the app and its purpose
st.markdown("""
**About This App:**

Welcome to the IELTS Speaking Practice App—your comprehensive solution for preparing for the IELTS speaking test. This interactive platform has been designed to simulate a real IELTS speaking test experience, providing you with:

- **Real-time feedback:** Receive immediate, AI-driven insights on your pronunciation, grammar, and vocabulary.
- **AI-powered examiner simulation:** Engage with a dynamic virtual examiner that asks relevant IELTS-style questions.
- **Detailed performance analysis:** Monitor your progress with analytics and personalized recommendations, ensuring you focus on areas that need improvement.
- **Practice and Test Modes:** Whether you need to refine your speaking skills or take a full simulation of the IELTS test, this app offers both options for a tailored learning experience.
- **User-friendly Interface:** Enjoy a streamlined design that makes navigation and practice as simple as possible.

Our mission is to help you build confidence and improve your English speaking skills through an innovative, tech-driven approach. Get ready to transform your IELTS preparation experience!
""")

col1, col2 = st.columns(2)
with col1:
    st.subheader("📝 Practice Mode")
    st.write("• Real-time feedback\n• AI-powered analysis\n• Pronunciation assessment")
    st.subheader("📊 Test Mode")
    st.write("• Complete simulations\n• Professional evaluation\n• Detailed reports")
with col2:
    st.subheader("📈 Progress Tracking")
    st.write("• Performance analytics\n• Skill breakdown\n• Personalized recommendations")




