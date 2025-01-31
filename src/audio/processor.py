from faster_whisper import WhisperModel
import numpy as np

class AudioProcessor:
    def __init__(self):
        # Load Whisper model for speech-to-text
        self.model = WhisperModel("tiny", device="cpu", compute_type="int8")
    
    def transcribe(self, audio_bytes):
        """Transcribe audio bytes to text using Whisper."""
        # Convert audio bytes to numpy array
        audio_np = np.frombuffer(audio_bytes, dtype=np.float32)

        # Transcribe audio
        segments, _ = self.model.transcribe(audio_np, language="en")
        return " ".join([seg.text for seg in segments])