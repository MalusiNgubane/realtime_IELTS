# realtime_IELTS 🎙️

A real-time IELTS Speaking Test simulator with AI-powered feedback system. Practice English speaking skills and receive instant evaluations based on official IELTS criteria.

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![IELTS Speaking Practice Demo](demo.gif)

## 🌟 Features

### Test Simulation Modes
- **Practice Mode**: Instant feedback after each response
- **Full Test Mode**: Complete 3-part IELTS simulation
  - Part 1: Introduction & Interview
  - Part 2: Long Turn (Cue Card)
  - Part 3: Discussion

### AI-Powered Assessment
- **Fluency & Coherence**: Analyzes speech rhythm and logical flow
- **Lexical Resource**: Vocabulary range and appropriateness
- **Grammatical Range**: Sentence structure complexity
- **Pronunciation**: Phoneme-level analysis (Beta)

### Core Functionality
- 🎤 Real-time speech-to-text conversion
- 🤖 AI Examiner with natural conversation flow
- 📊 Performance analytics dashboard
- 📄 PDF report generation
- 📈 Progress tracking over time

## 🛠️ Tech Stack

**Frontend**:
- Streamlit (Web Interface)
- CSS Custom Styling

**Backend**:
- Python 3.9+
- Hugging Face Transformers (FLAN-T5)
- OpenAI Whisper (Speech-to-Text)
- LanguageTool (Grammar Checking)

**APIs & Services**:
- Google Text-to-Speech (TTS)
- Streamlit Sharing (Deployment)

## 🚀 Installation

### Prerequisites
- Python 3.9+
- FFmpeg (for audio processing)
- LanguageTool Server (local instance)

### Setup

```bash
git clone https://github.com/MalusiNgubane/realtime_IELTS.git
cd realtime_IELTS
python -m venv ielts-env
source ielts-env/bin/activate  # On Windows: .\ielts-env\Scripts\activate
pip install -r requirements.txt
java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8081
```

### 🖥️ Usage
### Start the application:

```bash
streamlit run main.py
```
Navigation Guide:

- Splash Screen: Entry point with "Enter IELTS" button

- Practice Mode: Interactive Q&A with instant feedback

- Test Mode: Full exam simulation with PDF report

- Progress: Historical performance analysis

**Recording Interface:**

- Click microphone icon to start/stop recording

- Maximum recording duration: 2 minutes

- Automatic transcription after recording stops

## 📂 Project Structure

realtime_IELTS/
├── src/
│   ├── audio/          # Speech processing modules
│   ├── llm/            # AI examiner implementation
│   ├── utils/          # Helper functions and utilities
│   └── database/       # User progress storage
├── pages/              # Streamlit page components
├── static/             # CSS and assets
├── tests/              # Unit and integration tests
├── main.py             # Application entry point
└── requirements.txt    # Dependency list

## 🔍 API Documentation
### LLM Integration

```python
class IELTSExaminer:
    def ask_question(self, topic: str) -> str:
        """Generate IELTS-style question for given topic"""
    
    def evaluate_response(self, response: str) -> dict:
        """Return feedback dictionary with scores 1-10"""
```

### Speech Processing

```python
class AudioProcessor:
    def transcribe(self, audio_bytes: bytes) -> str:
        """Convert audio to text with timestamp metadata"""
```

## 🧠 Why FLAN-T5?

- Optimized for instruction-following tasks

- Low memory footprint (1.2GB)

- Apache 2.0 License

- Comparable performance to larger models

- Local execution capability

## 🚧 Challenges & Solutions
### Challenge	Solution

- LLM Latency	Model quantization & caching
- Audio Sync	WebSocket-based streaming
- Scoring Consistency	Multi-algorithm consensus
- State Management	Streamlit session_state

## 🤝 Contributing
Fork the repository

**Create feature branch:**

```bash

git checkout -b feature/amazing-feature
Commit changes:
```

```bash

git commit -m 'Add some amazing feature'
Push to branch:
```
```bash

git push origin feature/amazing-feature
Open Pull Request
```

## 📜 License
### MIT License - See LICENSE for details

## 🙏 Acknowledgments

- Hugging Face for FLAN-T5 implementation

- OpenAI Whisper team

- Streamlit for UI framework

- LanguageTool for grammar checking

## 📬 Contact
For support or inquiries: support@ielts-practice.com
