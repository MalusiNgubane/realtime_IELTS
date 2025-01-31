import streamlit as st

def progress_page():
    st.title("Progress Tracking")

    # Example progress data
    if "scores" in st.session_state:
        progress_data = st.session_state.scores
    else:
        progress_data = {
            "Grammar": [7, 8, 9],
            "Vocabulary": [6, 7, 8],
            "Fluency": [5, 6, 7]
        }

    # Display progress charts
    st.line_chart(progress_data)

if __name__ == "__main__":
    progress_page()