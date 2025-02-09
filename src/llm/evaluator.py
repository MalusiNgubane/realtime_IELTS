import streamlit as st

# Attempt to import LanguageTool. If it fails (for example, due to missing Java),
# we fall back to a dummy implementation.
try:
    from language_tool_python import LanguageTool
except Exception as e:
    st.error(f"Failed to import language_tool_python: {e}")
    LanguageTool = None

class IELTSEvaluator:
    def __init__(self):
        """
        Initialize the IELTSEvaluator with the LanguageTool grammar checker.
        If LanguageTool cannot be initialized (e.g. due to missing Java),
        fall back to a dummy evaluator.
        """
        if LanguageTool is not None:
            try:
                self.tool = LanguageTool('en-US')
            except Exception as e:
                st.error(f"LanguageTool initialization failed: {e}")
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
                   a neutral score is returned.
        """
        if self.tool is None:
            # Fall back to a neutral score if grammar checking is not available.
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
        
        Args:
            text (str): The user's response.
        
        Returns:
            float: Vocabulary score (1-10).
        """
        words = text.split()
        unique_words = set(words)
        return min(10.0, len(unique_words) / 5)  # Normalize to a score out of 10

    def evaluate_fluency(self, text):
        """
        Evaluate fluency based on response length.
        
        Args:
            text (str): The user's response.
        
        Returns:
            float: Fluency score (1-10).
        """
        # Heuristic: More words suggest higher fluency.
        return min(10.0, len(text.split()) / 10)  # Normalize to a score out of 10
