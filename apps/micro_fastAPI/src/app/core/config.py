from pydantic_settings import BaseSettings, SettingsConfigDict
# В отличие от обычного BaseModel,
# этот класс умеет сам искать значения полей в системных переменных
# окружения ОС и .env файлах.

class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",

    )

settings = Settings()