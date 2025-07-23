from autogen_agentchat.agents import CodeExecutorAgent

def GetCodeExecutorAgent(docker):
    """ Initializes and returns the CodeExecutorAgent with Docker."""
    code_executor_agent = CodeExecutorAgent(
        name="CodeExecutorAgent",
        code_executor=docker,
    )
    print("CodeExecutorAgent initialized with Docker command line executor.")

    return code_executor_agent