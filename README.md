Real-Time Language Translator 🎙️🌐

A Python-based application that listens to spoken language in real-time, translates it into another language, and provides both text and speech output.
This project is designed to break language barriers and enable seamless communication between people speaking different languages.

✨ Features

🎧 Real-time Speech Recognition – Capture and process spoken words instantly.

🌍 Multi-Language Translation – Supports a wide range of languages.

🔊 Text-to-Speech Output – Hear translations spoken aloud.

🖥️ User-Friendly GUI – Simple interface built with Tkinter.

🔄 Continuous Translation Mode – Keeps translating without manual restarts.

🛠️ Tech Stack

Python 3.x

SpeechRecognition – For converting speech to text.

Googletrans / Deep Translator – For translating text.

gTTS (Google Text-to-Speech) – For converting translations to speech.

Tkinter – For building the GUI.

📦 Installation
# Clone the repository
git clone https://github.com/YourUsername/RealTimeTranslator.git
cd RealTimeTranslator

# Install dependencies
pip install -r requirements.txt

🚀 Usage
# Run the GUI application
python translator_gui.py


Or, for continuous translation mode:

python translator_gui_continuous.py

📂 Project Structure
RealTimeTranslator/
│-- listen.py                  # Handles speech input
│-- translate.py                # Translation logic
│-- translate_basic.py          # Basic translation version
│-- translator_gui.py           # GUI-based translator
│-- translator_gui_continuous.py# Continuous translation GUI
│-- tts.py                      # Text-to-speech functions
│-- requirements.txt            # Dependencies list

💡 Future Enhancements

🌐 Add offline translation support.

🎨 Improve GUI design.

📱 Convert into a mobile application.

📜 License

This project is open-source and available under the MIT License.