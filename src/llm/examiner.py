import streamlit as st
from transformers import pipeline
import random

@st.cache_resource
def load_llm():
    """
    Load the Language Model (LLM) for generating questions and feedback.
    
    Returns:
        pipeline: A Hugging Face text-generation pipeline.
    """
    try:
        # Use Google's FLAN-T5-small for efficient text generation.
        return pipeline(
            "text2text-generation",
            model="google/flan-t5-small",  # A small, fast model.
            device="cpu"  # Change to "cuda" if a GPU is available.
        )
    except Exception as e:
        st.error(f"Failed to load LLM: {e}")
        raise

class IELTSExaminer:
    def __init__(self):
        """
        Initialize the IELTSExaminer by loading the LLM pipeline.
        """
        self.model = load_llm()

    def ask_question(self, topic, mode="test"):
        """
        Generate an IELTS question based on the given topic and mode.
        
        Args:
            topic (str): The topic for the question.
            mode (str): "practice" for direct, engaging questions or "test" for standard test questions.
        
        Returns:
            str: The generated question.
        """
        if mode == "practice":
            prompt = f"""You are an IELTS examiner. Ask the candidate a direct question about "{topic}" for a practice session.
Keep the question concise, direct, and engaging."""
        else:
            prompt = f"""You are an IELTS examiner. Ask the candidate a question about "{topic}".
Keep the question concise and relevant to the IELTS Speaking Test."""
        try:
            result = self.model(prompt, max_length=100, num_return_sequences=1)
            return result[0]['generated_text']
        except Exception as e:
            st.error(f"Failed to generate question: {e}")
            return "Could you tell me more about yourself?"

    def ask_follow_up(self, response):
        """
        Generate a follow-up question based on the user's response.
        
        Args:
            response (str): The user's response.
        
        Returns:
            str: The generated follow-up question.
        """
        prompt = f"""You are an IELTS examiner. The candidate just said: "{response}".
Ask a follow-up question to continue the conversation. Keep the question relevant and concise."""
        try:
            result = self.model(prompt, max_length=100, num_return_sequences=1)
            return result[0]['generated_text']
        except Exception as e:
            st.error(f"Failed to generate follow-up question: {e}")
            return "Could you elaborate on that?"

    def evaluate_response(self, response):
        """
        Generate detailed feedback on the user's response.

        Args:
            response (str): The user's response.

        Returns:
            str: The generated detailed feedback.
        """
        # Modified prompt with clear instructions and a separation marker.
        prompt = f"""You are an experienced IELTS examiner.
Provide a detailed evaluation of the following response:
"{response}"

Please comment thoroughly on grammar, vocabulary, and fluency.
Include specific examples of errors, suggested corrections, and actionable advice for improvement.

Detailed Feedback:"""
        try:
            # Increase max_length to allow for a more comprehensive response.
            result = self.model(prompt, max_length=250, num_return_sequences=1)
            feedback = result[0]['generated_text']
            # If the output starts with the prompt, trim it off.
            if feedback.startswith(prompt):
                feedback = feedback[len(prompt):].strip()
            # In case the feedback is empty, set a fallback message.
            if not feedback:
                feedback = "No detailed feedback was generated. Please try again."
            return feedback
        except Exception as e:
            st.error(f"Failed to generate feedback: {e}")
            return "Your response was clear, but try to use more advanced vocabulary and improve your fluency."

    def get_cue_card_topic(self):
        """
        Retrieve a random cue card topic from a predefined list.
        
        Returns:
            str: A cue card topic.
        """
        CUE_CARD_TOPICS = [
            "Discuss a person who has significantly impacted your life.",
            "Describe an achievement you are proud of.",
            "Describe a successful small business that you know about.",
            "Talk about a hobby or activity you enjoy.",
            "Describe a person often in the news and who you would like to meet.",
            "Discuss a cultural event or festival you have attended.",
            "Describe a recent travel experience.",
            "Describe a performance you enjoyed watching.",
            "Talk about your favourite book or movie.",
            "Describe a crowded place you’ve been to."
        ]
        return random.choice(CUE_CARD_TOPICS)
    
    def get_new_question(self, mode="test"):
        """
        Generate a new question using a random cue card topic.
        
        Args:
            mode (str): "practice" for direct questions, "test" for standard test questions.
        
        Returns:
            str: The generated IELTS question.
        """
        topic = self.get_cue_card_topic()
        return self.ask_question(topic, mode=mode)
