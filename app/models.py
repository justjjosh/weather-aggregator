from .database import Base
from sqlalchemy import Column, Integer, Text, String, JSON, Boolean, DateTime
from sqlalchemy.sql import func

class WeatherCache(Base):
    __tablename__ = "weather_cache"

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False, index=True)
    weather_data = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())