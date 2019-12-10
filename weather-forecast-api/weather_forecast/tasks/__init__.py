from celery.app.registry import TaskRegistry

from weather_forecast.tasks.receive_weather_forecast import ReceiveWeatherForecastTask
from weather_forecast.tasks.receive_weather_forecast_failure import ReceiveWeatherForecastFailureTask

task_registry = TaskRegistry()
task_registry.register(ReceiveWeatherForecastTask)
task_registry.register(ReceiveWeatherForecastFailureTask)
