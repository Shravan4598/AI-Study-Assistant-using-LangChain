"""
Parallel pipeline for the AI Study Assistant.

This pipeline generates interview/exam questions and
their answers simultaneously using LangChain's RunnableParallel.
"""

import sys
from typing import Dict

from src.chains import parallel_chain
from src.exception import AIStudyAssistantException
from src.logger import get_logger
from src.utils import clean_text

logger = get_logger(__name__)


class ParallelPipeline:
    """
    Pipeline for parallel generation of questions and answers.
    """

    def __init__(self) -> None:
        self.chain = parallel_chain

    def generate_questions_answers(
        self,
        notes: str,
    ) -> Dict[str, str]:
        """
        Generate questions and answers from study notes.

        Parameters
        ----------
        notes : str
            Generated study notes.

        Returns
        -------
        Dict[str, str]
            Dictionary containing:
            {
                "questions": "...",
                "answers": "..."
            }
        """

        try:
            logger.info("Starting parallel generation...")

            result = self.chain.invoke(
                {
                    "notes": notes
                }
            )

            questions = clean_text(result["questions"])
            answers = clean_text(result["answers"])

            logger.info("Questions generated successfully.")
            logger.info("Answers generated successfully.")
            logger.info("Parallel execution completed successfully.")

            return {
                "questions": questions,
                "answers": answers,
            }

        except Exception as e:
            logger.exception(
                "Parallel generation failed."
            )
            raise AIStudyAssistantException(e, sys)


# ---------------------------------------------------------
# Singleton Instance
# ---------------------------------------------------------

parallel_pipeline = ParallelPipeline()