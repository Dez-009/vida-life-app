from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Vida Life Coach API is running!"}


@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")
    return {"response": f"You said: {user_message}"}