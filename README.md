# HeyPico.ai Technical Test-Local LLM + Google Maps Integration

## Project Overview
This project demonstrates how to integrate a local LLM model with the Google Maps API to provide place recommendations (e.g., restaurants, cafes, tourist spots) based on user prompts. The system receives a text prompt from the user, processes it through a local LLM (via Ollama + Open-WebUI), and then queries the Google Places API to return real, map-based results that can be viewed via embedded Google Maps or links.

## Tech Stack
- Backend: FastAPI(Python)
- LLM Runtime: Ollama (Local)
- Model Used: Mistral (can be replaced with any supported LLM)
- External API: Google Maps Platform(Places API)
- Environment: Local setup with .env configuration

## How it Works
1.  User Prompt : The user asks for a recommendation (e.g., "find sushi restaurants near Jakarta")
2.  LLM Processing : The local LLM (Mistral) interprets the user prompt.
3.  Google Maps Query : The backend uses the interpreted query to call Google Places API.
4.  Results : Return a JSON response containing:
    -  Place name
    -  Address
    -  Location
    -  Embeded Google Map URL
    -  Direct Google Maps link

## Project Structure
HeyPicoTest/
│
├── backend/
│   ├── main.py              # FastAPI app (handles LLM + Google API integration)
│   ├── .env                 # API keys and environment config
│   ├── requirements.txt     # Dependencies
│
├── ollama/                  # Local LLM setup (Mistral model)
│
└── README.md                # Project documentation

## .env Configuration
GOOGLE_API_KEY=your_google_maps_api_key
OPENWEBUI_URL=http://localhost:11434/api/generate
OPENWEBUI_MODEL=mistral



