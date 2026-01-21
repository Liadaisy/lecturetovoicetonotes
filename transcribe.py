import json
import wave
from vosk import Model, KaldiRecognizer

MODEL_PATH = "vosk-model-small-en-us-0.15"

def transcribe_audio(audio_path):
    wf = wave.open(audio_path, "rb")

    if wf.getnchannels() != 1:
        raise ValueError("Audio must be mono WAV")

    model = Model(MODEL_PATH)
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(False)

    text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text += result.get("text", "") + " "

    final_result = json.loads(rec.FinalResult())
    text += final_result.get("text", "")

    return text.strip()
