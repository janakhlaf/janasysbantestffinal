from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(req: ChatRequest):
    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {"role": "system", "content": "You are an assistant for a platform that contains films and 3D assets. Answer clearly and simply."},
            {"role": "user", "content": req.message}
        ]
    )

    return {
        "reply": response.output_text
    }