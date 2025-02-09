import streamlit as st
from src.utils.navigation import render_sidebar
from src.audio.recorder import AudioRecorder
from src.audio.processor import AudioProcessor
from src.llm.examiner import IELTSExaminer
from src.llm.evaluator import IELTSEvaluator

# Page configuration: title, icon, and layout.
st.set_page_config(page_title="Practice - IELTS Speaking", page_icon="🎙️", layout="wide")

# Hide default Streamlit menu and footer.
st.markdown(
    "<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>",
    unsafe_allow_html=True
)

# Render the sidebar with navigation.
render_sidebar()

st.title("Practice Mode")

def practice_mode():
    """
    Render the Practice Mode page:
      - Displays a direct examiner question (generated randomly).
      - Prompts the user to record their response.
      - Transcribes the audio response and displays it.
      - Evaluates the response on grammar, vocabulary, and fluency.
      - Generates detailed feedback.
      - Provides a button to restart the session with a new question.
      
    (Visualization of performance data has been removed as requested.)
    """
    # Initialize core components.
    recorder = AudioRecorder()
    processor = AudioProcessor()
    examiner = IELTSExaminer()
    evaluator = IELTSEvaluator()

    # Initialize session state variables.
    if "examiner_question" not in st.session_state:
        st.session_state.examiner_question = examiner.get_new_question(mode="practice")
    if "scores" not in st.session_state:
        st.session_state.scores = []

    # Display the examiner's question.
    st.write("**Examiner:**", st.session_state.examiner_question)

    # Prompt the user to record their response.
    st.info("Click the microphone to start recording your response.")
    audio_bytes = recorder.record(show_prompt=False)

    if audio_bytes:
        # Transcribe the recorded audio.
        text = processor.transcribe(audio_bytes)

        # Display the transcription (or an error if transcription fails).
        if text and text.strip():
            st.write("**Your response:**", text)
        else:
            st.error("Transcription failed or no speech detected. Please try again.")

        # Evaluate and display feedback if transcription is valid.
        if text and text.strip():
            grammar_score = evaluator.evaluate_grammar(text)
            vocabulary_score = evaluator.evaluate_vocabulary(text)
            fluency_score = evaluator.evaluate_fluency(text)

            st.session_state.scores.append({
                "Grammar": grammar_score,
                "Vocabulary": vocabulary_score,
                "Fluency": fluency_score
            })

            st.write("**Grammar Score:**", f"{grammar_score}/10")
            st.write("**Vocabulary Score:**", f"{vocabulary_score}/10")
            st.write("**Fluency Score:**", f"{fluency_score}/10")

            # Generate detailed feedback using the examiner's LLM.
            detailed_feedback = examiner.evaluate_response(text)
            st.write("**Detailed Feedback:**", detailed_feedback)

            # Generate a follow-up question.
            st.session_state.examiner_question = examiner.ask_follow_up(text)

    # Provide a button to restart the practice session.
    if st.button("Restart Practice Session"):
        st.session_state.examiner_question = examiner.get_new_question(mode="practice")
        st.session_state.scores = []
        st.experimental_rerun()

if __name__ == "__main__":
    practice_mode()
