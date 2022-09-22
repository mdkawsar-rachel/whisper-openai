import whisper

model = whisper.load_model("tiny")
result = model.transcribe("audio_demo.mp3")
print(result["text"])
