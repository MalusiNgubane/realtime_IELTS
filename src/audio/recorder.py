import streamlit as st
from audio_recorder_streamlit import audio_recorder

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

        # Use a fixed key so that the widget state remains consistent during a single run.
        key = "audio_recorder"
        audio_bytes = audio_recorder(key=key, pause_threshold=2.0)
        
        # If audio was recorded, play it back for confirmation.
        if audio_bytes:
            st.audio(audio_bytes, format="audio/wav")
        else:
            st.warning("No audio recorded. Please try again.")

        # Remove the recorder's entry from session state to prevent binary data from being rehydrated
        # (which would trigger JSONDecodeError on rerun).
        if key in st.session_state:
            del st.session_state[key]
        
        return audio_bytes
<<<<<<< HEAD




=======
>>>>>>> bdaa281c98517f6955af6f84abee95d602dc63d2
