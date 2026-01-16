import httpx
from app.config import Settings

settings = Settings()

BASE_URL = settings.openweather_base_url

async def get_weather(city: str):
    params = {
        "q": city,
        "appid": settings.openweather_api_key,
        "units": "metric"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API call failed: {response.status_code}")