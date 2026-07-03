# 📚 AI Study Assistant using LangChain

> An end-to-end **Production-Level AI Study Assistant** built using **LangChain**, **Google Gemini**, and **Streamlit**. The application generates comprehensive study notes, creates interview/exam questions and answers using **RunnableParallel**, analyzes user feedback through **Sentiment Analysis**, and responds intelligently using **RunnableBranch (Conditional Chains)**.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

# 🚀 Project Overview

AI Study Assistant is an intelligent learning platform that helps students generate structured study material on any topic using Google's Gemini model through LangChain.

The application demonstrates modern **LLM Application Development** concepts including:

- Prompt Engineering
- LangChain Chains
- RunnableParallel
- RunnableBranch
- Output Parsing
- Pipeline Architecture
- Production-Level Project Structure
- Exception Handling
- Logging
- Streamlit Deployment

---

# ✨ Features

## 📖 Study Notes Generation

Generate detailed notes on any topic.

Each generated note includes:

- Introduction
- Explanation
- Important Concepts
- Examples
- Advantages
- Disadvantages
- Applications
- Summary

---

## ⚡ Parallel Processing using RunnableParallel

After generating notes, the application simultaneously creates:

- ✅ 5 Interview / Exam Questions
- ✅ Short Answers

using LangChain's

- RunnableParallel

---

## 💬 Feedback Collection

Users can provide feedback after reading the notes.

Example:

```
These notes were amazing!
```

or

```
I didn't understand the explanation.
```

---

## 😊 Sentiment Analysis

The feedback is automatically classified into:

- Positive
- Negative
- Neutral

using

- LangChain
- Gemini
- Pydantic Output Parser

---

## 🔀 Conditional Chain (RunnableBranch)

Depending on the detected sentiment, the application generates an intelligent response.

Positive →

> Thank the user.

Negative →

> Apologize and offer better explanations.

Neutral →

> Appreciate the feedback professionally.

---

## 📊 Production-Level Logging

The application logs:

- Application Start
- Topic Entered
- Notes Generated
- Questions Generated
- Answers Generated
- Feedback Received
- Sentiment Detected
- Errors

Logs are stored inside

```
logs/app.log
```

---

## 🛡 Exception Handling

Custom exception handling is implemented across the project.

The application gracefully handles

- Invalid API Keys
- Empty Inputs
- API Errors
- Runtime Exceptions

without crashing.

---

# 🏗 Project Architecture

```
                        User
                          │
                          ▼
                 Streamlit Interface
                          │
                          ▼
                 Notes Generation Chain
                          │
                          ▼
                 Generated Study Notes
                          │
                          ▼
                 RunnableParallel
             ┌────────────┴────────────┐
             ▼                         ▼
      Question Chain             Answer Chain
             │                         │
             └────────────┬────────────┘
                          ▼
                Display Results
                          │
                          ▼
                 User Feedback
                          │
                          ▼
               Sentiment Analysis Chain
                          │
                          ▼
          Positive / Negative / Neutral
                          │
                          ▼
                 RunnableBranch
             ┌────────┬────────┬────────┐
             ▼        ▼        ▼
        Positive   Negative  Neutral
             │        │        │
             └────────┴────────┘
                     ▼
              AI Response
```

---

# 🏛 Project Structure

```
AI_Study_Assistant/
│
├── app.py
│
├── requirements.txt
├── setup.py
├── README.md
├── LICENSE
├── .gitignore
├── .env
│
├── assets/
│      └── logo.png
│
├── logs/
│      └── app.log
│
├── config/
│      ├── __init__.py
│      └── config.py
│
├── src/
│
│      ├── constants.py
│      ├── prompt.py
│      ├── parser.py
│      ├── llm.py
│      ├── chains.py
│      ├── logger.py
│      ├── utils.py
│      ├── exception.py
│      │
│      └── pipeline/
│             ├── notes_pipeline.py
│             ├── parallel_pipeline.py
│             ├── sentiment_pipeline.py
│             └── conditional_pipeline.py
│
└── templates/
```

---

# ⚙ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangChain | LLM Orchestration |
| Google Gemini 2.5 Flash | Large Language Model |
| Streamlit | Frontend |
| Pydantic | Structured Output Parsing |
| python-dotenv | Environment Variables |
| Logging | Application Monitoring |
| pathlib | File Management |
| setuptools | Packaging |

---

# 🧠 LangChain Components Used

This project demonstrates multiple LangChain concepts.

### PromptTemplate

Used for

- Notes Generation
- Question Generation
- Answer Generation
- Sentiment Analysis
- AI Responses

---

### RunnableParallel

Used for

Generating

- Questions
- Answers

simultaneously.

---

### RunnableBranch

Used for

Conditional AI Responses

based on

- Positive
- Negative
- Neutral

sentiment.

---

### Output Parsers

- StrOutputParser
- PydanticOutputParser

---

### Prompt Engineering

Every prompt is stored separately inside

```
src/prompt.py
```

making the project modular.

---

# 📂 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AI_Study_Assistant.git

cd AI_Study_Assistant
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Environment Variables

Create a file named

```
.env
```

Add

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

MODEL_NAME=gemini-2.5-flash

TEMPERATURE=0.3

MAX_OUTPUT_TOKENS=2048
```

---

# ▶ Run the Application

```bash
streamlit run app.py
```

---

# 🖥 Application Workflow

```
User enters Topic
        │
        ▼
Generate Notes
        │
        ▼
RunnableParallel
        │
 ┌──────┴────────┐
 ▼               ▼
Questions      Answers
        │
        ▼
Display
        │
        ▼
Feedback
        │
        ▼
Sentiment Analysis
        │
        ▼
RunnableBranch
        │
        ▼
AI Response
```

---

# 📸 Screenshots

## 🖥️ Home Page

![Home Page](https://raw.githubusercontent.com/Shravan4598/AI-Study-Assistant-using-LangChain/main/assets/Home_page.png)

---

## Generated Notes

> *(Add Screenshot Here)*

---

## Generated Questions

> *(Add Screenshot Here)*

---

## Generated Answers

> *(Add Screenshot Here)*

---

## Sentiment Analysis

> *(Add Screenshot Here)*

---

# 📈 Future Improvements

- PDF Export
- Voice-based Learning
- Flashcard Generation
- Quiz Evaluation
- Chat with Notes
- Retrieval-Augmented Generation (RAG)
- Multi-language Support
- Authentication
- Study History
- Database Integration
- Dark Mode
- Docker Deployment
- CI/CD Pipeline
- Cloud Deployment (AWS, Azure, GCP)

---

# 📚 Learning Outcomes

This project demonstrates knowledge of

- Prompt Engineering
- LangChain
- RunnableParallel
- RunnableBranch
- Output Parsers
- LLM Integration
- Google Gemini API
- Streamlit
- Modular Python Development
- Logging
- Exception Handling
- Production-Level Project Architecture

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Shravan Kumar Pandey**

**B.Tech (Hons.) Data Science**

GitHub: https://github.com/Shravan4598

LinkedIn: https://www.linkedin.com/in/shravan-kumar-pandey-309786309/

Email: shravankumarpandey825412@gmail.com

---

# ⭐ If you found this project useful...

Please consider giving this repository a ⭐ on GitHub!

It motivates further development and helps others discover the project.
