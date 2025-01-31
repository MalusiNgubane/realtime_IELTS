import streamlit as st
from src.audio.recorder import AudioRecorder
from src.audio.processor import AudioProcessor
from src.llm.examiner import IELTSExaminer
from src.llm.evaluator import IELTSEvaluator
from src.utils.feedback import generate_feedback

def practice_mode():
    st.title("Practice Mode")
    
    # Initialize components
    recorder = AudioRecorder()
    processor = AudioProcessor()
    examiner = IELTSExaminer()
    evaluator = IELTSEvaluator()

    # Initialize session state for follow-up questions
    if "follow_up" not in st.session_state:
        st.session_state.follow_up = False
    if "examiner_question" not in st.session_state:
        st.session_state.examiner_question = examiner.ask_question("Technology")  # Default topic

        # Display examiner's question
    st.write("Examiner:", st.session_state.examiner_question)
    
    # Record audio
    audio_bytes = recorder.record()
    
    if audio_bytes:
        # Process audio
        text = processor.transcribe(audio_bytes)

        # Display user response
        st.write("Your response:", text)
        
        # Get examiner feedback
        feedback = examiner.evaluate_response(text)
        st.write("Feedback:", feedback)

        st.markdown(f"""
    <div class="feedback-box">
        <h4>Feedback:</h4>
        <p>{feedback}</p>
    </div>
    """,
    unsafe_allow_html=True)

        # Evaluate the response
        grammar_score = evaluator.evaluate_grammar(text)
        vocab_score = evaluator.evaluate_vocabulary(text)
        fluency_score = evaluator.evaluate_fluency(text)

        st.write("Grammar Score:", grammar_score)
        st.write("Vocabulary Score:", vocab_score)
        st.write("Fluency Score:", fluency_score)

        # Ask a follow-up question
        st.session_state.examiner_question = examiner.ask_follow_up(text)
        st.session_state.follow_up = True
        
        # Rerun the app to display the follow-up question
        st.rerun()

if __name__ == "__main__":
    practice_mode()