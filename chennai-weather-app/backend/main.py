from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(title="Chennai Weather API")

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
CHENNAI_LATITUDE = 13.0827
CHENNAI_LONGITUDE = 80.2707


@app.get("/api/health")
async def health():
    return {"status": "ok"}


@app.get("/api/weather")
async def get_chennai_weather():
    params = {
        "latitude": CHENNAI_LATITUDE,
        "longitude": CHENNAI_LONGITUDE,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "Asia/Kolkata",
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(OPEN_METEO_URL, params=params)
            response.raise_for_status()
            data = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise HTTPException(
            status_code=502,
            detail="Weather provider is temporarily unavailable",
        ) from exc

    current = data.get("current", {})
    try:
        return {
            "city": "Chennai",
            "temperature_c": current["temperature_2m"],
            "humidity_percent": current["relative_humidity_2m"],
            "wind_speed_kmh": current["wind_speed_10m"],
            "time": current["time"],
        }
    except KeyError as exc:
        raise HTTPException(
            status_code=502,
            detail="Unexpected response from weather provider",
        ) from exc
