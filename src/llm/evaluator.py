from language_tool_python import LanguageTool

class IELTSEvaluator:
    def __init__(self):
        """
        Initialize the IELTSEvaluator with the LanguageTool grammar checker.
        """
        self.tool = LanguageTool('en-US')

    def evaluate_grammar(self, text):
        """
        Evaluate grammar and return a score between 1 and 10.
        
        Args:
            text (str): The user's response.
        
        Returns:
            float: Grammar score (1-10), with fewer errors yielding a higher score.
        """
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
