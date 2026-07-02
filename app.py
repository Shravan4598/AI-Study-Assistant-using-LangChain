"""
Main Streamlit application for the AI Study Assistant.
"""

import streamlit as st

from src.constants import (
    PAGE_ICON,
    PAGE_TITLE,
    LAYOUT,
    PROJECT_NAME,
)
from src.logger import get_logger
from src.pipeline.notes_pipeline import notes_pipeline
from src.pipeline.parallel_pipeline import parallel_pipeline
from src.pipeline.sentiment_pipeline import sentiment_pipeline
from src.pipeline.conditional_pipeline import conditional_pipeline

logger = get_logger(__name__)


# ==========================================================
# Streamlit Configuration
# ==========================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
)

# ==========================================================
# Session State Initialization
# ==========================================================

if "notes" not in st.session_state:
    st.session_state.notes = ""

if "questions" not in st.session_state:
    st.session_state.questions = ""

if "answers" not in st.session_state:
    st.session_state.answers = ""

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "sentiment" not in st.session_state:
    st.session_state.sentiment = ""

if "response" not in st.session_state:
    st.session_state.response = ""


# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title(" AI Study Assistant")

    st.markdown("---")

    st.markdown(
        """
### About

This AI Study Assistant uses

- LangChain
- Google Gemini
- RunnableParallel
- RunnableBranch
- Streamlit

### Features

 Generate Notes

 Generate Questions

 Generate Answers

 Sentiment Analysis

 AI Feedback Response
"""
    )

    st.markdown("---")

    st.info("Built using LangChain + Gemini")


# ==========================================================
# Main Page
# ==========================================================

st.title("📖 AI Study Assistant using LangChain")

st.write(
    "Generate notes, interview questions, answers, and receive AI feedback."
)

st.markdown("---")

topic = st.text_input(
    "Enter Study Topic",
    placeholder="Example: Machine Learning",
)

# ==========================================================
# Generate Button
# ==========================================================

if st.button("🚀 Generate Study Material", use_container_width=True):

    if topic.strip() == "":
        st.warning("Please enter a study topic.")
        st.stop()

    try:

        logger.info("Topic entered: %s", topic)

        with st.spinner("Generating Notes..."):

            notes = notes_pipeline.generate_notes(topic)

            st.session_state.notes = notes

        with st.spinner("Generating Questions & Answers..."):

            result = parallel_pipeline.generate_questions_answers(
                notes
            )

            st.session_state.questions = result["questions"]

            st.session_state.answers = result["answers"]

        st.success("Study material generated successfully!")

    except Exception as e:

        logger.exception("Generation failed.")

        st.error(str(e))

# ==========================================================
# Display Notes
# ==========================================================

if st.session_state.notes:

    st.header("📝 Generated Notes")

    st.markdown(st.session_state.notes)

# ==========================================================
# Questions
# ==========================================================

if st.session_state.questions:

    st.header("❓ Interview / Exam Questions")

    st.markdown(st.session_state.questions)

# ==========================================================
# Answers
# ==========================================================

if st.session_state.answers:

    st.header("✅ Answers")

    st.markdown(st.session_state.answers)

# ==========================================================
# Feedback
# ==========================================================

if st.session_state.notes:

    st.markdown("---")

    st.header("💬 Feedback")

    feedback = st.text_area(
        "How were the generated notes?",
        placeholder="Example: The notes were very helpful.",
    )

    if st.button("Submit Feedback"):

        if feedback.strip() == "":
            st.warning("Please enter feedback.")
            st.stop()

        try:

            st.session_state.feedback = feedback

            with st.spinner("Analyzing feedback..."):

                sentiment = (
                    sentiment_pipeline.analyze_sentiment(
                        feedback
                    )
                )

                st.session_state.sentiment = sentiment

            with st.spinner("Generating response..."):

                response = (
                    conditional_pipeline.generate_response(
                        feedback,
                        sentiment,
                    )
                )

                st.session_state.response = response

            st.success("Feedback processed successfully!")

        except Exception as e:

            logger.exception("Feedback processing failed.")

            st.error(str(e))

# ==========================================================
# Sentiment
# ==========================================================

if st.session_state.sentiment:

    st.header("📊 Sentiment")

    st.success(st.session_state.sentiment.capitalize())

# ==========================================================
# AI Response
# ==========================================================

if st.session_state.response:

    st.header("🤖 AI Response")

    st.info(st.session_state.response)