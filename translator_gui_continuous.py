import tkinter as tk
from tkinter import ttk, scrolledtext
import threading, tempfile, os
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound

# --- Global flag ---
listening = False

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

def continuous_listen():
    global listening
    r = sr.Recognizer()
    t = Translator()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.6)
        status_label.config(text="🎙️ Listening (continuous)...")
        while listening:
            try:
                audio = r.listen(source, timeout=3, phrase_time_limit=7)
                text = r.recognize_google(audio, language=src_lang.get())
                translated = t.translate(text, src="auto", dest=dest_lang.get()).text
                output_box.insert(tk.END, f"You: {text}\n→ {translated}\n\n")
                output_box.see(tk.END)
                speak(translated, lang=dest_lang.get())
            except sr.WaitTimeoutError:
                continue
            except Exception as e:
                output_box.insert(tk.END, f"[Error] {e}\n\n")
                output_box.see(tk.END)
    status_label.config(text="⏹️ Stopped")

def start_continuous():
    global listening
    if listening: return
    listening = True
    threading.Thread(target=continuous_listen, daemon=True).start()

def stop_continuous():
    global listening
    listening = False

# --- UI ---
root = tk.Tk()
root.title("Continuous Real-Time Translator")
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

# Output text area
tk.Label(root, text="Conversation Log:").pack()
output_box = scrolledtext.ScrolledText(root, height=15)
output_box.pack(fill="both", padx=10, pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="▶ Start", command=start_continuous, width=10, bg="lightgreen").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="⏹ Stop", command=stop_continuous, width=10, bg="salmon").grid(row=0, column=1, padx=5)

# Status label
status_label = tk.Label(root, text="Idle", fg="blue")
status_label.pack(pady=5)

root.mainloop()

