# Text Speaker 🎙️

A simple and elegant **Text-to-Speech (TTS)** application built with **CustomTkinter** and **pyttsx3**. It allows users to convert written text into spoken words with selectable voices and save audio output locally.

## 🚀 Features
- 🗣️ Supports **two English voices**: **US** and **UK**.
- 🎨 Clean and modern **CustomTkinter** GUI.
- ✍️ Interactive **text box** with placeholder behavior.
- ▶️ **Play** button to instantly read your text aloud.
- 💾 **Save Audio** feature to export speech as an MP3.
- 🧹 **Clear** button to reset the input.
- ⚠️ Input validation with live **feedback messages**.

## 📦 Requirements

Ensure Python is installed, then run:

```bash
pip install customtkinter pyttsx3
📝 pyttsx3 uses your system’s speech engine, so available voices may vary by OS.

▶️ How to Use
Run the application:

bash
Copy
Edit
python texttospeech.py
Type or paste your text into the input area.

Select a voice from the dropdown menu.

Click ▶ Play to hear the speech.

Click 💾 Save Audio to export the speech as a file.

Click 🗑️ Clear to reset the text box.

📂 Output
Saved audio files will be stored as output1.mp3 or output2.mp3 depending on the voice selected.

🛠 Future Enhancements
🎚️ Adjustable speech rate and pitch.

🌍 Support for more voices and languages.

🌗 Light/Dark theme toggle.

📤 Export with custom file names.

📜 License
This project is licensed under the MIT License.

Made with ❤️ using Python & CustomTkinter.