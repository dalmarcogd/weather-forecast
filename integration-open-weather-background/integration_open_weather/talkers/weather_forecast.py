from typing import Dict

from celery import signature


def send_weather_forecast(weather_forecast: Dict):
    signature(
        "receive-weather-forecast", args=[weather_forecast], queue="weather-forecast"
    ).apply_async()


def send_weather_forecast_failure(params: Dict):
    signature(
        "receive-weather-forecast-failure", args=[params], queue="weather-forecast"
    ).apply_async()
