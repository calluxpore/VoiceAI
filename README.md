# 🗣️ AI Voice Assistant with OpenAI GPT-3.5 Turbo

This project creates a conversational AI system using OpenAI's GPT models, allowing users to interact via voice. The AI listens to your voice input, generates a response using OpenAI, and speaks the response aloud using text-to-speech. Additionally, it logs the entire conversation to a text file.

## Features
- Speech-to-Text using the `speech_recognition` library.
- Text generation using OpenAI's GPT-3.5-turbo.
- Text-to-Speech using `pyttsx3`.
- Logs the conversation to a file.

---

## Installation

### 1. **Clone the repository**
```bash
git clone https://github.com/yourusername/conversational-ai-voice.git
cd conversational-ai-voice
```

### 2. **Set Up Python Environment**
It is recommended to use a virtual environment to manage dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. **Install Dependencies**

You need to install the required Python libraries. Note that you must downgrade the OpenAI library for compatibility.

```bash
pip install openai==0.27.8 SpeechRecognition pyttsx3 pyaudio
```

If you encounter issues installing `pyaudio` on Windows, you can use `pipwin`:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## Configuration

### 1. **Add Your OpenAI API Key**

Add your Open API Key

```python
openai.api_key = 'YOUR_OPENAI_API_KEY'
```

To get an API key, sign up at [OpenAI's API page](https://platform.openai.com/signup).

---

## Running the Script

1. **Activate the Virtual Environment** (if not already activated):
   ```bash
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Run the Python Script**:
   ```bash
   python conversation.py
   ```

The AI will start listening for your voice input, respond, and log the conversation to `conversation.txt`.

---
