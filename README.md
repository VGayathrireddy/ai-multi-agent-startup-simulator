# 🚀 AI Startup Simulator

An AI-powered multi-agent system that transforms a simple startup idea into a complete, structured business plan using LLMs and LangGraph.

---

## 📌 Overview

AI Startup Simulator is a full-stack application that takes a user’s startup idea and generates a professional business plan using multiple AI agents.

It demonstrates:
- Multi-agent AI architecture
- Workflow orchestration using LangGraph
- Real-time frontend + backend integration
- Document generation (DOCX)

---

## 🧠 How It Works

1. User enters a startup idea
2. LangGraph orchestrates multiple AI agents
3. Each agent performs a specific task:
   - Idea refinement
   - Market analysis
   - Business model generation
   - Growth strategy creation
4. Results are combined into a structured business plan
5. Output is:
   - Displayed on frontend
   - Available for download as DOCX

---

## 🧩 Architecture
```bash
User Input
      ↓
LangGraph Workflow
      ↓
[ Ideation Agent ]
      ↓
[Market_Research_Agent], [Business_Model_Agent],  [Growth_Strategy_Agent]
      ↓
Final Node
      ↓
Formatted Business Plan Output
      ↓
Frontend + DOCX Download
```

---

## 🤖 AI Agents

### 1. Ideation Agent
- Refines the startup idea
- Defines problem, users, and value proposition

### 2. Market Research Agent
- Market demand
- Competitors
- Trends
- Market size

### 3. Business Agent
- Revenue streams
- Pricing strategy
- Cost structure
- Partnerships

### 4. Growth Strategy Agent
- Marketing channels
- User acquisition
- Growth strategy

---

## ⚙️ Tech Stack

### 🧠 AI & Backend
- Python
- FastAPI
- LangGraph
- Ollama (LLM - Mistral model)

### 🌐 Frontend
- HTML
- CSS
- JavaScript (Vanilla)

### 📄 Document Generation
- python-docx

---

## 🔥 Features

- ✅ Multi-agent AI system
- ✅ LangGraph workflow orchestration
- ✅ Structured business plan generation
- ✅ Real-time frontend rendering
- ✅ DOCX export functionality
- ✅ Clean UI
- ✅ Modular architecture

---

## 📂 Project Structure
```bash
AI-STARTUP-SIMULATOR/
│
├── agents/
│ ├── ideation_agent.py
│ ├── market_research_agent.py
│ ├── business_agent.py
│ └── growth_strategy_agent.py
│
├── graph/
│ └── workflow.py
│
├── utils/
│ └── formatter.py
│
├── llm/
│ └── ollama_client.py
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── outputs/
│ └── business_plan.docx
│
└── main.py
└── requirements.txt
└── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/VGayathrireddy/ai-multi-agent-startup-simulator
cd ai-multi-agent-startup-simulator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run Ollama (LLM)
```bash
ollama run mistral
```

### 4. Start Backend
```bash
uvicorn main:app --reload
```

### 5. Open Frontend
Open:
```bash
frontend/index.html
```

📸 Output Example

The system generates:

- Executive Summary
- Product & Problem
- Market Analysis
- Business Model
- Growth Strategy

👉 Fully structured business plan

📥 API Endpoints
Generate Plan
```bash
GET /generate?prompt=your_idea
```
Download DOCX
```bash
GET /download?prompt=your_idea
```
---

💡 Key Highlights
- Uses LangGraph instead of traditional pipelines
- Demonstrates real-world AI orchestration
- Converts raw idea → structured business plan
- Strong example of AI + Full Stack Integration

🧠 Future Improvements
- PDF export with styled templates
- User authentication
- Save & history feature
- Advanced UI (React / Tailwind)
- Multi-language support
- Deployment (Docker + Cloud)

---

⭐ If you like this project

Give it a star ⭐ and share your feedback!
