from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Vida Life Coach API is running!"}