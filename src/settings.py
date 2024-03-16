from enum import StrEnum

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Environment(StrEnum):
    DEV = "dev"
    PROD = "prod"


class Settings(BaseSettings):
    """Global application settings loaded from the .env file."""

    env: Environment = Environment.DEV
    other_var: str = "other"


load_dotenv(override=True)
settings = Settings()
