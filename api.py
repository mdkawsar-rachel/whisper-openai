import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import aiofiles
import transcriber2 as transcriber
import os
import uuid

app = FastAPI()

# model = whisper.load_model("tiny")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/transcribe/")
async def transcribe_audio(audio: UploadFile = File(...)):
    try:
        name = uuid.uuid4()
        out_file_path = f"files/{name}.mp3"
        async with aiofiles.open(out_file_path, 'wb') as out_file:
            content = await audio.read()  # async read
            await out_file.write(content)
        # return {"Result": "OK"}

        text = await transcriber.transcribe(out_file_path)
        os.remove(out_file_path)
        return {"Result": text}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
