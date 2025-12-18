import pyttsx3
import speech_recognition as sr

# Initialize EDITH's voice engine once
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    """Make EDITH speak a sentence."""
    engine.say(text)
    engine.runAndWait()

DEVICE_INDEX = 2  # change this to your chosen index

def listen():
    """Listen from the microphone and return recognized text (lowercase)."""
    with sr.Microphone(device_index=DEVICE_INDEX) as source:
        print("EDITH is listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        text = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        speak("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        print("Network error while recognizing speech.")
        speak("There was a problem with the speech service.")
        return ""

if __name__ == "__main__":
    speak("Hello, I am EDITH. Say something after the beep.")
    print("Speak after the beep...")
    text = listen()
    if text:
        speak(f"You said: {text}")

# def listen():
#     """Temporary: read text from keyboard instead of microphone."""
#     text = input("Type your command as if you spoke it: ")
#     return text.lower().strip()

# def handle_command(text):
#     """Decide what EDITH should do based on the text command."""
#     if not text:
#         return

#     if "open" in text and "email" in text:
#         speak("Opening your email.")
#         # TODO: open your email in browser
#         print("[ACTION] Would open your email here.")
#     elif "weather" in text:
#         speak("Checking the weather.")
#         # TODO: call weather API
#         print("[ACTION] Would tell you the weather here.")
#     elif "summarize" in text and "document" in text:
#         speak("Summarizing the document.")
#         # TODO: call your summarizer
#         print("[ACTION] Would summarize the document here.")
#     else:
#         speak("I did not recognize that command yet.")
#         print("[INFO] Unknown command:", text)
        
# if __name__ == "__main__":
#     speak("Hello, I am EDITH. Type your commands to control me.")
#     while True:
#         text = listen()
#         if text in ("exit", "quit", "bye"):
#             speak("Goodbye.")
#             break
#         handle_command(text)
