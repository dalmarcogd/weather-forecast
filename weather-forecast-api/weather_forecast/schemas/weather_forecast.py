from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel, root_validator

from weather_forecast.database.models.weather_forecast import WeatherForecastStatus


class WeatherForecastInput(BaseModel):
    cityName: Optional[str]
    latitude: Optional[int]
    longitude: Optional[int]

    @root_validator
    def check_params(cls, values):
        city_name, latitude, longitude = (
            values.get("cityName"),
            values.get("latitude"),
            values.get("longitude"),
        )
        if city_name and latitude is not None and longitude is not None:
            raise ValueError(
                "Latitude and longitude should not be informed when city name exists"
            )
        if city_name is None and (not latitude or not longitude):
            raise ValueError("Latitude and longitude i required")
        return values


class WeatherForecastOutput(BaseModel):
    id: UUID


class ResultWeatherForecastOutput(BaseModel):
    id: UUID
    status: WeatherForecastStatus
    result: Optional[Dict]
