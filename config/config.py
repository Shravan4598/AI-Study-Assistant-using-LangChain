"""
Configuration module for the AI Study Assistant.

This module loads all configuration values from the .env file
and makes them available throughout the application.
"""

from dataclasses import dataclass
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@dataclass(frozen=True)
class Settings:
    """
    Stores application configuration.
    """

    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "gemini-2.5-flash")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.3"))
    MAX_OUTPUT_TOKENS: int = int(os.getenv("MAX_OUTPUT_TOKENS", "2048"))


settings = Settings()


def validate_config() -> None:
    """
    Validate required environment variables.

    Raises:
        ValueError: If GOOGLE_API_KEY is missing.
    """
    if not settings.GOOGLE_API_KEY:
        raise ValueError(
            "GOOGLE_API_KEY not found. Please add it to your .env file."
        )