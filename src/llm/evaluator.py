import streamlit as st

# Attempt to import LanguageTool from language_tool_python.
# If not available, fall back without raising an error.
try:
    from language_tool_python import LanguageTool
except ImportError:
    LanguageTool = None
    # Use print so that no Streamlit widget is invoked at module level.
    print("Warning: language_tool_python module not found. Grammar evaluation will be disabled.")

class IELTSEvaluator:
    def __init__(self):
        """
        Initialize the IELTSEvaluator with the LanguageTool grammar checker.
        If LanguageTool cannot be initialized (e.g., because it's not installed),
        fall back by setting self.tool to None.
        """
        if LanguageTool:
            try:
                self.tool = LanguageTool('en-US')
            except Exception as e:
                print(f"Warning: LanguageTool initialization failed: {e}")
                self.tool = None
        else:
            self.tool = None

    def evaluate_grammar(self, text):
        """
        Evaluate grammar and return a score between 1 and 10.
        
        Args:
            text (str): The user's response.
        
        Returns:
            float: Grammar score (1-10). If LanguageTool is unavailable,
                   a neutral score (5.0) is returned.
        """
        if self.tool is None:
            # Return a neutral grammar score if the grammar checker isn't available.
            return 5.0

        matches = self.tool.check(text)
        error_count = len(matches)
        if error_count == 0:
            return 10.0
        elif error_count >= 10:
            return 1.0
        else:
            return max(1.0, 10.0 - error_count)

    def evaluate_vocabulary(self, text):
        """
        Evaluate vocabulary usage and return a score between 1 and 10.
        """
        words = text.split()
        unique_words = set(words)
        return min(10.0, len(unique_words) / 5)

    def evaluate_fluency(self, text):
        """
        Evaluate fluency based on the number of words and return a score between 1 and 10.
        """
        return min(10.0, len(text.split()) / 10)
