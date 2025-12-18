import speech_recognition as sr

DEVICE_INDEX = 2  # try 33, then 34, then 2, then 19, one by one

r = sr.Recognizer()

print("Trying microphone index:", DEVICE_INDEX)

with sr.Microphone(device_index=DEVICE_INDEX) as source:
    print("Opened mic. Speak now...")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source, timeout=5, phrase_time_limit=5)

try:
    text = r.recognize_google(audio, language="en-IN")
    print("You said:", text)
except Exception as e:
    print("Recognition error:", e)
