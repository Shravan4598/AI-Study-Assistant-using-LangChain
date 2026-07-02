"""
LangChain chains for the AI Study Assistant.

This module creates all reusable LangChain chains used by the
application.
"""

import sys

from langchain_core.runnables import (
    RunnableBranch,
    RunnableLambda,
    RunnableParallel,
)

from src.exception import AIStudyAssistantException
from src.llm import llm
from src.logger import get_logger
from src.parser import (
    sentiment_parser,
    text_parser,
    get_sentiment_format_instructions,
)
from src.prompt import (
    ANSWER_PROMPT,
    NEGATIVE_RESPONSE_PROMPT,
    NEUTRAL_RESPONSE_PROMPT,
    NOTES_PROMPT,
    POSITIVE_RESPONSE_PROMPT,
    QUESTION_PROMPT,
    SENTIMENT_PROMPT,
)

logger = get_logger(__name__)


class StudyChains:
    """
    Collection of reusable LangChain chains.
    """

    def __init__(self) -> None:
        self.model = llm

    # ==========================================================
    # Notes Generation Chain
    # ==========================================================

    def notes_chain(self):
        """
        Generate study notes.
        """
        return NOTES_PROMPT | self.model | text_parser

    # ==========================================================
    # Question Generation Chain
    # ==========================================================

    def question_chain(self):
        """
        Generate five questions from notes.
        """
        return QUESTION_PROMPT | self.model | text_parser

    # ==========================================================
    # Answer Generation Chain
    # ==========================================================

    def answer_chain(self):
        """
        Generate answers from notes.
        """
        return ANSWER_PROMPT | self.model | text_parser

    # ==========================================================
    # Parallel Chain
    # ==========================================================

    def parallel_chain(self):
        """
        Run question and answer generation in parallel.
        """

        return RunnableParallel(
            {
                "questions": self.question_chain(),
                "answers": self.answer_chain(),
            }
        )

    # ==========================================================
    # Sentiment Chain
    # ==========================================================

    def sentiment_chain(self):
        """
        Classify user feedback.
        """

        prompt = SENTIMENT_PROMPT.partial(
            format_instructions=get_sentiment_format_instructions()
        )

        return prompt | self.model | sentiment_parser

    # ==========================================================
    # Conditional Branch
    # ==========================================================

    def conditional_chain(self):
        """
        Create conditional response chain.
        """

        return RunnableBranch(

            (
                lambda x: x["sentiment"] == "positive",
                POSITIVE_RESPONSE_PROMPT
                | self.model
                | text_parser,
            ),

            (
                lambda x: x["sentiment"] == "negative",
                NEGATIVE_RESPONSE_PROMPT
                | self.model
                | text_parser,
            ),

            (
                lambda x: x["sentiment"] == "neutral",
                NEUTRAL_RESPONSE_PROMPT
                | self.model
                | text_parser,
            ),

            RunnableLambda(
                lambda _: "Unable to determine sentiment."
            ),
        )


study_chains = StudyChains()

notes_chain = study_chains.notes_chain()

parallel_chain = study_chains.parallel_chain()

sentiment_chain = study_chains.sentiment_chain()

conditional_chain = study_chains.conditional_chain()