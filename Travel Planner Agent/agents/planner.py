from autogen_agentchat.agents import AssistantAgent
from models.gemini_model import model_client
from config.settings import GOOGLE_API_KEY, MODEL, MAX_TURNS, TERMINATATION_WORD

planner_agent = AssistantAgent(
    name="TravelPlannerAgent",
    model_client=model_client,
    system_message="You are a travel planner agent. Your task is to assist users in planning their trips by providing recommendations, itineraries, and travel tips based on their preferences and requirements.",
)