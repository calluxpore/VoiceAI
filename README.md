# 🗣️ AI Voice Assistant with OpenAI GPT-3.5 Turbo

This project creates a conversational AI system using OpenAI's GPT models, allowing users to interact via voice. The AI listens to your voice input, generates a response using OpenAI, and speaks the response aloud using text-to-speech. Additionally, it logs the entire conversation to a text file.

## Features
- **Speech-to-Text**: Uses the `speech_recognition` library to capture and transcribe voice input.
- **Text Generation**: Generates responses using OpenAI's GPT-3.5-turbo model.
- **Text-to-Speech**: Converts text responses to speech using the `pyttsx3` library.
- **Conversation Logging**: Logs the conversation to a file (`conversation.txt`).

---

## Required Packages

Before running the project, you need to install the following Python packages:

- **`openai==0.27.8`**: For interacting with the GPT-3.5-turbo model.
- **`SpeechRecognition`**: For capturing and converting voice input to text.
- **`pyttsx3`**: For converting the generated text into speech.
- **`pyaudio`**: Required by `SpeechRecognition` to access the microphone.

### Install these packages using the following commands:

```bash
# Install OpenAI with specific version
pip install openai==0.27.8

# Install SpeechRecognition
pip install SpeechRecognition

# Install pyttsx3
pip install pyttsx3

# Install pyaudio
pip install pyaudio
```

### **Note for Windows Users**:
If you encounter issues while installing `pyaudio`, use `pipwin` to install it:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## Installation

### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/conversational-ai-voice.git
cd conversational-ai-voice
```

### 2. **Set Up Python Environment**

To avoid conflicts with other Python packages, it's recommended to use a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. **Install Required Libraries**

If you haven’t already installed the required packages, use the following commands:

```bash
pip install openai==0.27.8 SpeechRecognition pyttsx3 pyaudio
```

#### For Windows Users:
If you encounter issues while installing `pyaudio`, use `pipwin` as mentioned earlier:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## Configuration

### 1. **Add Your OpenAI API Key**

You need to add your OpenAI API key to the script. Open the `conversation.py` file and update the following line:

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

The AI will start listening for your voice input, generate responses using GPT-3.5, and speak the responses aloud using text-to-speech. All conversations will be logged in `conversation.txt`.

---

## Verifying Installed Packages

You can verify that all the necessary packages are installed by using the following commands:

```bash
pip show openai
pip show SpeechRecognition
pip show pyttsx3
pip show pyaudio
```

Make sure all required packages are installed and correctly configured before running the script.
