from typing import Dict

from integration_open_weather.settings import OPEN_WEATHER_APP_ID, OPEN_WEATHER_URL
from integration_open_weather.utils.miscellaneous import requests_retry


def get_weather_forecast_by_city_name(city_name: str) -> Dict:
    response = requests_retry().get(
        f"{OPEN_WEATHER_URL}/weather?q={city_name}&APPID={OPEN_WEATHER_APP_ID}"
    )
    response.raise_for_status()
    return response.json()


def get_weather_forecast_geographic_coordinates(latitude: int, longitude: int) -> Dict:
    response = requests_retry().get(
        f"{OPEN_WEATHER_URL}/weather?lat={latitude}&lon={longitude}&APPID={OPEN_WEATHER_APP_ID}"
    )
    response.raise_for_status()
    return response.json()
