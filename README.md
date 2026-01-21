🎙️ Lecture Voice-to-Notes Generator

A web-based application that converts lecture audio into written text using speech-to-text technology.
The project helps students capture lecture content without manual note-taking.

📌 Problem Statement

Students often miss important points during lectures because listening and writing notes simultaneously is difficult.
This project provides a voice-to-text solution that automatically converts spoken lectures into readable text.

💡 Solution Overview

The Lecture Voice-to-Notes Generator allows users to upload a lecture audio file and receive a text transcription.
The system focuses on accurate transcription, a clean user interface, and offline processing for privacy and reliability.

⚙️ Features

Upload lecture audio (WAV format)

Convert voice into text automatically

Display transcription in a clean UI

Download transcript as a .txt file

Modern UI with background image

Offline speech recognition (local execution)

🛠️ Technologies Used

Python 3.12

Streamlit – Web application framework

Vosk – Offline speech recognition engine

HTML / CSS (via Streamlit) – UI styling

Git & GitHub – Version control

🧠 System Architecture
Lecture Audio (WAV)
        ↓
Offline Speech Recognition (Vosk)
        ↓
Text Transcription
        ↓
Web Interface (Streamlit)

📂 Project Structure
lecture/
├── app.py                  # Streamlit web app
├── transcribe.py           # Speech-to-text logic
├── requirements.txt        # Dependencies
├── background.webp         # UI background image
├── vosk-model-small-en-us-0.15/   # Speech recognition model
└── README.md

🚀 How to Run the Project Locally (FULLY FUNCTIONAL)
✅ Step 1: Install Python

Install Python 3.12

Make sure Python is added to PATH

Verify:

python --version

✅ Step 2: Install dependencies

Inside the project folder:

pip install -r requirements.txt

✅ Step 3: Download Vosk Model

Download the model from:
https://alphacephei.com/vosk/models

Download:

vosk-model-small-en-us-0.15.zip


Extract it

Place the extracted folder inside the project directory

✅ Step 4: Run the application
streamlit run app.py


The browser will open automatically.

✅ Step 5: Use the app

Upload a WAV audio file

Wait for transcription

View and download the transcript

✔ This version supports real audio transcription

🎧 Audio Requirements (IMPORTANT)

For best results:

Format: WAV

Channel: Mono

Clear speech

Minimal background noise

Duration: preferably under 5 minutes

☁️ Streamlit Cloud Deployment (Important Explanation)
❗ Why transcription does not work on Streamlit Cloud

Streamlit Cloud runs applications inside a restricted container environment.
Offline speech recognition engines like Vosk require native system dependencies that are not supported on Streamlit Cloud.

Result:

✅ Local version → Full speech-to-text functionality

⚠️ Cloud version → UI demonstration only

The deployed version is intended to showcase:

Interface design

Workflow

Project structure

🧪 Testing Strategy

Tested locally on Windows

Controlled audio recordings used for accuracy

Manual verification of transcription output

🔮 Future Enhancements

Real-time microphone recording

Multi-language transcription

Timestamped transcripts

Summarization and study notes

Cloud-based transcription using APIs

🎓 Academic Justification

This project demonstrates:

Practical use of speech-to-text technology

Offline AI system design

UI/UX integration with backend logic

Real-world deployment considerations

👩‍💻 Author

annliasunil

📄 License

This project is developed for educational and academic purposes.# 🎙️ Lecture Voice-to-Notes Generator

A web-based application that converts lecture audio into text (speech-to-text), helping students capture lecture content without manual note-taking.

---

## 📌 Project Overview

Students often miss important points during lectures because listening and writing simultaneously is difficult.  
This project provides a **voice-to-text transcription system** that converts spoken lecture audio into written text automatically.

The system is designed with a **simple, clean user interface** and focuses on **accurate transcription** as its core functionality.

---

## ⚙️ Features

- Upload lecture audio (WAV format)
- Convert voice into text automatically
- Display transcribed text in a clean interface
- Download transcript as a text file
- Modern, user-friendly UI with background image
- Offline speech recognition (local execution)

---

## 🛠️ Technologies Used

- **Python 3.12**
- **Streamlit** – Web interface
- **Vosk** – Offline speech-to-text engine
- **HTML/CSS (via Streamlit)** – UI customization
- **Git & GitHub** – Version control

---

## 🧠 System Architecture

