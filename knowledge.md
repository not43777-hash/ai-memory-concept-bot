# AI Memory — Project Concept Knowledge Base

## Source of Truth
This document contains the verified facts for the **AI Memory — Find Anything** ideathon project concept.

---

## 1. Project Overview & Identity
- **Project Name:** AI Memory — Find Anything
- **Tagline:** "Your entire digital life. One intelligent search."
- **Team Name:** Team Titans
- **Institution:** Sapthagiri NPS University
- **Team Members:**
  - Shubham Kumar
  - Vedansh Rai
  - Shreya Singh
  - Shubham Pandey
- **GitHub Repository:** not43777-hash
- **Current Status:** Proposed concept / MVP idea (NOT a finished product).

---

## 2. Problem Statement
- Digital information is scattered across multiple locations: email inboxes, cloud storage platforms, and local downloads folders.
- People frequently forget exact filenames, folder locations, and timestamps.
- Standard keyword search requires users to repeatedly guess keywords and manually check each app one by one.

---

## 3. Proposed Solution
- A single centralized AI assistant that searches across connected productivity applications (specifically Gmail and Google Drive).
- Users formulate questions in everyday, conversational language.
- The AI discovers relevant emails, files, and contextual data, and returns direct links to the original documents.

---

## 4. How It Works (4-Step Workflow)
1. **User asks:** The user asks a question in everyday language (e.g., *"Find the receipt for my headphones bought two months ago"*).
2. **AI extracts clues:** The AI analyzes the prompt to identify key clues, including the item/topic, document type (receipt, invoice, ticket), and estimated time range.
3. **Searches authorized sources:** The system queries only authorized, connected sources (Gmail and Google Drive).
4. **Ranks matches & displays links:** The AI ranks relevant matches and displays direct links to original files and emails along with a concise summary.

---

## 5. Key Features
- **Natural-Language Search:** Formulate queries as normal sentences instead of rigid keywords.
- **Semantic & Fuzzy Search:** Understands intent and variations even when exact keywords are misspelled or omitted.
- **Cross-Platform Search:** Simultaneously searches Gmail and Google Drive in one place.
- **Summaries & Contextual Answers:** Provides instant answers and context extracted from matching files.
- **Direct Source Links:** Delivers one-click links directly back to the original email or Drive file.
- **Secure Permission-Based Access:** Connects only through user-approved OAuth authorizations.

---

## 6. Proposed Tech Stack (Conceptual / Not Built Yet)
- **Frontend:** React
- **Backend:** Python + FastAPI
- **Integrations / APIs:** Gmail API and Google Drive API
- **AI / LLM:** Large Language Model (LLM) to interpret queries and synthesize summaries
- **Data & Indexing:** Text indexing, vector embeddings, and a vector database for semantic retrieval
- *Note:* This tech stack represents the proposed architecture for the eventual build. It has not been implemented yet.

---

## 7. Demo Scenario & Performance Reality
- **Demo Scenario:** A user asks: *"Find my laptop invoice from last month"*. The AI locates the matching email, the attached invoice PDF, the exact date, and direct links to the originals.
- **Performance Metrics:** There are currently **no measured performance numbers or benchmarks** (speed, accuracy, or latency), as this is an early concept proposal.

---

## 8. Future Scope & Roadmap
- Integration with more cloud and productivity apps (e.g., Notion, Slack, OneDrive, Dropbox).
- Voice search capabilities.
- Personalized document organization and automated tagging.
- Stronger privacy controls and granular, role-based permission settings.

---

## 9. Strict Bot Rules & Tone Guidelines
1. **Fact Fidelity:** Answer strictly and ONLY from the facts listed above. Do not invent features, integrations, team details, or stats.
2. **Out of Scope Handling:** If asked about anything outside these facts, clearly state that it is not part of the project concept and suggest a related question they can ask (e.g., "That is not part of our current concept. You could ask: 'How does AI Memory work?' or 'What tech stack is proposed?'").
3. **Honesty & Transparency:** Always emphasize that this is a proposed concept / MVP idea, not a fully built product. Never claim that the app is live, running in production, or has existing benchmarks.
4. **Simplicity & Conciseness:** Keep responses short (2 to 5 sentences) and easy for a first-year student to follow. Avoid overly dense academic jargon.
