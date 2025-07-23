from autogen_agentchat.agents import CodeExecutorAgent
from config.docker_executor import get_docker_executor



def get_code_executor_agent():
    """
    Initializes and returns the CodeExecutorAgent with the model client.
    """
    docker = get_docker_executor()

    code_executor_agent = CodeExecutorAgent(
        name="CodeExecutorAgent",
        code_executor=docker,
    )
    print("CodeExecutorAgent initialized with Docker command line executor.")

    return code_executor_agent, docker