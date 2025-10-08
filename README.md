# HeyPico.ai Technical Test-Local LLM + Google Maps Integration

## Project Overview
This project demonstrates how to integrate a local LLM model with the Google Maps API to provide place recommendations (e.g., restaurants, cafes, tourist spots) based on user prompts. The system receives a text prompt from the user, processes it through a local LLM (via Ollama + Open-WebUI), and then queries the Google Places API to return real, map-based results that can be viewed via embedded Google Maps or links.

## Tech Stack
- Backend: FastAPI(Python)
- LLM Runtime: Ollama (Local)
- Model Used: Mistral (can be replaced with any supported LLM)
- External API: Google Maps Platform(Places API)
- Environment: Local setup with .env configuration
