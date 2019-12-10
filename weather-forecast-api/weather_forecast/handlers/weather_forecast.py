from uuid import UUID

import ujson
from fastapi import APIRouter
from starlette.responses import UJSONResponse
from starlette.status import HTTP_201_CREATED

from weather_forecast.database import queries
from weather_forecast.schemas.weather_forecast import (
    WeatherForecastInput,
    WeatherForecastOutput,
    ResultWeatherForecastOutput,
)
from weather_forecast.talkers import integration_open_weather

weather_forecast_router = APIRouter()


@weather_forecast_router.post(
    "/weather-forecasts",
    status_code=HTTP_201_CREATED,
    response_model=WeatherForecastOutput,
    response_class=UJSONResponse,
)
async def post(weather_forecast_input: WeatherForecastInput):
    weather_forecast_input_data = weather_forecast_input.dict()
    weather_forecast = queries.create_weather_forecast(weather_forecast_input_data)
    weather_forecast_input_data.setdefault("weatherForecastId", weather_forecast["id"])
    integration_open_weather.send_open_weather_forecast(weather_forecast_input_data)
    return {"id": weather_forecast["id"], "status": weather_forecast["status"]}


@weather_forecast_router.get(
    "/weather-forecasts/{weather_forecast_id}",
    response_model=ResultWeatherForecastOutput,
    response_class=UJSONResponse,
)
async def get(weather_forecast_id: UUID):
    weather_forecast = queries.get_weather_forecast(weather_forecast_id)
    return {
        "id": weather_forecast["id"],
        "status": weather_forecast["status"],
        "result": ujson.loads(weather_forecast["result"]),
    }
