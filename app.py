import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# Load Environment Variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="AI LinkedIn Post Generator",
    page_icon="💼",
    layout="centered",
)

# Custom Styling
st.markdown("""
<style>
.block-container{
    max-width:850px;
    padding-top:2rem;
}
h1{
    text-align:center;
}
.stButton>button{
    width:100%;
    height:3rem;
    font-size:18px;
    font-weight:600;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# Load Model
model = ChatMistralAI(model="mistral-medium-3-5")

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert LinkedIn content writer who creates engaging, professional, and high-performing LinkedIn posts.

Your task is to generate a Human Written LinkedIn post based on the following inputs.

## Inputs
Topic: {topic}
Target Audience: {target_audience}
Tone: {tone}
Goal: {goal}

## Instructions

- Start with a strong hook in the first 1–2 lines.
- Keep the post between 150–250 words.
- Write in short, readable paragraphs.
- Use storytelling if appropriate.
- Include insights, lessons, or actionable advice.
- Add a clear Call-to-Action (CTA) at the end.
- Include 5–8 relevant hashtags.
- Do NOT use excessive emojis (maximum 2).
- Make the post feel authentic and human.
- Avoid generic AI-sounding phrases.
- Return only the final LinkedIn post.

## Output
LinkedIn Post:
            """,
        ),
        (
            "human",
            """
Topic: {topic}

Target Audience: {target_audience}

Tone: {tone}

Goal: {goal}
            """,
        ),
    ]
)

# ---------------- UI ---------------- #

st.title("💼 AI LinkedIn Post Generator")
st.caption("Generate engaging and professional LinkedIn posts in seconds.")

st.divider()

topic = st.text_input("Topic")
target_audience = st.text_input("Target Audience")
tone = st.text_input("Tone")
goal = st.text_input("Goal")

generate = st.button("✨ Generate LinkedIn Post")

if generate:

    if not all([topic, target_audience, tone, goal]):
        st.warning("Please fill in all the fields.")
    else:

        with st.spinner("Generating your LinkedIn post..."):

            final_prompt = prompt.invoke(
                {
                    "topic": topic,
                    "target_audience": target_audience,
                    "tone": tone,
                    "goal": goal,
                }
            )

            response = model.invoke(final_prompt)

        st.success("Post Generated Successfully!")

        st.markdown("## 📄 LinkedIn Post")

        # Markdown rendering (supports **bold**, lists, etc.)
        st.markdown(response.content)

        st.divider()

        # Copyable version (shows copy button)
        st.markdown("### 📋 Copy Post")
        st.code(response.content, language="markdown")