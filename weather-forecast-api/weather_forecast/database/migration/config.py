from alembic.config import Config

from weather_forecast.settings import BASE_DIR, DATABASE_URI

alembic_cfg = Config()
alembic_cfg.set_main_option("script_location", f"{BASE_DIR}/weather_forecast/database/migration")
alembic_cfg.set_main_option("sqlalchemy.url", DATABASE_URI)
