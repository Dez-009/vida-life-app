# API Reference

All endpoints are served from the FastAPI backend running on `http://127.0.0.1:8000` by default.

## GET /
Returns a simple status message confirming the server is running.

### Example Response
```json
{"message": "Vida Life Coach API is running!"}
```

## POST /chat
Send a user message and receive an AI-generated response.

### Request Body
```json
{"message": "Hello"}
```

### Example Response
```json
{"response": "You said: Hello"}
```

