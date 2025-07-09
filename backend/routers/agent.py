import os
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

from auth.auth_utils import get_current_user, TokenData

# Load environment variables and configure OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter(prefix="/agent", tags=["agent"])

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_with_agent(
    payload: ChatRequest,
    current_user: TokenData = Depends(get_current_user)
):
    """Generate a coaching reply via GPT-4."""
    if not client.api_key:
        raise HTTPException(status_code=500, detail="AI service unavailable")
    try:
        result = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a supportive, insightful life coach that helps users think clearly and move forward with confidence.",
                },
                {"role": "user", "content": payload.message},
            ],
        )
        # New OpenAI SDK returns objects, not dictionaries
        content = result.choices[0].message.content.strip()
        return {"response": content}
    except Exception as e:
        # The modern OpenAI SDK uses standard exceptions
        raise HTTPException(status_code=503, detail="AI request failed") from e
