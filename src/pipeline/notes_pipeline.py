"""
Notes generation pipeline for the AI Study Assistant.

This pipeline is responsible for generating study notes
from a user-provided topic.
"""

import sys

from src.chains import notes_chain
from src.exception import AIStudyAssistantException
from src.logger import get_logger
from src.utils import clean_text, validate_topic

logger = get_logger(__name__)


class NotesPipeline:
    """
    Pipeline responsible for generating study notes.
    """

    def __init__(self) -> None:
        self.chain = notes_chain

    def generate_notes(self, topic: str) -> str:
        """
        Generate study notes for a given topic.

        Parameters
        ----------
        topic : str
            User-provided study topic.

        Returns
        -------
        str
            Generated study notes.

        Raises
        ------
        ValueError
            If the topic is invalid.
        AIStudyAssistantException
            If note generation fails.
        """

        try:
            logger.info("Received topic: %s", topic)

            if not validate_topic(topic):
                logger.warning("Invalid topic entered.")
                raise ValueError(
                    "Please enter a valid study topic."
                )

            logger.info("Generating notes...")

            notes = self.chain.invoke(
                {
                    "topic": topic
                }
            )

            notes = clean_text(notes)

            logger.info("Notes generated successfully.")

            return notes

        except Exception as e:
            logger.exception("Failed to generate notes.")
            raise AIStudyAssistantException(e, sys)


# --------------------------------------------------------
# Singleton Pipeline
# --------------------------------------------------------

notes_pipeline = NotesPipeline()