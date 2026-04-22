from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os

from services.intent_service import classify_intent
from services.normal_chat_service import normal_chat
from services.similarity_service import similar_chat

load_dotenv()

router = APIRouter()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(req: ChatRequest):
    intent = classify_intent(client, req.message)

    if intent == "SIMILAR_REQUEST":
        reply = similar_chat(client, req.message)

    elif intent == "OUT_OF_SCOPE":
        reply = "This question is not related to the platform. I can only assist with movies, resources, purchases, and platform features."

    else:
        reply = normal_chat(client, req.message)

    return {
        "intent": intent,
        "reply": reply
    }