from teams.travel_team import team
import asyncio

async def main():
    """Main function to run the travel planning team."""
    print("Starting the Travel Planning Team...")
    
    task = "I want to plan a trip to Paris next month. Can you help me with recommendations?"
    
    result = await team.run(task=task)

    for message in result.messages:
        print(f"{message.source}: {message.content}")

if __name__ == "__main__":
    asyncio.run(main())