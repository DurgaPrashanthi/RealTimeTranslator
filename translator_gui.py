import tkinter as tk
from tkinter import ttk, scrolledtext
import threading, tempfile, os
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound

# --- Functions ---
def speak(text, lang="en"):
    if not text: return
    fd, path = tempfile.mkstemp(suffix=".mp3"); os.close(fd)
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(path)
        playsound.playsound(path)
    finally:
        if os.path.exists(path):
            os.remove(path)

def listen_and_translate():
    output_box.delete(1.0, tk.END)
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            status_label.config(text="🎙️ Listening...")
            root.update()
            r.adjust_for_ambient_noise(source, duration=0.6)
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        text = r.recognize_google(audio, language=src_lang.get())
        status_label.config(text="🔄 Translating...")
        root.update()
        translated = Translator().translate(text, src="auto", dest=dest_lang.get()).text
        output_box.insert(tk.END, translated)
        status_label.config(text="✅ Done")
        speak(translated, lang=dest_lang.get())
    except Exception as e:
        status_label.config(text=f"❌ Error: {e}")

def translate_typed():
    output_box.delete(1.0, tk.END)
    text = input_box.get("1.0", tk.END).strip()
    if not text:
        status_label.config(text="⚠️ No input text")
        return
    try:
        status_label.config(text="🔄 Translating...")
        root.update()
        translated = Translator().translate(text, src="auto", dest=dest_lang.get()).text
        output_box.insert(tk.END, translated)
        status_label.config(text="✅ Done")
        speak(translated, lang=dest_lang.get())
    except Exception as e:
        status_label.config(text=f"❌ Error: {e}")

def start_listen_thread():
    threading.Thread(target=listen_and_translate, daemon=True).start()

def start_type_thread():
    threading.Thread(target=translate_typed, daemon=True).start()

# --- UI ---
root = tk.Tk()
root.title("Real-Time Language Translator")
root.geometry("600x500")

# Dropdown for languages
lang_codes = ["en", "hi", "te", "fr", "es", "de", "ja", "ko", "zh-cn"]

tk.Label(root, text="From (speech):").pack()
src_lang = ttk.Combobox(root, values=["en-IN", "hi-IN", "te-IN"], width=10)
src_lang.set("en-IN")
src_lang.pack()

tk.Label(root, text="To (target):").pack()
dest_lang = ttk.Combobox(root, values=lang_codes, width=10)
dest_lang.set("fr")
dest_lang.pack()

# Input text area
tk.Label(root, text="Type text here (or use mic):").pack()
input_box = scrolledtext.ScrolledText(root, height=5)
input_box.pack(fill="both", padx=10, pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="🎙️ Speak & Translate", command=start_listen_thread).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="⌨️ Translate Typed", command=start_type_thread).grid(row=0, column=1, padx=5)

# Output text area
tk.Label(root, text="Translated text:").pack()
output_box = scrolledtext.ScrolledText(root, height=5)
output_box.pack(fill="both", padx=10, pady=5)

# Status label
status_label = tk.Label(root, text="Idle", fg="blue")
status_label.pack(pady=5)

root.mainloop()
