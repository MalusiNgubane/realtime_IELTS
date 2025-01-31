# src/llm/evaluator.py

from language_tool_python import LanguageTool

class IELTSEvaluator:
    def __init__(self):
        self.tool = LanguageTool('en-US')

    def evaluate_grammar(self, text):
        """Evaluate grammar and return the number of errors."""
        matches = self.tool.check(text)
        return len(matches)

    def evaluate_vocabulary(self, text):
        """Evaluate vocabulary usage and return a score."""
        # Simple heuristic: Count the number of unique words
        words = text.split()
        unique_words = set(words)
        return len(unique_words) / len(words) if words else 0

    def evaluate_fluency(self, text):
        """Evaluate fluency based on response length and pauses."""
        # Simple heuristic: Fluency is higher for longer responses
        return len(text.split()) / 50  # Normalize to a score out of 10