import os
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import openai
from dotenv import load_dotenv

from backend.auth.auth_utils import get_current_user, TokenData

# Load environment variables and configure OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter(prefix="/agent", tags=["agent"])

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_with_agent(
    payload: ChatRequest,
    current_user: TokenData = Depends(get_current_user)
):
    """Generate a coaching reply via GPT-4.1."""
    if not openai.api_key:
        raise HTTPException(status_code=500, detail="AI service unavailable")
    try:
        result = openai.ChatCompletion.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": "You are a supportive, insightful life coach that helps users think clearly and move forward with confidence.",
                },
                {"role": "user", "content": payload.message},
            ],
        )
        content = result["choices"][0]["message"]["content"].strip()
        return {"response": content}
    except openai.error.OpenAIError as e:
        raise HTTPException(status_code=503, detail="AI request failed") from e
