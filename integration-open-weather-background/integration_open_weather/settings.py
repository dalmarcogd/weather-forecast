from decouple import config

APPLICATION = config("APPLICATION")

CELERY = {
    "CELERY_BROKER_URL": config("CELERY_BROKER_URL"),
    "CELERY_RESULT_BACKEND": config("CELERY_RESULT_BACKEND"),
    "CELERY_EAGER_PROPAGATES_EXCEPTIONS": True,
    "CELERY_TIMEZONE": "America/Sao_Paulo",
    "CELERY_ENABLE_UTC": True,
    "CELERY_SEND_EVENTS": True,
    "CELERY_TASK_SEND_SENT_EVENT": True,
    "CELERY_TASK_ACKS_LATE": True,
    "CELERYD_PREFETCH_MULTIPLIER": 1,
}

OPEN_WEATHER_URL = "http://api.openweathermap.org/data/2.5"
OPEN_WEATHER_APP_ID = "79d7e33821c140fc1344a6d645a4ef0b"
