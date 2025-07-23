import pytest
from agents.planner import planner_agent
from agents.researcher import researcher_agent


def test_planner_agent():
    """Test the planner agent's initialization."""
    assert planner_agent.name == "TravelPlannerAgent"
    assert planner_agent.system_message == "You are a travel planner agent. Your task is to assist users in planning their trips by providing recommendations, itineraries, and travel tips based on their preferences and requirements."
    
