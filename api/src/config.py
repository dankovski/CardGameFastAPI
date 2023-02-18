from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    DATABASE_PORT: int
    EMAIL_LOGIN: str
    EMAIL_PASSWORD: str
    SECRET_KEY: str

    class Config:
        env_file = '../../.env'


@lru_cache()
def get_settings():
    return Settings()
