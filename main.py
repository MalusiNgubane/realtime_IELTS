import streamlit as st

# Must be the first Streamlit command
st.set_page_config(
    page_title="IELTS Speaking Practice",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def set_styles():
    """
    Set custom styles for the app.
    """
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .splash-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 80vh;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    """
    Render the splash screen and handle navigation to the home page.
    """
    set_styles()
    
    # Splash screen content
    st.markdown("""
        <div class="splash-container">
            <div style="font-size: 80px;">🎙️</div>
            <h1>Welcome to IELTS Speaking Practice</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Center the "Enter IELTS" button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Enter IELTS", key="enter_button"):
            st.switch_page("pages/1_🏠_Home.py")  # Redirect to the home page

if __name__ == "__main__":
    main()