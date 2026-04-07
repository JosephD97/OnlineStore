from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Online Store"
    debug: bool = True
    database_url: str = "postgresql://postgres:1234@localhost:5432/OnlineStore"
    cors_origins: list = [

    ]
    static_dir: str = "static"
    images_dir: str = "static/images"

    class Config:
        env_file = ".env"

settings = Settings()