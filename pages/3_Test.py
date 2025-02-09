import streamlit as st
from src.utils.navigation import render_sidebar
from src.audio.recorder import AudioRecorder
from src.audio.processor import AudioProcessor
from src.llm.examiner import IELTSExaminer
from src.llm.evaluator import IELTSEvaluator
from src.utils.report import generate_pdf_report

# Page configuration: title, icon, and layout.
st.set_page_config(page_title="Test - IELTS Speaking", page_icon="🎙️", layout="wide")

# Hide default menu and footer.
st.markdown(
    "<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>", 
    unsafe_allow_html=True
)

# Render the sidebar.
render_sidebar()

st.title("Test Mode")

def test_mode():
    """
    Render the Test Mode page:
      - Displays the examiner's question (progressing through test parts).
      - Records the user's audio response.
      - Transcribes and displays the response.
      - Evaluates the response with scores and detailed feedback.
      - Proceeds through different parts of the test and eventually generates a report.
    """
    # Initialize core components.
    recorder = AudioRecorder()
    processor = AudioProcessor()
    examiner = IELTSExaminer()
    evaluator = IELTSEvaluator()

    # Initialize session state for test progress.
    if "current_part" not in st.session_state:
        st.session_state.current_part = 1
    if "examiner_question" not in st.session_state:
        # Begin with a predefined introductory question.
        st.session_state.examiner_question = examiner.ask_question("Introduction", mode="test")
    if "scores" not in st.session_state:
        st.session_state.scores = []

    # Display the examiner's question.
    st.write("**Examiner:**", st.session_state.examiner_question)

    # Record the audio (the recorder shows its own prompt by default).
    audio_bytes = recorder.record()

    if audio_bytes:
        # Transcribe the audio.
        text = processor.transcribe(audio_bytes)

        # Display the transcription.
        st.write("**Your response:**", text)

        # Evaluate the response.
        grammar_score = evaluator.evaluate_grammar(text)
        vocabulary_score = evaluator.evaluate_vocabulary(text)
        fluency_score = evaluator.evaluate_fluency(text)

        # Append scores.
        st.session_state.scores.append({
            "Grammar": grammar_score,
            "Vocabulary": vocabulary_score,
            "Fluency": fluency_score
        })

        # Display scores.
        st.write("**Grammar Score:**", f"{grammar_score}/10")
        st.write("**Vocabulary Score:**", f"{vocabulary_score}/10")
        st.write("**Fluency Score:**", f"{fluency_score}/10")

        # Generate detailed feedback.
        detailed_feedback = examiner.evaluate_response(text)
        st.write("**Detailed Feedback:**", detailed_feedback)

        # Progress through test parts.
        if st.session_state.current_part == 1:
            # After the introduction, get a new cue card question.
            cue_card_topic = examiner.get_cue_card_topic()
            st.session_state.examiner_question = examiner.ask_question(cue_card_topic, mode="test")
            st.session_state.current_part = 2
        elif st.session_state.current_part == 2:
            # Next part: Discussion.
            st.session_state.examiner_question = examiner.ask_question("Discussion", mode="test")
            st.session_state.current_part = 3
        else:
            # Test is complete – generate a report.
            st.write("**Test complete! Thank you for practicing.**")
            report_path = generate_pdf_report(
                scores=st.session_state.scores,
                feedback="Overall, your performance was good. Keep practicing and work on the detailed feedback provided!"
            )
            with open(report_path, "rb") as file:
                st.download_button(
                    label="Download Report",
                    data=file,
                    file_name="ielts_report.pdf",
                    mime="application/pdf"
                )

if __name__ == "__main__":
    test_mode()
