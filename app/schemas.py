from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from pydantic import ConfigDict


#Schema for OpenWeatherMap API response
class Coordinates(BaseModel):
    lon: float
    lat: float

class WeatherDetail(BaseModel):
    id: int
    main: str
    description: str

class MainStats(BaseModel):
    temp: float
    temp_min: Optional[float]=None
    temp_max: Optional[float]=None
    feels_like: Optional[float]=None
    pressure: int
    humidity: int


class OpenWeatherMapResponse(BaseModel):
    coord: Coordinates
    weather: List[WeatherDetail]
    main: MainStats
    timezone: int
    name: str

class WeatherResponse(BaseModel):
    """
    Schema for weatherdata returned to users.
    Includes cached status and timestamp for transparency
    """
    city: str
    feels_like: Optional[float]=None
    temp: float
    temp_min: Optional[float]=None
    temp_max: Optional[float]=None
    humidity: int
    description: str
    is_cached: bool
    timestamp: datetime

class WeatherCacheResponse(BaseModel):
    id: int
    city: str
    weather_data: dict
    created_at: datetime
    updated_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)