import streamlit as st
from audio_recorder_streamlit import audio_recorder
import uuid

class AudioRecorder:
    def record(self, show_prompt=True):
        """
        Record audio using the streamlit-audio-recorder component.
        
        Args:
            show_prompt (bool): Whether to display a prompt before recording.
                                  Defaults to True.
        
        Returns:
            bytes: Recorded audio data in WAV format, or None if no audio was recorded.
        """
        # Display a prompt if desired.
        if show_prompt:
            st.write("Click the microphone to start recording:")

        # Use a persistent unique key for the audio recorder widget.
        if "recorder_key" not in st.session_state:
            st.session_state.recorder_key = str(uuid.uuid4())
        
        # Call the audio recorder component with the persistent key.
        audio_bytes = audio_recorder(key=st.session_state.recorder_key, pause_threshold=2.0)
        
        # Check if audio was recorded and provide feedback.
        if audio_bytes:
            st.audio(audio_bytes, format="audio/wav")
        else:
            st.warning("No audio recorded. Please try again.")
        
        return audio_bytes


