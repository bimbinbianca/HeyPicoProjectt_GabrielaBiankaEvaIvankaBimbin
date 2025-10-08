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
```bash
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
```

## .env Configuration
Create a .env file inside the backend folder:
```bash
GOOGLE_API_KEY=your_google_maps_api_key
OPENWEBUI_URL=http://localhost:11434/api/generate
OPENWEBUI_MODEL=mistral
```

## Running the App
1.    Start Ollama & Open-WebUI:
```bash
ollama serve
``` 
2.    Run FastAPI
```bash
uvicorn main:app --reload
```
3.    Test Endpoint
```arduino
http://127.0.0.1:8000/search?query=restaurant+jakarta
```

## Example Output
```json
{
  "prompt": "Find coffee shops near Jakarta",
  "llm_result": "coffee shop jakarta",
  "places_results": [
    {
      "name": "Tanamera Coffee",
      "address": "Jl. Thamrin No. 11, Jakarta",
      "location": {"lat": -6.194, "lng": 106.823},
      "embed_url": "https://www.google.com/maps/embed/v1/place?key=...&q=Tanamera+Coffee",
      "maps_link": "https://www.google.com/maps/search/?api=1&query=Tanamera+Coffee"
    }
  ]
}
```
## Pict the Output

