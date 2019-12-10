from celery import Celery

from integration_open_weather.settings import APPLICATION, CELERY
from integration_open_weather.tasks import task_registry

app = Celery(APPLICATION, tasks=task_registry, config_source=CELERY)
