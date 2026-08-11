from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from agents import create_agents

# 🧠 AGENT DECISION CONTROLLER
def decision_controller(user_input, history):
    text = user_input.lower()
   
    count = sum(1 for issue in history if text in issue.lower())
    # 🚨 STRONG EMERGENCY KEYWORDS
    emergency_keywords = [
        "vomit", "vomiting",
        "weak", "collapse", "collapsed",
        "not eating", "not drinking",
        "bleeding", "unconscious",
        "high fever", "seizure", "can't stand"
    ]

    # Emergency detection
    if any(word in text for word in emergency_keywords ):
        return "EMERGENCY"
    elif any(word in text for word in ["vomit", "weak", "not eating"]):
        return "ATTENTION"

    elif count >= 2:
        return "REPEATED"

    else:
        return "NORMAL"

    # Repeated issue detection
    count = sum(1 for issue in history if text in issue.lower())
    if count >= 2:
        return "REPEATED"

    return "NORMAL"


# 🧠 PLANNING FUNCTION
def planning_agent(user_input):
    if "vomit" in user_input.lower() or "weak" in user_input.lower():
        return "High risk detected → prioritize immediate care and vet visit"
    else:
        return "Normal case → perform full analysis including simulation"

# 🛠️ SMART TOOL 1: HISTORY
def history_tool(history):
    if not history:
        return None

    from collections import Counter
    issue_counter = Counter(history)
    most_common, freq = issue_counter.most_common(1)[0]

    if freq >= 2:
        return f"⚠️ This issue is repeating frequently ({freq} times). Chronic condition possible."
    
    return "No major repeated issue detected"


# 🛠️ SMART TOOL 2: PROFILE
def profile_tool(pet_age, pet_type):
    if pet_age == 0:
        return None  # avoid wrong output

    if pet_age <= 1:
        return "🍼 Young pet → higher infection risk"
    
    if pet_age >= 7:
        return "🐶 Senior pet → higher risk"

    if pet_type == "Dog":
        return "🐕 Dogs prone to infections & allergies"
    
    return None


# 🛠️ SMART TOOL 3: PRIORITY
def priority_tool(user_input):
    text = user_input.lower()

    if "collapse" in text or "collapsed" in text:
        return "🚨 CRITICAL: Collapse detected → Immediate vet required"

    if "high fever" in text:
        return "🚨 CRITICAL: High fever → Possible infection"

    if "vomit" in text and "not eating" in text:
        return "🚨 High priority: Severe gastrointestinal issue"

    if "rash" in text or "scratching" in text:
        return "⚠️ Medium priority: Allergy or skin issue"

    return "Low priority symptoms"


# 🛠️ TOOL 1: FIRST AID
def first_aid_tool(user_input):
    if "vomit" in user_input.lower():
        return "Give small amounts of water, avoid food for few hours, monitor hydration"
    return "Provide basic rest and monitor condition"


# 🛠️ TOOL 2: VET SUGGESTION
def vet_tool():
    return "Nearest vet: ABC Veterinary Clinic (visit immediately if condition worsens)"


# 🔐 LOAD ENV
load_dotenv()

llm = ChatGroq(model_name="llama-3.1-8b-instant")


def log_step(message, verbose_log):
    print(message)          # 👈 shows in terminal
    verbose_log.append(message)   # 👈 keeps UI display

# 🚀 MAIN WORKFLOW
def run_workflow(user_input, history=[], pet_profile=None):
    verbose_log = []

    # 🧠 PLANNER AGENT (decides flow)
    log_step("🧭 Planner Agent → Analyzing situation", verbose_log)
    
    if len(history) > 1:
        next_step = "check_history"
    else:
        next_step = "analyze_symptoms"
    
    log_step(f"🧭 Planner Decision → {next_step}", verbose_log)

    # 🛠️ TOOL USAGE DECIDED BY PLANNER
    history_help = None
    profile_help = None

    if next_step == "check_history":
        log_step("🧭 Planner → Calling History Tool", verbose_log)
        history_help = history_tool(history)
        log_step(f"📊 History Tool → {history_help}", verbose_log)

    log_step("🧭 Planner → Checking profile", verbose_log)
    
    profile_help = profile_tool(
        pet_age=pet_profile.get("age", 0) if pet_profile else 0,
        pet_type=pet_profile.get("type", "") if pet_profile else ""
    )
    log_step(f"🐾 Profile Tool → {profile_help}", verbose_log)

    # 🧠 ANALYZER AGENT (LLM work)
    log_step("🤖 Analyzer Agent → Processing symptoms", verbose_log)

    symptom_output = llm.invoke(
        f"Analyze pet symptoms: {user_input}"
    ).content

    diagnosis_output = llm.invoke(
        f"Give diseases based on: {symptom_output}"
    ).content

    risk_output = llm.invoke(
        f"Evaluate severity: {symptom_output}"
    ).content

    simulation_output = llm.invoke(
        f"Untreated vs treated: {symptom_output}"
    ).content

    # 🧠 DECISION AGENT (FINAL AUTHORITY 🔥)
    log_step("🧠 Decision Agent → Evaluating severity", verbose_log)
    
    priority_help = priority_tool(user_input)

    decision_type = decision_controller(user_input, history)

    # 🔥 REAL OVERRIDE LOGIC (agent autonomy)
    if "CRITICAL" in str(priority_help):
        decision_type = "EMERGENCY"
        log_step(
             "🚨 Decision Agent → Overriding to EMERGENCY",
            verbose_log
        )
        

    elif "Medium" in str(priority_help):
        decision_type = "ATTENTION"
        log_step(
             "⚠️ Decision Agent →  Adjusted to ATTENTION",
            verbose_log
        )

    else:
        log_step(
             f"🧠 Decision Agent → Keeping {decision_type}",
            verbose_log
        )

    # 🧠 FINAL ACTIONS
    if decision_type == "EMERGENCY":
        urgency_output = "🚨 Immediate vet visit required"
        simulation_output = "Skipped due to emergency"
    elif decision_type == "REPEATED":
        urgency_output = "⚠️ Repeated issue → Vet needed"
    else:
        urgency_output = "Monitor condition at home"

    immediate_output = first_aid_tool(user_input)

    # 🧠 PLAN (decided AFTER everything)
    plan = planning_agent(user_input)

    log_step(f"🧭 Final Plan → {plan}", verbose_log)

    return {
        "decision_type": decision_type,
        "plan": plan,
        "symptoms": symptom_output,
        "diagnosis": diagnosis_output,
        "risk": risk_output,
        "simulation": simulation_output,
        "decision": diagnosis_output,
        "immediate": immediate_output,
        "urgency": urgency_output,
        "tools": {
            "history": history_help,
            "profile": profile_help,
            "priority": priority_help
        },
        "verbose": verbose_log
    }