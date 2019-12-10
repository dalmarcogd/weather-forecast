from typing import Dict

from celery.task import Task

from weather_forecast.database import queries
from weather_forecast.database.models.weather_forecast import WeatherForecastStatus


class ReceiveWeatherForecastFailureTask(Task):
    name = "receive-weather-forecast-failure"
    ignore_result = True

    def run(self, result: Dict) -> Dict:
        return queries.update_weather_forecast(
            {"id": result["weatherForecastId"], **result}, WeatherForecastStatus.error
        )
