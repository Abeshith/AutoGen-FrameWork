from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import Swarm
from autogen_agentchat.conditions import TextMentionTermination, HandoffTermination
from dotenv import load_dotenv
from autogen_agentchat.messages import HandoffMessage
from autogen_agentchat.ui import Console
import asyncio
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
open_router_key = os.getenv("OPEN_ROUTER_API_KEY")

model_client = OpenAIChatCompletionClient(
    model="gemini-1.5-flash",
    api_key=api_key,
)

def refund_flight(flight_id: str) -> str:
    # Simulate refunding a flight

    return f"Flight ticket for {flight_id} has been successfully refunded."

travel_agent = AssistantAgent(
    name="TravelAgent",
    model_client=model_client,
    handoffs=['FlightRefunder', 'user'],
    system_message="""You are a travel agent. The flight_refunder is in charge of refunding flight tickets.
    If you need information from the user, you must first send your message and you ca n handoff to the user.
    Use 'TERMINATE' when the travel planning is done.
    """,
)

flight_refunder = AssistantAgent(
    name="FlightRefunder",
    model_client=model_client,
    handoffs=['TravelAgent','user'],
    tools=[refund_flight],
    system_message="""You are a agent that specializes in refunding flight.
    You only need flight PNR number to refund a flight.
    You have the ability to refund a flight using the refund_flight tool.
    If you need more information from the user, you must first send your message and you can handoff to the user.
    When the Transaction is done, handoff to the travel_agent to finalize.
    """
)

termination_condition = HandoffTermination(target='user') | TextMentionTermination('TERMINATE')

team = Swarm(participants=[travel_agent, flight_refunder], termination_condition=termination_condition)

task = "I need to refund my flight"

async def run_team() -> None:
    task_result = await Console(team.run_stream(task=task))
    
    last_message = task_result.messages[-1]
    print("Last Message is ---------->", last_message)

    while isinstance(last_message, HandoffMessage) and last_message.target == 'user':
        print(last_message.type)
        print("Last Message is ---------->", last_message)
        
        user_message = input("User: ")

        task_result = await Console(
            team.run_stream(task=HandoffMessage(source='user', target=last_message.source, content=user_message))
            )
        
        last_message = task_result.messages[-1]

if __name__ == "__main__":
    asyncio.run(run_team())