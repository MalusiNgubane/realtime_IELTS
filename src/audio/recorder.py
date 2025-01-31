import streamlit as st
from audio_recorder_streamlit import audio_recorder

class AudioRecorder:
    def record(self):
        """Record audio using the streamlit-audio-recorder component."""
        audio_bytes = audio_recorder()
        return audio_bytes