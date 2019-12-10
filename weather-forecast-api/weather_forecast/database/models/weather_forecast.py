from enum import Enum
from typing import Dict

from sqlalchemy import Column, JSON, Enum as EnumSqlAlchemy

from weather_forecast.database.models.base import BaseModel


class WeatherForecastStatus(str, Enum):
    process = "process"
    error = "error"
    done = "done"


class WeatherForecast(BaseModel):
    __tablename__ = "weather-forecast"

    status = Column(
        EnumSqlAlchemy(WeatherForecastStatus),
        nullable=False,
        default=WeatherForecastStatus.process,
    )
    params = Column(JSON, nullable=False)
    result = Column(JSON, nullable=True)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "status": self.status,
            "result": self.result,
        }
