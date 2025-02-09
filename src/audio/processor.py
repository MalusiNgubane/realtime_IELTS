import streamlit as st
from faster_whisper import WhisperModel
import numpy as np
import logging
import io
import wave

# Configure logging.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@st.cache_resource
def load_whisper():
    """
    Load the Whisper model for speech-to-text transcription.
    
    Returns:
        WhisperModel: The loaded Whisper model.
    """
    try:
        # Load the "tiny" model using CPU with int8 computation for efficiency.
        return WhisperModel("tiny", device="cpu", compute_type="int8")
    except Exception as e:
        logger.error(f"Failed to load Whisper model: {e}")
        raise

class AudioProcessor:
    def __init__(self):
        """
        Initialize the AudioProcessor by loading the Whisper model.
        """
        try:
            self.model = load_whisper()
        except Exception as e:
            st.error(f"Failed to initialize AudioProcessor: {e}")
            raise

    def transcribe(self, audio_bytes):
        """
        Transcribe audio bytes (WAV format) to text using the Whisper model.
        
        Args:
            audio_bytes (bytes): Recorded audio data in WAV format.
        
        Returns:
            str: The transcribed text, or an empty string if transcription fails.
        
        Note: Beam search and zero temperature are used to increase transcription accuracy.
        """
        try:
            # Open the WAV file from the provided audio bytes.
            with wave.open(io.BytesIO(audio_bytes), 'rb') as wf:
                n_channels = wf.getnchannels()
                sampwidth = wf.getsampwidth()
                framerate = wf.getframerate()
                n_frames = wf.getnframes()
                logger.info(f"Audio parameters: Channels: {n_channels}, Sample Width: {sampwidth}, Frame Rate: {framerate}, Frames: {n_frames}")
                
                # Read audio frames.
                frames = wf.readframes(n_frames)
                
                # Convert frames to a normalized numpy array.
                audio_np = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
            
            if len(audio_np) == 0:
                return ""
            
            logger.info(f"Transcribing audio with {len(audio_np)} samples.")
            # Use beam search with beam_size=5 and temperature=0.0 for a more accurate and deterministic transcription.
            segments, _ = self.model.transcribe(audio_np, language="en", beam_size=5, temperature=0.0)
            transcription = " ".join([seg.text for seg in segments])
            return transcription
        except Exception as e:
            logger.error(f"Error transcribing audio: {e}")
            st.error(f"Error transcribing audio: {e}")
            return ""

