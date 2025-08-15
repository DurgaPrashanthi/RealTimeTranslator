from gtts import gTTS
import playsound
import tempfile, os

text = "Bonjour! Je suis votre traducteur."
lang = "fr"  # match your translation language

tts = gTTS(text=text, lang=lang)
fd, path = tempfile.mkstemp(suffix=".mp3"); os.close(fd)
tts.save(path)
playsound.playsound(path)
os.remove(path)
