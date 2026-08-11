from crewai import Agent

def create_agents():

    model = "groq/llama-3.1-8b-instant"

    symptom_agent = Agent(
        role="Symptom Analyzer",
        goal="Understand pet symptoms clearly",
        backstory="Expert in veterinary symptom analysis",
        llm=model
    )

    diagnosis_agent = Agent(
        role="Diagnosis Expert",
        goal="Generate possible diseases",
        backstory="Veterinary doctor AI",
        llm=model
    )

    risk_agent = Agent(
        role="Risk Evaluator",
        goal="Assess severity level",
        backstory="Expert in pet health risk",
        llm=model
    )

    simulation_agent = Agent(
        role="Simulation Agent",
        goal="Predict outcomes if treated or ignored",
        backstory="Predictive health model",
        llm=model
    )

    decision_agent = Agent(
        role="Decision Maker",
        goal="Give final recommendation",
        backstory="Senior vet decision system",
        llm=model
    )

    return (
        symptom_agent,
        diagnosis_agent,
        risk_agent,
        simulation_agent,
        decision_agent
    )
    