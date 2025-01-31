from transformers import pipeline
from .prompts import EXAMINER_PROMPT, FEEDBACK_PROMPT, FOLLOW_UP_PROMPT  #import both prompts

class IELTSExaminer:
    def __init__(self):
        # Load a free LLM from Hugging Face (e.g., TinyLlama or FLAN-T5)
        self.model = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # Replace with "google/flan-t5-small" if preferred
            device="cpu"  # Use "cuda" if you have a GPU
        )

    def ask_question(self, topic):
        """Generate an IELTS question based on the topic."""
        prompt = EXAMINER_PROMPT.format(topic=topic)
        result = self.model(prompt, max_length=100, num_return_sequences=1)
        return result[0]['generated_text']
    
    def ask_follow_up(self, response):
        """Generate a follow-up question based on the user's response."""
        prompt = FOLLOW_UP_PROMPT.format(response=response)
        result = self.model(prompt, max_length=100, num_return_sequences=1)
        return result[0]['generated_text']

    def evaluate_response(self, response):
        """Generate feedback on the user's response."""
        prompt = FEEDBACK_PROMPT.format(response=response)
        result = self.model(prompt, max_length=200, num_return_sequences=1)
        return result[0]['generated_text']
