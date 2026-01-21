# 🎙️ Lecture Voice-to-Notes Generator

A web-based application that converts lecture audio into written text using speech-to-text technology.  
This project helps students capture lecture content without manual note-taking.

---

## 📌 Problem Statement

Students often miss important points during lectures because it is difficult to listen and write notes at the same time.  
There is a need for a system that can automatically convert spoken lectures into readable text.

---

## 💡 Solution Overview

The **Lecture Voice-to-Notes Generator** converts recorded lecture audio into text automatically.  
The system focuses on:

- Accurate speech-to-text conversion  
- Simple and clean user interface  
- Offline processing for privacy and reliability  

---

## ⚙️ Features

- Upload lecture audio (WAV format)
- Convert voice into text automatically
- Display transcription in a clean interface
- Download the transcript as a text file
- Modern UI with background image
- Offline speech recognition (local execution)

---

## 🛠️ Technologies Used

- **Python 3.12**
- **Streamlit** – Web application framework
- **Vosk** – Offline speech recognition engine
- **HTML & CSS (via Streamlit)** – UI styling
- **Git & GitHub** – Version control

---
## 🧠 System Architecture
Lecture Audio (WAV)
↓
Offline Speech Recognition (Vosk)
↓
Text Transcription
↓
Web Interface (Streamlit)


---

## 📂 Project Structure
lecture/
├── app.py # Streamlit web app
├── transcribe.py # Speech-to-text logic
├── requirements.txt # Project dependencies
├── background.webp # Background image for UI
├── vosk-model-small-en-us-0.15/ # Vosk speech model
└── README.md


---

## 🚀 How to Run the Project Locally (Fully Functional)

### ✅ Step 1: Install Python
Install **Python 3.12** and ensure it is added to PATH.

Verify installation:
```bash
python --version

pip install -r requirements.txt

download- vosk-model-small-en-us-0.15.zip

run - streamlit run app.py

## ✅ How to Use the Application

1. Upload a **WAV lecture audio file**
2. Wait while the audio is transcribed
3. View the transcribed text on the screen
4. Download the transcript if required

✔ The local version fully supports **real audio transcription**

---

## 🎧 Audio Requirements (Important)

For best transcription accuracy, ensure that the audio meets the following conditions:

- **Format:** WAV  
- **Channel:** Mono  
- **Speech:** Clear and well-articulated  
- **Noise:** Minimal background noise  
- **Duration:** Preferably under **5 minutes**

---

## ☁️ Streamlit Cloud Deployment (Important Note)

### ❗ Why transcription does not work on Streamlit Cloud

Streamlit Cloud runs applications inside a **restricted container environment**.  
Offline speech recognition engines like **Vosk** require native system-level dependencies, which are **not supported** on Streamlit Cloud.

### As a result:

- ✅ **Local version:** Full speech-to-text functionality  
- ⚠️ **Cloud version:** UI and workflow demonstration only  

The deployed version is intended to showcase:
- Interface design  
- Application workflow  
- Project structure  

---

## 🧪 Testing Strategy

- Tested locally on **Windows**
- Controlled audio recordings used for testing
- Manual verification of transcription output

---

## 🔮 Future Enhancements

- Real-time microphone recording
- Multi-language transcription
- Timestamped transcripts
- Lecture summarization
- Cloud-based transcription using APIs

---

## 🎓 Academic Justification

This project demonstrates:

- Practical application of speech-to-text technology  
- Offline AI system design  
- UI/UX integration with backend logic  
- Awareness of real-world deployment constraints  

---

## 👩‍💻 Author

**annliasunil**



## 🧠 System Architecture

