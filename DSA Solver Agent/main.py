import asyncio
from teams.dsa_solver import create_dsa_solver_team
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from config.docker_utils import start_docker_container, stop_docker_container

async def main():
    team, docker = create_dsa_solver_team()

    try:
        await start_docker_container(docker)
        print("Docker container started successfully.")

        task = "Write a Python code to find a Armstrong number between 1 - 100."
        
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print('==' * 20)
                print(message.source, ": ", message.content)
            elif isinstance(message, TaskResult):
                print("Task Result:", message.stop_reason)
                
    except Exception as e:
        print(f"Error during code execution: {e}")
    finally:
        await stop_docker_container(docker)
        print("Docker container stopped successfully.")


if __name__ == "__main__":
    asyncio.run(main())