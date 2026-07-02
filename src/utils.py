"""
Utility functions for the AI Study Assistant.

This module contains reusable helper functions used across
the application.
"""

from pathlib import Path
import re
from typing import Optional

from src.logger import get_logger

logger = get_logger(__name__)


def create_directory(directory: Path) -> None:
    """
    Create a directory if it does not already exist.

    Parameters
    ----------
    directory : Path
        Directory path to create.
    """
    directory.mkdir(parents=True, exist_ok=True)
    logger.info("Directory verified: %s", directory)


def validate_topic(topic: str) -> bool:
    """
    Validate the user-entered topic.

    Parameters
    ----------
    topic : str
        Study topic entered by the user.

    Returns
    -------
    bool
        True if valid, otherwise False.
    """
    if not topic:
        return False

    topic = topic.strip()

    if len(topic) < 2:
        return False

    return True


def validate_feedback(feedback: str) -> bool:
    """
    Validate feedback entered by the user.

    Parameters
    ----------
    feedback : str
        Feedback text.

    Returns
    -------
    bool
        True if valid, otherwise False.
    """
    if not feedback:
        return False

    feedback = feedback.strip()

    if len(feedback) < 3:
        return False

    return True


def clean_text(text: Optional[str]) -> str:
    """
    Clean generated text by removing unnecessary whitespace.

    Parameters
    ----------
    text : str | None
        Raw text.

    Returns
    -------
    str
        Cleaned text.
    """
    if text is None:
        return ""

    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


def save_text(file_path: Path, content: str) -> None:
    """
    Save text content to a file.

    Parameters
    ----------
    file_path : Path
        Destination file.

    content : str
        Text to save.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    logger.info("File saved: %s", file_path)


def read_text(file_path: Path) -> str:
    """
    Read text from a file.

    Parameters
    ----------
    file_path : Path
        File path.

    Returns
    -------
    str
        File content.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def truncate_text(text: str, max_length: int = 200) -> str:
    """
    Truncate text to the specified length.

    Parameters
    ----------
    text : str
        Input text.

    max_length : int
        Maximum length.

    Returns
    -------
    str
        Truncated text.
    """
    if len(text) <= max_length:
        return text

    return text[:max_length].rstrip() + "..."


def format_questions(questions: str) -> list[str]:
    """
    Convert generated questions into a list.

    Parameters
    ----------
    questions : str

    Returns
    -------
    list[str]
    """
    lines = questions.split("\n")

    formatted = [
        line.strip()
        for line in lines
        if line.strip()
    ]

    return formatted


def format_answers(answers: str) -> list[str]:
    """
    Convert generated answers into a list.

    Parameters
    ----------
    answers : str

    Returns
    -------
    list[str]
    """
    lines = answers.split("\n")

    formatted = [
        line.strip()
        for line in lines
        if line.strip()
    ]

    return formatted


def print_banner() -> None:
    """
    Print a startup banner in the console.
    """
    banner = """
====================================================
            AI STUDY ASSISTANT
      LangChain + Gemini + Streamlit
====================================================
"""
    print(banner)