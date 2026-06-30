"""
Application configuration.

This module centralizes all application settings.
Configuration values are loaded from environment variables
or a local .env file.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    # Project
    PROJECT_NAME: str = "AI Audience Analytics Platform"
    PROJECT_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str

    # TMDB
    TMDB_API_KEY: str
    TMDB_READ_ACCESS_TOKEN: str
    TMDB_BASE_URL: str = "https://api.themoviedb.org/3"

    # OMDB
    OMDB_API_KEY: str
    OMDB_BASE_URL: str 

    # AWS
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_REGION: str = "ap-south-1"

  
    # Logging
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings object.
    """
    return Settings()


settings = get_settings()