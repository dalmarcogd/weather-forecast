from celery.app.registry import TaskRegistry

from integration_open_weather.tasks.open_weather_forecast import OpenWeatherForecastTask

task_registry = TaskRegistry()
task_registry.register(OpenWeatherForecastTask)
