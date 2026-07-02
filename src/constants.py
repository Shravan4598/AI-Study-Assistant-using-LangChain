"""
Project-wide constants for the AI Study Assistant.

This module stores application metadata, directory paths,
logging paths, and default configuration values.
"""

from pathlib import Path

# ==========================================================
# Project Information
# ==========================================================

PROJECT_NAME: str = "AI Study Assistant"
PROJECT_VERSION: str = "1.0.0"

# ==========================================================
# Base Directories
# ==========================================================

# AI_Study_Assistant/
BASE_DIR: Path = Path(__file__).resolve().parent.parent

SRC_DIR: Path = BASE_DIR / "src"
CONFIG_DIR: Path = BASE_DIR / "config"
LOG_DIR: Path = BASE_DIR / "logs"
ASSETS_DIR: Path = BASE_DIR / "assets"
TEMPLATES_DIR: Path = BASE_DIR / "templates"

# ==========================================================
# Files
# ==========================================================

ENV_FILE: Path = BASE_DIR / ".env"

LOG_FILE: Path = LOG_DIR / "app.log"

README_FILE: Path = BASE_DIR / "README.md"

# ==========================================================
# Model Defaults
# ==========================================================

DEFAULT_MODEL_NAME: str = "gemini-2.5-flash"

DEFAULT_TEMPERATURE: float = 0.3

DEFAULT_MAX_OUTPUT_TOKENS: int = 2048

# ==========================================================
# UI Defaults
# ==========================================================

PAGE_TITLE: str = "📚 AI Study Assistant"

PAGE_ICON: str = "📖"

LAYOUT: str = "wide"

SIDEBAR_TITLE: str = "About"

# ==========================================================
# Feedback Labels
# ==========================================================

POSITIVE: str = "positive"

NEGATIVE: str = "negative"

NEUTRAL: str = "neutral"

VALID_SENTIMENTS = (
    POSITIVE,
    NEGATIVE,
    NEUTRAL,
)

# ==========================================================
# Generation Settings
# ==========================================================

NUMBER_OF_QUESTIONS: int = 5

MIN_FEEDBACK_LENGTH: int = 3

MAX_TOPIC_LENGTH: int = 200

# ==========================================================
# Logging
# ==========================================================

LOG_FORMAT: str = (
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

LOG_LEVEL: str = "INFO"

# ==========================================================
# Application Messages
# ==========================================================

APP_START_MESSAGE: str = "AI Study Assistant started successfully."

NOTES_SUCCESS: str = "Notes generated successfully."

QUESTIONS_SUCCESS: str = "Questions generated successfully."

ANSWERS_SUCCESS: str = "Answers generated successfully."

FEEDBACK_SUCCESS: str = "Feedback submitted successfully."

SENTIMENT_SUCCESS: str = "Sentiment detected successfully."