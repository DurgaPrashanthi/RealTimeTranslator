import os, tempfile, threading
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound

def speak(text, lang="en"):
    if not text: return
    fd, path = tempfile.mkstemp(suffix=".mp3"); os.close(fd)
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(path)
        th = threading.Thread(target=playsound.playsound, args=(path,), daemon=True)
        th.start(); th.join()
    finally:
        if os.path.exists(path): os.remove(path)

def listen_once(lang_code="en-IN"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now…")
        r.adjust_for_ambient_noise(source, duration=0.6)
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
    try:
        return r.recognize_google(audio, language=lang_code)
    except Exception:
        return None

def translate_text(text, dest="en", src="auto"):
    if not text: return ""
    try:
        return Translator().translate(text, src=src, dest=dest).text
    except Exception as e:
        print("Translation error:", e)
        return ""

if __name__ == "__main__":
    speech_lang = input("Speech language (e.g., en-IN, hi-IN) [default en-IN]: ").strip() or "en-IN"
    target = input("Target language (e.g., en, hi, te, fr) [default en]: ").strip().lower() or "en"

    while True:
        cmd = input("\nPress ENTER to listen, or 'q' to quit: ").strip().lower()
        if cmd == "q": break

        heard = listen_once(speech_lang)
        if not heard:
            print("Didn’t catch that. Try again.")
            continue

        print("🗣️ You said:", heard)
        translated = translate_text(heard, dest=target)
        print(f"🌐 Translated [{target}]:", translated)
        speak(translated, lang=target)
