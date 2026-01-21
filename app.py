import streamlit as st
from transcribe import transcribe_audio
import base64

# ---------- Background Image ----------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/webp;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("background.webp")

# ---------- Page Config ----------
st.set_page_config(
    page_title="Lecture Voice-to-Notes",
    page_icon="🎙️",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
    .title-text {
        font-size: 3rem;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
        margin-bottom: 0.2em;
    }
    .subtitle-text {
        font-size: 1.2rem;
        color: #e0e0e0;
        text-align: center;
        margin-bottom: 2em;
    }
    .card {
        background: rgba(255, 255, 255, 0.92);
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Sidebar ----------
with st.sidebar:
    st.header("🎧 About")
    st.write(
        "This tool converts lecture audio into text using offline speech recognition."
    )
    st.markdown("---")
    st.write("📌 Supported format: WAV")
    st.write("📌 Best for clear speech")
    st.write("📌 Offline & privacy-friendly")

# ---------- Main UI ----------
st.markdown('<div class="title-text">🎙️ Lecture Voice-to-Notes</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle-text">Convert your lecture audio into clean text instantly</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="card">', unsafe_allow_html=True)

audio_file = st.file_uploader(
    "Upload Lecture Audio (WAV only)",
    type=["wav"]
)

if audio_file:
    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())

    st.info("🔄 Transcribing audio… Please wait")

    try:
        transcript = transcribe_audio("temp.wav")

        st.subheader("📄 Transcribed Text")
        st.text_area(
            label="",
            value=transcript,
            height=320
        )

        st.download_button(
            label="⬇️ Download Transcript",
            data=transcript,
            file_name="lecture_transcript.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        right: 20px;
        font-size: 0.85rem;
        color: rgba(255, 255, 255, 0.7);
    }
    </style>

    <div class="footer">
        — annliasunil
    </div>
    """,
    unsafe_allow_html=True
)

