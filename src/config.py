from pydantic import BaseSettings

class Settings(BaseSettings):
    # General
    ENVIRONMENT: str = ""
    PORT: int = 0
    VERSION: str = ""
    STATUS: str = ""

    # Google settings
    API_KEY: str = ""
    GEOCODE_URL: str = ""
    PLACES_URL: str  = ""

config = Settings()
