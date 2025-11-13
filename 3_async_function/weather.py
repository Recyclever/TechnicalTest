# import httpx <- uncomment this
from typing import List

from pydantic import BaseModel


class Weather(BaseModel):
    city: str
    temperature: float
    conditions: str

async def fetch_weather_for_cities(cities: List[str], api_key: str) -> List[Weather]:
    """
    Fetch weather data for multiple cities concurrently.

    API endpoint: https://api.weather.com/current?city={city}&key={api_key}

    Returns list of Weather objects in the same order as input cities.
    If a city fails, include None in that position.
    """
    # Your implementation here
    pass
