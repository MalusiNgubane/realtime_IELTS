# src/utils/feedback.py
from src.llm.examiner import IELTSExaminer
from src.llm.evaluator import IELTSEvaluator
import streamlit as st

class FeedbackGenerator:
    def __init__(self):
        self.evaluator = IELTSEvaluator()
        self.examiner = IELTSExaminer()

    def generate_feedback(self, text):
        """
        Generate detailed feedback for the user's response.
        Args:
            text (str): The user's response.
        Returns:
            dict: A dictionary containing feedback on grammar, vocabulary, and fluency.
        """
        try:
            # Evaluate grammar
            grammar_errors = self.evaluator.evaluate_grammar(text)
            grammar_feedback = f"Grammar errors: {grammar_errors}. " + (
                "Try to avoid common mistakes like subject-verb agreement and tense consistency."
                if grammar_errors > 0
                else "Great job! No grammar errors found."
            )

            # Evaluate vocabulary
            vocab_score = self.evaluator.evaluate_vocabulary(text)
            vocab_feedback = f"Vocabulary score: {vocab_score:.2f}. " + (
                "Try to use more advanced vocabulary and synonyms to improve your lexical resource."
                if vocab_score < 0.7
                else "Excellent use of vocabulary!"
            )

            # Evaluate fluency
            fluency_score = self.evaluator.evaluate_fluency(text)
            fluency_feedback = f"Fluency score: {fluency_score:.2f}. " + (
                "Try to speak more fluently by reducing pauses and using connecting words."
                if fluency_score < 0.7
                else "Great fluency! Keep it up."
            )

            # Generate overall feedback
            overall_feedback = self.examiner.evaluate_response(text)

            # Return feedback as a dictionary
            return {
                "grammar": grammar_feedback,
                "vocabulary": vocab_feedback,
                "fluency": fluency_feedback,
                "overall": overall_feedback,
            }
        except Exception as e:
            st.error(f"Error generating feedback: {e}")
            return {
                "grammar": "Error",
                "vocabulary": "Error",
                "fluency": "Error",
                "overall": "Error",
            }