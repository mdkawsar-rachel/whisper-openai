import whisper

model = whisper.load_model("base")

async def transcribe(path: str):
    result = model.transcribe(path, fp16=False)
    return result["text"]
