from typing import Dict

from celery import signature


def send_open_weather_forecast(params: Dict):
    signature(
        "open-weather-forecast", args=[params], queue="integration-open-weather"
    ).apply_async()
