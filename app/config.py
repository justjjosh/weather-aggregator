from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    #database
    postgres_user: str
    postgres_password: str
    postgres_db: str
    database_url: str
    
    #openweather api
    openweather_api_key: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
