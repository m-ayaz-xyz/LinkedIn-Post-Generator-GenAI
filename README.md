# AI LinkedIn Post Generator

Generate professional, engaging, and human-like LinkedIn posts using **LangChain**, **Mistral AI**, and **Streamlit**.

---

## Features

* Generate high-quality LinkedIn posts
* Human-like writing style
* Strong opening hooks
* Professional tone
* Clear Call-to-Action (CTA)
* Relevant hashtags
* Markdown formatting support
* One-click copy option
* Clean Streamlit UI

---

## Tech Stack

* Python
* Streamlit
* LangChain
* Mistral AI
* python-dotenv

---

## Project Structure

```text
.
├── app.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-linkedin-post-generator.git

cd ai-linkedin-post-generator
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Application Preview

The application allows you to enter:

* Topic
* Target Audience
* Tone
* Goal

It then generates a polished LinkedIn post with proper formatting and hashtags.

---

## Requirements

Example `requirements.txt`

```text
streamlit
langchain
langchain-core
langchain-mistralai
python-dotenv
```

---
