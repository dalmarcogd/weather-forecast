from typing import Dict

from celery.task import Task

from weather_forecast.database import queries
from weather_forecast.database.models.weather_forecast import WeatherForecastStatus


class ReceiveWeatherForecastTask(Task):
    name = "receive-weather-forecast"
    ignore_result = True

    def run(self, result: Dict) -> Dict:
        return queries.update_weather_forecast(
            {**result, "id": result["weatherForecastId"]}, WeatherForecastStatus.done
        )
