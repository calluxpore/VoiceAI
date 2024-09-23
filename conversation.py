import openai
import speech_recognition as sr
import pyttsx3
import os

# Set your OpenAI API key
openai.api_key = ('OPENAI_API_KEY')

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Conversation log file
conversation_file = 'conversation.txt'

# Initialize recognizer
r = sr.Recognizer()

# Function to get audio input from the user and convert it to text
def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not get that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

# Function to get response from OpenAI
def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or 'gpt-4' if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=150,
        n=1,
        stop=None
    )
    message = response['choices'][0]['message']['content']
    print(f"AI: {message}")
    return message

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main conversation loop
def main():
    if not os.path.exists(conversation_file):
        with open(conversation_file, 'w') as f:
            f.write("Conversation Log\n")
            f.write("================\n\n")

    while True:
        user_input = get_audio()
        if user_input:
            # Save user's input to file
            with open(conversation_file, 'a') as f:
                f.write(f"You: {user_input}\n")

            # Get AI's response
            ai_response = get_response(user_input)

            # Save AI's response to file
            with open(conversation_file, 'a') as f:
                f.write(f"AI: {ai_response}\n\n")

            # Speak AI's response
            speak(ai_response)

if __name__ == "__main__":
    main()
