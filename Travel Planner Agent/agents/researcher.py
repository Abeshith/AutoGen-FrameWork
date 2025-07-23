from autogen_agentchat.agents import AssistantAgent
from models.gemini_model import model_client
from config.settings import GOOGLE_API_KEY, MODEL, MAX_TURNS, TERMINATATION_WORD


researcher_agent = AssistantAgent(
    name="TravelResearcherAgent",
    model_client=model_client,
    system_message="You are a travel researcher agent. Your task is to gather information about travel destinations, accommodations, and activities based on user queries and preferences.",
)