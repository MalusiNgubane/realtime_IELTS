import streamlit as st
import pandas as pd
from src.utils.report import generate_pdf_report
from src.utils.navigation import render_sidebar

# Page configuration.
st.set_page_config(page_title="Progress - IELTS Speaking", page_icon="🎙️", layout="wide")

# Hide default Streamlit menu and footer.
st.markdown(
    "<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>", 
    unsafe_allow_html=True
)

# Render the sidebar.
render_sidebar()

st.title("Progress Tracking")

def progress_page():
    """
    Render the Progress Tracking page:
      - Displays progress charts of your performance over time.
      - Shows a detailed table of scores.
      - Provides a downloadable PDF report with overall progress and feedback.
    """
    # Check if there are any recorded scores.
    if "scores" not in st.session_state or not st.session_state.scores:
        st.warning("No progress data available. Complete a practice or test session to see your progress.")
    else:
        # Convert scores to a DataFrame.
        progress_data = pd.DataFrame(st.session_state.scores)

        # Display a line chart of performance.
        st.subheader("Your Progress Over Time")
        st.line_chart(progress_data)

        # Display detailed scores.
        st.subheader("Detailed Scores")
        st.write(progress_data)

        # Generate and provide a downloadable report.
        report_path = generate_pdf_report(
            scores=progress_data.to_dict(orient="records"),
            feedback="Overall, your performance is showing promise. Analyze the detailed feedback and continue to practice to improve further."
        )
        with open(report_path, "rb") as file:
            st.download_button(
                label="Download Progress Report",
                data=file,
                file_name="ielts_progress_report.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    progress_page()
