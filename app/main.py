from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, services
from app.database import get_db

app = FastAPI()

@app.get("/weather", response_model = schemas.WeatherResponse)
async def get_weather_cache(city: str, db: Session = Depends(get_db)):
    city = city.title()
    cached = crud.get_cached_weather(db=db, city=city)
    if cached:
        weather_data = cached.weather_data #a dict from openweathermap

        return schemas.WeatherResponse(
            city=weather_data["name"],
            temp=weather_data["main"]["temp"],
            feels_like=weather_data["main"]["feels_like"],
            temp_min=weather_data["main"]["temp_min"],
            temp_max=weather_data["main"]["temp_max"],
            humidity=weather_data["main"]["humidity"],
            description=weather_data["weather"][0]["description"],
            is_cached=True,
            timestamp=cached.updated_at
        )
    
    try:
        api_response = await services.get_weather(city)
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Weather service unavailable: {str(e)}")
    
    try:
        parsed = schemas.OpenWeatherMapResponse(**api_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invalid response from weather service: {str(e)}")

    saved = crud.save_weather(db=db, city=city, weather_data=api_response)

    return schemas.WeatherResponse(
        city=parsed.name,
        temp=parsed.main.temp,
        feels_like=parsed.main.feels_like,
        temp_min=parsed.main.temp_min,
        temp_max=parsed.main.temp_max,
        humidity=parsed.main.humidity,
        description=parsed.weather[0].description,
        is_cached=False,
        timestamp=saved.updated_at
    )