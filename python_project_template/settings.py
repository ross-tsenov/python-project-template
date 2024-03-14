from typing import Literal

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Global application settings loaded from the .env file."""

    env: Literal["dev", "prod"] = "dev"
    other_var: str = "other"


load_dotenv(override=True)
settings = Settings()
