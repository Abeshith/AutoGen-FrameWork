import asyncio
from agents.code_executor_agent import GetCodeExecutorAgent
from agents.data_analyser_agent import GetDataAnalyzerAgent
from teams.analyzer_gpt import GetAnalyzerGPTTeam
from config.docker_utils import start_docker_container, stop_docker_container, GetDockerCommandLineExecutor
from models.google_model_client import GetModelClient
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

async def main():
    model_client = GetModelClient()

    docker = GetDockerCommandLineExecutor()

    team = GetAnalyzerGPTTeam(docker, model_client)

    try:
        task ='Can you tell me How many rows and columns are there in the titanic.csv file?'

        await start_docker_container(docker)

        async for message in team.run_stream(task=task):
            print('=' * 20)
            if isinstance(message, TextMessage):
                print(f"Message from {message.source} : {message.content}")
            elif isinstance(message, TaskResult):
                print("Stop Reason: ", message.stop_reason)
            

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await stop_docker_container(docker)


if __name__ == "__main__":
    asyncio.run(main())




