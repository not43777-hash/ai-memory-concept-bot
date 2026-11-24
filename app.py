import os
import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
from google import genai
from google.genai import types

# ---------------------------------------------------------
# Configuration: easily switch the Gemini model here
# ---------------------------------------------------------
MODEL_NAME = "gemini-3.5-flash-lite"

# Load environment variables from .env file (local) or st.secrets (Streamlit Community Cloud)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    try:
        if "GEMINI_API_KEY" in st.secrets:
            GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

# ---------------------------------------------------------
# Page Setup & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI Memory Concept Bot",
    page_icon="🧠",
    layout="centered"
)

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------
@st.cache_data
def load_knowledge_base():
    """Load the project facts and rules from knowledge.md."""
    knowledge_path = os.path.join(os.path.dirname(__file__), "knowledge.md")
    if os.path.exists(knowledge_path):
        with open(knowledge_path, "r", encoding="utf-8") as f:
            return f.read()
    return "Knowledge base file missing. Please ensure knowledge.md is present."


def build_system_prompt(knowledge_content: str) -> str:
    """Create the system instruction prompt enforcing rules and facts."""
    return f"""You are the "AI Memory Concept Bot", a beginner-friendly assistant for explaining an ideathon project concept.

SOURCE OF TRUTH & PROJECT FACTS:
\"\"\"
{knowledge_content}
\"\"\"

CRITICAL OPERATING RULES:
1. Answer ONLY using the facts provided above. If a user asks anything outside of these facts (e.g. pricing, unmentioned integrations, competitors, or general trivia), politely state that it is not part of the project concept and suggest one or two related questions they can ask instead.
2. Always be completely transparent and honest that this is a PROPOSED CONCEPT / MVP idea, NOT a finished product.
3. NEVER invent features, statistics, latency numbers, benchmarks, or integrations.
4. Keep all responses concise (strictly 2 to 5 sentences) and simple enough for a first-year college student to easily understand.
"""

# Load knowledge base content
knowledge_text = load_knowledge_base()
SYSTEM_PROMPT = build_system_prompt(knowledge_text)

# ---------------------------------------------------------
# UI Header & Disclaimer
# ---------------------------------------------------------
st.title("🧠 AI Memory Concept Bot")
st.caption("Your entire digital life. One intelligent search. | Team Titans")

# Prominent concept disclaimer
st.info(
    "⚠️ **Concept demo — not the real product.** "
    "This bot is designed solely to explain the proposed ideathon concept and MVP architecture.",
    icon="ℹ️"
)

# ---------------------------------------------------------
# Check for API Key
# ---------------------------------------------------------
if not GEMINI_API_KEY or GEMINI_API_KEY.strip() == "" or GEMINI_API_KEY == "your_key_here":
    st.error(
        "🔑 **Gemini API Key missing or invalid!**\n\n"
        "**Local setup:**\n"
        "1. Create a `.env` file in the project directory.\n"
        "2. Add: `GEMINI_API_KEY=your_actual_api_key`\n\n"
        "**Streamlit Community Cloud:**\n"
        "1. Go to your app dashboard > **Settings** > **Secrets**.\n"
        "2. Add: `GEMINI_API_KEY = \"your_actual_api_key\"`\n\n"
        "*(You can get a free key at [Google AI Studio](https://aistudio.google.com/app/apikey))*",
        icon="🚨"
    )

# ---------------------------------------------------------
# Session State for Chat History & Auto-scroll Counter
# ---------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I'm the AI Memory Concept Bot. Ask me anything about our ideathon project, how it works, or the proposed tech stack!"
        }
    ]

if "answer_count" not in st.session_state:
    st.session_state.answer_count = 0

# ---------------------------------------------------------
# Clickable Example Questions
# ---------------------------------------------------------
example_prompt = None
is_initial = len(st.session_state.messages) <= 1

with st.expander("Try an example question", expanded=is_initial):
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        if st.button("❓ What problem does this solve?", use_container_width=True):
            example_prompt = "What problem does this solve?"
    with col2:
        if st.button("⚙️ How does it work?", use_container_width=True):
            example_prompt = "How does it work?"
    with col3:
        if st.button("💻 What tech will you use?", use_container_width=True):
            example_prompt = "What tech will you use?"
    with col4:
        if st.button("🚀 What is the future scope?", use_container_width=True):
            example_prompt = "What is the future scope?"

# ---------------------------------------------------------
# Render Existing Chat Messages
# ---------------------------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------------------------------------------------
# Handle User Input (Chat box or Example button)
# ---------------------------------------------------------
chat_input = st.chat_input("Ask a question about the AI Memory concept...")

# Determine prompt to send
active_prompt = example_prompt or chat_input

if active_prompt:
    # 1. Append and display user message
    st.session_state.messages.append({"role": "user", "content": active_prompt})
    with st.chat_message("user"):
        st.write(active_prompt)

    # Place the "latest" anchor just before the newest assistant answer
    st.markdown('<div id="latest"></div>', unsafe_allow_html=True)

    # 2. Check API key before attempting call
    if not GEMINI_API_KEY or GEMINI_API_KEY.strip() == "" or GEMINI_API_KEY == "your_key_here":
        warning_msg = "Cannot generate response: GEMINI_API_KEY is not set. Please add your key to `.env` or Streamlit Secrets."
        with st.chat_message("assistant"):
            st.warning(warning_msg)
        st.session_state.messages.append({"role": "assistant", "content": warning_msg})
        st.session_state.answer_count += 1
    else:
        # 3. Generate response via Gemini API
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    client = genai.Client(api_key=GEMINI_API_KEY)

                    # Build conversation contents formatted for google-genai SDK
                    contents = []
                    # Skip initial greeting so history starts cleanly with a user message
                    for m in st.session_state.messages[1:]:
                        role = "user" if m["role"] == "user" else "model"
                        contents.append(
                            types.Content(
                                role=role,
                                parts=[types.Part.from_text(text=m["content"])]
                            )
                        )

                    response = client.models.generate_content(
                        model=MODEL_NAME,
                        contents=contents,
                        config=types.GenerateContentConfig(
                            system_instruction=SYSTEM_PROMPT,
                            temperature=0.2,
                        )
                    )

                    bot_reply = response.text if response.text else "Sorry, I couldn't generate a response."
                    st.write(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                    st.session_state.answer_count += 1

                except Exception as e:
                    error_msg = f"⚠️ An error occurred while communicating with Gemini API: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
                    st.session_state.answer_count += 1

    # Auto-scroll to the latest assistant message (fresh script per answer via counter + 300ms delay)
    components.html(
        f"""
        <script>
        var n = {st.session_state.answer_count};
        setTimeout(function() {{
            try {{
                var el = window.parent.document.getElementById("latest");
                if (el) {{
                    el.scrollIntoView({{behavior: "smooth", block: "start"}});
                }}
            }} catch (e) {{}}
        }}, 300);
        </script>
        """,
        height=0,
    )
