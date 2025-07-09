import os
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

from auth.auth_utils import get_current_user, TokenData

# Load environment variables and configure OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY", "")
client = None
try:
    if api_key and api_key != "your_openai_api_key_here":
        client = OpenAI(api_key=api_key)
        print(f"OpenAI client initialized with API key: {api_key[:5]}...{api_key[-4:]}")
except Exception as e:
    print(f"Error initializing OpenAI client: {str(e)}")

router = APIRouter(prefix="/agent", tags=["agent"])

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_with_agent(
    payload: ChatRequest,
    current_user: TokenData = Depends(get_current_user)
):
    """Generate a coaching reply via GPT-4."""
    
    # For testing or when API key is not available, return a demo response
    if client is None:
        return {
            "response": "I'm your Vida Life Coach. I'd normally respond with AI-generated advice, but I'm currently in demo mode because the OpenAI API key is not properly configured. Please ask your question again when the API key is set up!"
        }
    
    try:
        # Try using the OpenAI API
        print(f"Sending request to OpenAI with message: {payload.message[:30]}...")
        result = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Fallback to a more widely available model
            messages=[
                {
                    "role": "system",
                    "content": "You are a supportive, insightful life coach that helps users think clearly and move forward with confidence.",
                },
                {"role": "user", "content": payload.message},
            ],
        )
        content = result.choices[0].message.content.strip()
        return {"response": content}
    except Exception as e:
        # Provide a helpful response in case of API errors
        error_detail = f"AI request failed: {str(e)}"
        print(f"OpenAI API error: {error_detail}")
        
        # Return a friendly message to the user instead of an error
        return {
            "response": "I apologize, but I'm having trouble connecting to my coaching knowledge base right now. Please try again in a few moments. In the meantime, remember that taking deep breaths and focusing on one thing at a time can help with most stressful situations."
        }
