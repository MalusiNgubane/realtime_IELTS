import streamlit as st
from audio_recorder_streamlit import audio_recorder
import uuid

class AudioRecorder:
    def record(self, show_prompt=True):
        """
        Record audio using the streamlit-audio-recorder component.

        Args:
            show_prompt (bool): Whether to display a prompt before recording. Defaults to True.

        Returns:
            bytes: Recorded audio data in WAV format, or None if no audio was recorded.
        """
        # Display a prompt if enabled.
        if show_prompt:
            st.write("Click the microphone to start recording:")

        # Generate a brand-new unique key each time so that no stale binary data is loaded.
        unique_key = str(uuid.uuid4())
        
        # Call the audio recorder widget with the new key.
        audio_bytes = audio_recorder(key=unique_key, pause_threshold=2.0)
        
        # If audio is recorded, play it back for confirmation.
        if audio_bytes:
            st.audio(audio_bytes, format="audio/wav")
        else:
            st.warning("No audio recorded. Please try again.")
        
        return audio_bytes

        

     

