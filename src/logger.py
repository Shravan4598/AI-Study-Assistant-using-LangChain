"""
Centralized logging configuration for the AI Study Assistant.

This module configures logging for the entire application.
Logs are written to both the console and a log file.
"""

import logging
from logging.handlers import RotatingFileHandler

from src.constants import (
    LOG_DIR,
    LOG_FILE,
    LOG_FORMAT,
    LOG_LEVEL,
)

# Create logs directory if it doesn't exist
LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Parameters
    ----------
    name : str
        Name of the logger (usually __name__).

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

    formatter = logging.Formatter(LOG_FORMAT)

    # --------------------------------------------------------
    # File Handler
    # --------------------------------------------------------
    file_handler = RotatingFileHandler(
        filename=LOG_FILE,
        maxBytes=5 * 1024 * 1024,   # 5 MB
        backupCount=3,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    # --------------------------------------------------------
    # Console Handler
    # --------------------------------------------------------
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # --------------------------------------------------------
    # Add handlers
    # --------------------------------------------------------
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False

    return logger