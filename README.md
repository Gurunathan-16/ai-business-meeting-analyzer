# 📊 AI Business Meeting Analyzer

An AI-powered meeting intelligence application that analyzes business meeting transcripts using Google's Gemini Large Language Model (LLM). The application automatically extracts key insights, including executive summaries, decisions, action items, risks, blockers, participant analysis, and overall project status, helping teams quickly understand meeting outcomes.

---

## 🚀 Features

- 📄 Upload meeting transcripts (.txt)
- 🤖 AI-powered meeting analysis using Google Gemini
- 📌 Executive Summary generation
- ✅ Key Decisions extraction
- 📋 Action Items with owner and deadline
- 🚧 Risks & Blockers identification
- ❓ Open Questions detection
- ➡️ Next Steps recommendation
- 👥 Participant Analysis
- 📊 Project Status classification (Green / Yellow / Red)
- ⚡ Interactive Streamlit user interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Interactive Web Application |
| Google Gemini API | AI Meeting Analysis |
| python-dotenv | Environment Variable Management |

---

## 📂 Project Structure

```text
meeting-analyzer/
│
├── app.py                 # Streamlit application
├── analyzer.py            # Gemini AI integration
├── prompts.py             # Prompt template
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables
│
├── sample_data/
│   └── meeting.txt
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-github-username/meeting-analyzer.git
cd meeting-analyzer
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### 5. Run the Application

```bash
streamlit run app.py
```

---

## 📊 Application Workflow

```text
Meeting Transcript (.txt)
            │
            ▼
Upload through Streamlit
            │
            ▼
Google Gemini API
            │
            ▼
AI Analysis
            │
            ▼
──────────────────────────────
Executive Summary
Key Decisions
Action Items
Risks & Blockers
Open Questions
Next Steps
Participant Analysis
Project Status
──────────────────────────────
```

---

## 💡 Sample Use Case

A project manager uploads a meeting transcript after a sprint planning session.

The AI automatically identifies:

- Executive Summary
- Key Decisions
- Action Items
- Risks and Blockers
- Next Steps
- Project Status

This helps stakeholders review meeting outcomes within seconds instead of reading lengthy transcripts.

---

## 📸 Screenshots

### Home Page

> Add a screenshot of the application home page.

### Meeting Analysis

> Add a screenshot showing the generated analysis.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Large Language Model (LLM) Integration
- Prompt Engineering
- Natural Language Processing (NLP)
- AI-powered Business Process Automation
- Streamlit Application Development
- Python Project Structuring
- API Integration
- Environment Variable Management

---

## 🔮 Future Enhancements

- 📄 PDF Report Export
- 📝 DOCX Report Export
- 📥 Markdown Report Export
- 🎤 Audio Meeting Analysis
- 🗣️ Speech-to-Text Integration
- 📈 Meeting Analytics Dashboard
- 💾 Meeting History
- 🔍 Search Across Previous Meetings
- ☁️ Cloud Deployment

---

## 👨‍💻 Author

**Gurunathan R**

AI Engineer | Machine Learning | Deep Learning | Generative AI

- **GitHub:** https://github.com/Gurunathan-16
- **LinkedIn:** https://linkedin.com/in/gurunathan-r

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.