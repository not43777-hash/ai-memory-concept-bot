# 🧠 AI Memory Concept Bot

A minimal, beginner-friendly chatbot built with **Streamlit** and the **Gemini API** (`google-genai`) to explain the **"AI Memory — Find Anything"** ideathon project concept.

---

## 📌 The Concept in 5 Lines
1. **Problem:** Personal documents and data are scattered across Gmail, Google Drive, and local downloads, making files hard to find.
2. **Solution:** A unified AI search assistant that lets users search across connected apps using everyday, natural language.
3. **How It Works:** The AI extracts clues (topic, doc type, dates), searches authorized apps, and returns direct links to originals.
4. **Proposed Tech Stack:** React frontend, Python + FastAPI backend, Gmail & Google Drive APIs, and vector embeddings (planned MVP).
5. **Goal:** Provide one intelligent search engine for your entire digital life with privacy-first, permission-based access.

> ⚠️ **Important Note:** This chatbot is a **concept explainer / MVP prototype**, not the full product. The full AI Memory application and integrations are in the concept/planning phase, and no live performance benchmarks currently exist.

---

## 🔑 How to Get a Free Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Sign in with your Google account.
3. Click **"Create API Key"** and copy the generated key.
4. In this project folder, copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   *(On Windows Command Prompt / PowerShell: `copy .env.example .env`)*
5. Open `.env` and replace `your_key_here` with your actual key:
   ```env
   GEMINI_API_KEY=AIzaSy...
   ```

---

## 🚀 How to Run the Bot

### 1. (Optional but recommended) Set up a virtual environment:
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit application:
```bash
streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`.

---

## ☁️ Deploying to Streamlit Community Cloud
1. Push this repository to GitHub (ensure `.env` is never committed — `.gitignore` protects it).
2. Go to [share.streamlit.io](https://share.streamlit.io) and deploy your repository (Main file path: `app.py`).
3. In your Streamlit app dashboard, navigate to **Settings** > **Secrets**.
4. Add your Gemini API key in TOML format:
   ```toml
   GEMINI_API_KEY = "your_actual_gemini_api_key"
   ```
5. Click **Save** — the app will detect the secret automatically and run!

---

## 📁 Project Structure (6 Files Total)
- `app.py`: Streamlit user interface and Gemini integration with configurable model variable.
- `knowledge.md`: The verified project facts and guidelines used as the bot's source of truth.
- `requirements.txt`: Python dependencies (`streamlit`, `google-genai`, `python-dotenv`).
- `.env.example`: Template for environment variables.
- `.gitignore`: Prevents secret `.env` and Python cache files from being committed.
- `README.md`: Project documentation and setup guide.

---

## 👥 Team Titans
- **Institution:** Sapthagiri NPS University
- **Team Members:** Shubham Kumar, Vedansh Rai, Shreya Singh, Shubham Pandey
- **GitHub:** not43777-hash
