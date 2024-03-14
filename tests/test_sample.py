from python_project_template.settings import settings

def test_settings() -> None:
    assert settings.env in ["dev", "prod"]
