from typing import Dict, List

from celery.task import Task

from integration_open_weather.exceptions.weather_forecast import WeatherForecastRequiredParams
from integration_open_weather.talkers import open_weather, weather_forecast


class OpenWeatherForecastTask(Task):
    name = "open-weather-forecast"
    ignore_result = True

    def run(self, params: Dict) -> Dict:
        if city_name := params.get("cityName"):
            weather_forecast_data = open_weather.get_weather_forecast_by_city_name(
                city_name
            )
        elif (latitude := params.get("latitude")) and (
            longitude := params.get("longitude")
        ):
            weather_forecast_data = open_weather.get_weather_forecast_geographic_coordinates(
                latitude, longitude
            )
        else:
            raise WeatherForecastRequiredParams()

        weather_forecast_data.setdefault(
            "weatherForecastId", params["weatherForecastId"]
        )

        return weather_forecast_data

    def on_success(self, retval: Dict, task_id, args: List[Dict], kwargs):
        weather_forecast.send_weather_forecast(retval)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        weather_forecast.send_weather_forecast_failure(args[0])
