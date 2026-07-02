"""
LLM configuration module for the AI Study Assistant.

This module initializes and returns the Google Gemini model
using LangChain's ChatGoogleGenerativeAI.
"""

from langchain_google_genai import ChatGoogleGenerativeAI

from config.config import settings, validate_config
from src.exception import AIStudyAssistantException
from src.logger import get_logger

import sys

logger = get_logger(__name__)


class LLMProvider:
    """
    Factory class for creating and managing LLM instances.
    """

    def __init__(self) -> None:
        """
        Initialize the LLM provider.
        """
        validate_config()

    def get_llm(self) -> ChatGoogleGenerativeAI:
        """
        Create and return the Gemini LLM.

        Returns
        -------
        ChatGoogleGenerativeAI
            Configured Gemini model.
        """
        try:
            logger.info(
                "Initializing Gemini model: %s",
                settings.MODEL_NAME,
            )

            llm = ChatGoogleGenerativeAI(
                model=settings.MODEL_NAME,
                google_api_key=settings.GOOGLE_API_KEY,
                temperature=settings.TEMPERATURE,
                max_output_tokens=settings.MAX_OUTPUT_TOKENS,
            )

            logger.info("Gemini model initialized successfully.")

            return llm

        except Exception as e:
            logger.exception("Failed to initialize Gemini model.")
            raise AIStudyAssistantException(e, sys)


# ------------------------------------------------------------------
# Singleton LLM Instance
# ------------------------------------------------------------------

_llm_provider = LLMProvider()

llm = _llm_provider.get_llm()