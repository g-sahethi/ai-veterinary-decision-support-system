# ai-veterinary-decision-support-system
You’re right 😭 — I should have given you the complete, cleaned, copy-paste-ready README in one go instead of making you fix pieces yourself.

Below is the final version. You can copy everything inside this block and paste it directly into your GitHub README.md.

# 🐾 AI Veterinary Decision Support System
## Agentic AI-Based Veterinary Decision Support
The AI Veterinary Decision Support System is a multi-agent AI application designed to assist pet owners with preliminary pet health assessment and decision support.
The system accepts symptoms provided by the pet owner and combines AI-based analysis, pet profile information, previous health history, risk assessment, and decision logic to determine the severity of the situation and provide appropriate veterinary guidance.
> ⚠️ This system is intended for preliminary decision support and educational purposes. It does not replace professional veterinary diagnosis or treatment.
---
## 🎯 What Does the System Do?
When a pet owner enters symptoms such as vomiting, weakness, fever, or other health concerns, the system:
1. Receives the pet's symptoms.
2. Checks the pet profile and available health history.
3. Determines the initial severity of the situation.
4. Uses intelligent tools for history, profile, and priority analysis.
5. Uses LLM-powered agents to analyze symptoms and possible conditions.
6. Evaluates the health risk.
7. Simulates possible outcomes.
8. Makes a final decision about the urgency.
9. Provides precautions and veterinary recommendations.
---
## 🤖 Multi-Agent Architecture
The system contains five specialized AI agents:
### 1. Symptom Analyzer Agent
Analyzes the symptoms provided by the pet owner and interprets possible health concerns.
### 2. Diagnosis Expert Agent
Uses the analyzed symptoms to identify possible veterinary conditions and generate diagnostic reasoning.
### 3. Risk Evaluator Agent
Evaluates the severity of the condition and identifies potentially critical situations.
### 4. Simulation Agent
Considers possible outcomes if the condition is treated or left untreated.
### 5. Decision Maker Agent
Combines the available analysis and generates the final veterinary decision and recommendation.
---
## 🧠 How the Agents and Workflow Interact
The system does not simply send the user's input to one AI model and return an answer. The workflow coordinates different stages of analysis and uses specialized agents and tools to process the situation.
### Example
Suppose the pet owner enters:
> "My dog has been vomiting and is not eating."
The workflow processes the situation through multiple stages:
```text

Pet Owner
   ↓
Pet Symptoms
   ↓
Planner / Workflow Controller
   ↓
History Analysis
   ↓
Pet Profile Analysis
   ↓
Symptom Analyzer
   ↓
Diagnosis Analysis
   ↓
Risk Evaluation
   ↓
Priority Assessment
   ↓
Decision Maker
   ↓
Final Recommendation

The system can also use the pet’s previous health history to identify repeated problems:

Previous Health History
        ↓
History Tool
        ↓
Repeated Issue Detected
        ↓
Decision Agent
        ↓
Higher Attention / Veterinary Consultation

For critical symptoms:

Symptoms
   ↓
Priority Analysis
   ↓
Critical Condition Detected
   ↓
Decision Agent
   ↓
EMERGENCY
   ↓
Immediate Veterinary Attention

⸻

🔄 Agent Workflow Logging

The project includes verbose workflow logging to make the decision process visible in the terminal.

Example:

🧭 Planner Agent → Analyzing situation
🧭 Planner Decision → check_history
🧭 Planner → Calling History Tool
📊 History Tool → Repeated issue detected
🧭 Planner → Checking profile
🐾 Profile Tool → Dog profile risk
🤖 Analyzer Agent → Processing symptoms
🧠 Decision Agent → Evaluating severity
🧠 Decision Agent → Keeping EMERGENCY
🧭 Final Plan → High risk detected

This provides visibility into the sequence of workflow decisions, tool usage, analysis stages, and final action.

⸻

🛠️ Intelligent Tools

The system uses specialized tools within the workflow.

History Tool

Checks previous pet health records and identifies repeated health issues.

Profile Tool

Uses information such as pet age and pet type to identify profile-based risks.

Priority Tool

Checks reported symptoms for critical or high-priority conditions.

First-Aid Tool

Provides basic precautionary guidance based on the reported symptoms.

Veterinary Suggestion Tool

Provides veterinary visit guidance when the situation requires professional attention.

⸻

🐾 Pet Profile and Memory

The system maintains pet-specific information such as:

* Pet Name
* Age
* Type
* Breed
* Gender
* Previous Health Issues

This information can be considered when analyzing new symptoms.

The system can also identify repeated health issues from the stored history and use this information during decision-making.

⸻

🚨 Decision Classification

The system can classify cases into different decision categories:

* NORMAL
* ATTENTION
* REPEATED
* EMERGENCY

Critical symptoms can cause the Decision Agent to override the initial decision and classify the condition as an emergency.

⸻

💡 Key Features

* 🐾 Pet profile management
* 🧠 AI-based symptom analysis
* 🤖 Multi-agent architecture
* 📊 Health-history analysis
* ⚠️ Risk evaluation
* 🚨 Emergency detection
* 🔄 Dynamic decision-making
* 🔮 Treatment and untreated-condition simulation
* 💊 Immediate precaution suggestions
* 🧭 Agent workflow logging
* 📋 Veterinary decision support

⸻

🧰 Technologies Used

* Python
* CrewAI
* LangChain-Groq
* Groq API
* Llama 3.1 8B Instant
* Streamlit
* python-dotenv

⸻

🏗️ Project Structure

ai-veterinary-decision-support-system/
│
├── app.py
├── workflow.py
├── agents.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│   └── helpers.py
│
└── screenshots/
    ├── dashboard.png
    └── agent-workflow.png

⸻

▶️ How to Run

1. Clone the Repository

git clone https://github.com/g-sahethi/ai-veterinary-decision-support-system.git

2. Open the Project

cd ai-veterinary-decision-support-system

3. Install Dependencies

pip install -r requirements.txt

4. Configure the Groq API Key

Create a .env file locally:

GROQ_API_KEY=your_api_key_here

Do not upload the .env file to GitHub.

5. Run the Application

streamlit run app.py

⸻

📊 Project Outcome

The project demonstrates how Agentic AI can be applied to veterinary decision support by combining specialized agents, intelligent tools, memory-based analysis, LLM reasoning, and dynamic decision-making into a single workflow.

It provides a practical example of using multi-agent AI to analyze a real-world problem and produce an actionable decision rather than simply generating a text response.

⸻

⚠️ Disclaimer

This project is intended for educational and preliminary decision-support purposes only. It does not replace professional veterinary diagnosis, treatment, or emergency veterinary care.

