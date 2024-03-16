from src.settings import Environment, settings


def test_settings() -> None:
    assert settings.env in [Environment.DEV, Environment.PROD]
