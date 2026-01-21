from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import JSON
from app.models import WeatherCache
from datetime import datetime, timedelta

def get_cached_weather(db: Session, city: str) -> models.WeatherCache:
    weather_cache = db.query(WeatherCache).filter(WeatherCache.city == city).first()

    if weather_cache is None: 
        return None
    
    if weather_cache.updated_at > datetime.now() - timedelta(minutes=10):
        return weather_cache
    else: 
        return None
    
def save_weather(db: Session, city:str, weather_data: JSON) -> models.WeatherCache:
    check_cache = db.query(WeatherCache).filter(WeatherCache.city == city).first()
    if check_cache:
        check_cache.weather_data = weather_data
        db.commit()
        db.refresh(check_cache)
        return check_cache
   
    else:
        new_entry = models.WeatherCache(
            city=city,
            weather_data=weather_data
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return new_entry
   
