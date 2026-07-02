"""
Conditional response pipeline for the AI Study Assistant.

This pipeline generates an appropriate response based on
the detected sentiment using LangChain's RunnableBranch.
"""

import sys

from src.chains import conditional_chain
from src.exception import AIStudyAssistantException
from src.logger import get_logger
from src.utils import clean_text, validate_feedback

logger = get_logger(__name__)


class ConditionalPipeline:
    """
    Pipeline responsible for generating AI responses
    based on user sentiment.
    """

    def __init__(self) -> None:
        self.chain = conditional_chain

    def generate_response(
        self,
        feedback: str,
        sentiment: str,
    ) -> str:
        """
        Generate an AI response based on the detected sentiment.

        Parameters
        ----------
        feedback : str
            Original user feedback.

        sentiment : str
            Detected sentiment.
            (positive / negative / neutral)

        Returns
        -------
        str
            AI-generated response.
        """

        try:

            logger.info(
                "Generating response for sentiment: %s",
                sentiment,
            )

            if not validate_feedback(feedback):
                raise ValueError(
                    "Invalid feedback."
                )

            feedback = clean_text(feedback)

            response = self.chain.invoke(
                {
                    "feedback": feedback,
                    "sentiment": sentiment.lower(),
                }
            )

            response = clean_text(response)

            logger.info(
                "Conditional response generated successfully."
            )

            return response

        except Exception as e:
            logger.exception(
                "Conditional response generation failed."
            )

            raise AIStudyAssistantException(e, sys)


# ---------------------------------------------------------
# Singleton Instance
# ---------------------------------------------------------

conditional_pipeline = ConditionalPipeline()