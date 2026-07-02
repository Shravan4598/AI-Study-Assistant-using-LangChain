"""
Sentiment analysis pipeline for the AI Study Assistant.

This pipeline analyzes user feedback and classifies it as
positive, negative, or neutral.
"""

import sys

from src.chains import sentiment_chain
from src.exception import AIStudyAssistantException
from src.logger import get_logger
from src.utils import clean_text, validate_feedback

logger = get_logger(__name__)


class SentimentPipeline:
    """
    Pipeline responsible for sentiment analysis.
    """

    def __init__(self) -> None:
        self.chain = sentiment_chain

    def analyze_sentiment(self, feedback: str) -> str:
        """
        Analyze the sentiment of user feedback.

        Parameters
        ----------
        feedback : str
            User feedback.

        Returns
        -------
        str
            One of:
            - positive
            - negative
            - neutral

        Raises
        ------
        ValueError
            If feedback is invalid.

        AIStudyAssistantException
            If sentiment analysis fails.
        """

        try:
            logger.info("Received user feedback.")

            if not validate_feedback(feedback):
                logger.warning("Invalid feedback received.")

                raise ValueError(
                    "Please enter valid feedback before submitting."
                )

            feedback = clean_text(feedback)

            logger.info("Analyzing sentiment...")

            result = self.chain.invoke(
                {
                    "feedback": feedback
                }
            )

            sentiment = result.sentiment.lower()

            logger.info(
                "Detected sentiment: %s",
                sentiment,
            )

            return sentiment

        except Exception as e:
            logger.exception(
                "Sentiment analysis failed."
            )

            raise AIStudyAssistantException(e, sys)


# ---------------------------------------------------------
# Singleton Instance
# ---------------------------------------------------------

sentiment_pipeline = SentimentPipeline()