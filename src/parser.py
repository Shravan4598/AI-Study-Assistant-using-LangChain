"""
Output parsers for the AI Study Assistant.

This module defines all output parsers used throughout the
application, including structured sentiment parsing.
"""

from typing import Literal

from langchain_core.output_parsers import (
    PydanticOutputParser,
    StrOutputParser,
)
from pydantic import BaseModel, Field

# ==========================================================
# String Output Parser
# ==========================================================

text_parser = StrOutputParser()


# ==========================================================
# Pydantic Model for Sentiment Analysis
# ==========================================================

class FeedbackSentiment(BaseModel):
    """
    Represents the sentiment classification of user feedback.
    """

    sentiment: Literal["positive", "negative", "neutral"] = Field(
        ...,
        description="Sentiment of the feedback."
    )


# ==========================================================
# Pydantic Output Parser
# ==========================================================

sentiment_parser = PydanticOutputParser(
    pydantic_object=FeedbackSentiment
)


# ==========================================================
# Helper Function
# ==========================================================

def get_sentiment_format_instructions() -> str:
    """
    Return formatting instructions for the sentiment parser.

    Returns
    -------
    str
        Instructions for the LLM to produce valid structured output.
    """
    return sentiment_parser.get_format_instructions()