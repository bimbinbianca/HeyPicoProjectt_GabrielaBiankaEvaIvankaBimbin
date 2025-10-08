from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv
import httpx
import re

load_dotenv()  # load .env file

app = FastAPI()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENWEBUI_URL = os.getenv("OPENWEBUI_URL")
OPENWEBUI_MODEL = os.getenv("OPENWEBUI_MODEL")


@app.get("/search")
async def search_place(prompt: str):
    if not GOOGLE_API_KEY:
        raise HTTPException(status_code=500, detail="Google API Key not found")
    if not OPENWEBUI_URL or not OPENWEBUI_MODEL:
        raise HTTPException(status_code=500, detail="Open-WebUI URL or Model not configured")

    # 1️⃣ Request ke LLM secara async
    llm_output = ""
    try:
        llm_payload = {
            "model": OPENWEBUI_MODEL,
            "prompt": prompt,
            "stream": True
        }

        async with httpx.AsyncClient(timeout=30) as client:
            async with client.stream("POST", OPENWEBUI_URL, json=llm_payload) as llm_response:
                llm_response.raise_for_status()
                async for line in llm_response.aiter_lines():
                    if not line.strip():
                        continue
                    try:
                        data = llm_response.json()
                    except Exception:
                        import json
                        data = json.loads(line)
                    if "response" in data:
                        llm_output += data["response"]

        print("✅ LLM Output:", llm_output)


    except Exception as e:
        llm_output = f"LLM error: {str(e)}"

    # 2️⃣ Request ke Google Places API secara async
    places_results = []
    try:
        names = re.findall(r"\d+\.\s*([A-Za-z\s&]+)", llm_output)
        if names:
            search_query = names[0] + " Jakarta"
        else:
            search_query = prompt
        #search_query = llm_output if llm_output and "LLM error" not in llm_output else "restaurant"
        params = {"query": search_query, "key": GOOGLE_API_KEY}
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

        for place in data.get("results", []):
            name = place.get("name")
            address = place.get("formatted_address")
            places_results.append({
                "name": name,
                "address": address,
                "location": place.get("geometry", {}).get("location"),
                "embed_url": f"https://www.google.com/maps/embed/v1/place?key={GOOGLE_API_KEY}&q={name}, {address}",
                "maps_link": f"https://www.google.com/maps/search/?api=1&query={name}"
            })
    except Exception as e:
        places_results = [{"error": f"Google Places API error: {str(e)}"}]

    return {
        "prompt": prompt,
        "llm_result": llm_output,
        "places_results": places_results
    }
