===========================================================
🎙️ LECTURE VOICE-TO-NOTES GENERATOR
===========================================================

Lecture Voice-to-Notes Generator is a web-based application 
that converts lecture audio into written text using offline 
speech-to-text technology. 

The project helps students focus on listening during lectures 
instead of manually writing notes.

-----------------------------------------------------------
📌 PROBLEM STATEMENT
-----------------------------------------------------------
Students often miss important points during lectures because 
it is difficult to listen and write notes at the same time. 
Manual note-taking can be incomplete and inaccurate.

There is a need for a system that can automatically convert 
spoken lectures into readable text.

-----------------------------------------------------------
💡 SOLUTION OVERVIEW
-----------------------------------------------------------
The Lecture Voice-to-Notes Generator provides an automated 
voice-to-text solution. Users can upload recorded lecture 
audio files, which are then transcribed into text using 
speech recognition technology.

The system is designed to be simple, offline, and easy to use.

-----------------------------------------------------------
⚙️ FEATURES
-----------------------------------------------------------
- Upload lecture audio files in WAV format
- Automatically convert speech into text
- Display transcription in a clean interface
- Download the transcribed text as a file
- Offline speech recognition for privacy and reliability
- Simple and modern user interface

-----------------------------------------------------------
🛠️ TECHNOLOGIES USED
-----------------------------------------------------------
- Python 3.12
- Streamlit (web application framework)
- Vosk (offline speech recognition engine)
- HTML and CSS (via Streamlit customization)
- Git and GitHub (version control)

-----------------------------------------------------------
📂 PROJECT STRUCTURE
-----------------------------------------------------------
app.py                           # Main Streamlit web application
transcribe.py                    # Handles speech-to-text conversion
requirements.txt                 # Lists required dependencies
background.webp                  # Background image for the UI
vosk-model-small-en-us-0.15/     # Offline speech recognition model
README.txt                       # Project documentation

-----------------------------------------------------------
🚀 HOW TO RUN THE PROJECT LOCALLY
-----------------------------------------------------------
Step 1: Install Python
Ensure Python 3.12 is installed and added to your system PATH.
Check with: python --version

Step 2: Install Project Dependencies
Run the following command in your terminal:
pip install -r requirements.txt

Step 3: Download the Vosk Model
1. Visit: https://alphacephei.com/vosk/models
2. Download: vosk-model-small-en-us-0.15.zip
3. Extract the ZIP file.
4. Place the extracted folder inside the project directory.

Step 4: Run the Application
Start the app using:
streamlit run app.py

-----------------------------------------------------------
🎧 AUDIO REQUIREMENTS
-----------------------------------------------------------
- File format: .WAV
- Channel: Mono
- Quality: Clear speech, minimal background noise
- Duration: Recommended under 5 minutes for best performance

-----------------------------------------------------------
☁️ STREAMLIT CLOUD NOTE
-----------------------------------------------------------
The local version provides full speech-to-text functionality. 
Streamlit Cloud deployment is limited to demonstrating the 
UI as it does not support the native dependencies required 
for offline speech recognition engines like Vosk.

-----------------------------------------------------------
🔮 FUTURE ENHANCEMENTS
-----------------------------------------------------------
- Live microphone-based transcription
- Multi-language support
- Timestamped transcripts
- Lecture summarization

-----------------------------------------------------------
👩‍💻 AUTHOR: annliasunil
-----------------------------------------------------------
LICENSE: Developed for educational and academic purposes only.
===========================================================
