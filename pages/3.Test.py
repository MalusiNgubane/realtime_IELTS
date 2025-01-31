import streamlit as st
from src.audio.recorder import AudioRecorder
from src.audio.processor import AudioProcessor
from src.llm.examiner import IELTSExaminer
from src.llm.evaluator import IELTSEvaluator
from src.utils.report import generate_pdf_report

def test_mode():
    st.title("IELTS Speaking Test")

    # Initialize components
    recorder = AudioRecorder()
    processor = AudioProcessor()
    examiner = IELTSExaminer()
    evaluator = IELTSEvaluator()

    # Initialize session state for test progress
    if "current_part" not in st.session_state:
        st.session_state.current_part = 1
    if "examiner_question" not in st.session_state:
        st.session_state.examiner_question = examiner.ask_question("Introduction")  # Part 1

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

        # Evaluate the response
        grammar_score = evaluator.evaluate_grammar(text)
        vocab_score = evaluator.evaluate_vocabulary(text)
        fluency_score = evaluator.evaluate_fluency(text)

        st.write("Grammar Score:", grammar_score)
        st.write("Vocabulary Score:", vocab_score)
        st.write("Fluency Score:", fluency_score)

        # Move to the next part of the test
        if st.session_state.current_part == 1:
            st.session_state.examiner_question = examiner.ask_question("Cue Card")  # Part 2
        if st.session_state.current_part == 2:
            st.image("static/images/cue_card.png", caption="Cue Card", use_column_width=True)
            st.session_state.current_part = 2
        if st.session_state.current_part == 3:
           st.write("Test complete! Thank you for practicing.")

           # Generate and download the PDF report
           report_path = generate_pdf_report(
               scores={
                   "Grammar": grammar_score,
                   "Vocabulary": vocab_score,
                   "Fluency": fluency_score
                },
                feedback=feedback
           )

    with open(report_path, "rb") as file:
        st.download_button(
            label="Download Report",
            data=file,
            file_name="ielts_report.pdf",
            mime="application/pdf"
        )

        # Rerun the app to display the next question
        st.rerun()

if __name__ == "__main__":
    test_mode()