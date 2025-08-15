import speech_recognition as sr

r = sr.Recognizer()

# (Optional) See available mics if you get device errors:
# print(sr.Microphone.list_microphone_names())

with sr.Microphone() as source:
    print("🎙️ Speak now…")
    r.adjust_for_ambient_noise(source, duration=0.6)
    audio = r.listen(source, timeout=5, phrase_time_limit=10)

try:
    text = r.recognize_google(audio, language="en-IN")  # change to hi-IN, te-IN, etc.
    print("You said:", text)
except sr.UnknownValueError:
    print("Couldn’t understand audio.")
except sr.RequestError as e:
    print("Speech API error:", e)
