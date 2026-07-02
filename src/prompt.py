"""
Prompt templates for the AI Study Assistant.

This module stores all prompt templates used throughout the
application. Keeping prompts in one place makes them easier
to maintain and modify.
"""

from langchain_core.prompts import PromptTemplate

# ==========================================================
# Notes Generation Prompt
# ==========================================================

NOTES_PROMPT = PromptTemplate(
    template="""
You are an expert educator.

Generate comprehensive and easy-to-understand study notes on the following topic.

Topic:
{topic}

The notes MUST contain the following sections:

1. Introduction
2. Explanation
3. Important Concepts
4. Examples
5. Advantages
6. Disadvantages
7. Applications
8. Summary

Write in a student-friendly language using proper headings and bullet points wherever appropriate.
""",
    input_variables=["topic"],
)

# ==========================================================
# Question Generation Prompt
# ==========================================================

QUESTION_PROMPT = PromptTemplate(
    template="""
You are an experienced examiner.

Based on the following study notes, generate EXACTLY 5 interview/exam questions.

Notes:
{notes}

Instructions:
- Generate exactly 5 questions.
- Questions should test conceptual understanding.
- Number each question.
- Do not include answers.
""",
    input_variables=["notes"],
)

# ==========================================================
# Answer Generation Prompt
# ==========================================================

ANSWER_PROMPT = PromptTemplate(
    template="""
You are an expert teacher.

Read the following study notes carefully.

Notes:
{notes}

Generate concise answers for the most important five concepts discussed in the notes.

Instructions:
- Generate exactly 5 answers.
- Number each answer.
- Keep answers short and easy to understand.
""",
    input_variables=["notes"],
)

# ==========================================================
# Sentiment Analysis Prompt
# ==========================================================

SENTIMENT_PROMPT = PromptTemplate(
    template="""
You are a sentiment analysis model.

Analyze the following feedback.

Feedback:
{feedback}

{format_instructions}

Return ONLY the JSON output.
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": "{format_instructions}"
    },
)
# ==========================================================
# Positive Response Prompt
# ==========================================================

POSITIVE_RESPONSE_PROMPT = PromptTemplate(
    template="""
You are an AI Study Assistant.

The user gave the following positive feedback:

{feedback}

Write a short professional response.

Requirements:
- Thank the user.
- Mention that you're happy the notes were useful.
- Maximum 3 sentences.
""",
    input_variables=["feedback"],
)

# ==========================================================
# Negative Response Prompt
# ==========================================================

NEGATIVE_RESPONSE_PROMPT = PromptTemplate(
    template="""
You are an AI Study Assistant.

The user gave the following negative feedback:

{feedback}

Write a short professional response.

Requirements:
- Apologize politely.
- Mention that you will improve future explanations.
- Offer to generate simpler notes.
- Maximum 3 sentences.
""",
    input_variables=["feedback"],
)

# ==========================================================
# Neutral Response Prompt
# ==========================================================

NEUTRAL_RESPONSE_PROMPT = PromptTemplate(
    template="""
You are an AI Study Assistant.

The user gave the following neutral feedback:

{feedback}

Write a short professional response.

Requirements:
- Thank the user.
- Mention that you appreciate the feedback.
- State that future explanations will continue improving.
- Maximum 3 sentences.
""",
    input_variables=["feedback"],
)