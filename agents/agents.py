# agent.py

from llm import ask_llm
from tools import get_weather, check_calendar, send_email

def run_agent():


    task = "What is the weather like today?"

    prompt = f"""
    You are a simple AI agent.

    User task:
    {task}

    Available tools:
    - weather
    - calendar

    Decide which tool should be used to answer the user's task.

    Respond with only the name of the tool.
    """

    decision = ask_llm(prompt)

    print("Agent decision:", decision)

    # -------------------------
    # Execute the chosen tool
    # -------------------------

    if "weather" in decision.lower():

        result = get_weather()

    elif "calendar" in decision.lower():

        result = check_calendar()

    else:

        result = "The agent did not select a valid tool."


    print("Tool result:", result)
    return result