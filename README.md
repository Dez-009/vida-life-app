# Vida Life Coach

Vida Life Coach is a web-based AI life coaching platform with a chat interface. It helps users track goals and receive personalized guidance.

## Tech Stack
- **Frontend:** React (Create React App)
- **Backend:** FastAPI
- **API Integration:** OpenAI

## Getting Started

### Backend
1. `cd backend`
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies
   ```bash
   pip install -r ../requirements.txt
   ```
4. Run the development server
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend
1. `cd frontend`
2. Install packages
   ```bash
   npm install
   ```
3. Start the development server
   ```bash
   npm start
   ```

Open `http://localhost:3000` in your browser to view the app.

## Directory Structure
- `backend/` – FastAPI server
- `frontend/` – React application
- `requirements.txt` – Backend Python dependencies

## API Overview
See [docs/API.md](docs/API.md) for detailed endpoints.

