# Import text generation functions
from app.text_generator import generate_text
from fastapi import FastAPI

app = FastAPI()

@app.get("/text-generator")
async def root(prompt: str):
    message = generate_text(prompt)

    return {"message": message}