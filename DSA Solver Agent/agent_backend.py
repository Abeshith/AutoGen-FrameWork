from autogen_agentchat.agents import CodeExecutorAgent, AssistantAgent
import asyncio
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.base import TaskResult
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

model_client = OpenAIChatCompletionClient(
    model='gemini-1.5-flash',
    api_key=api_key
)

async def main():
    docker = DockerCommandLineCodeExecutor(
        image='python:3.11-slim',
        work_dir='temp',
        timeout=120,
    )

    code_executor_agent = CodeExecutorAgent(
        name="CodeExecutorAgent",
        code_executor=docker,
    )

    problem_solver_agent = AssistantAgent(
        name="ProblemSolverAgent",
        model_client=model_client,
        system_message='''You are a problem solver agent. Your task is to assist users in solving programming problems by providing code solutions
        and explanations for Data Structures and Algorithms and code with efficient time complexity and 
        also provide a brute solution first and make the solution to best efficient solution like provide two solutions.
        You will be Working with a code executor agent to execute the code.
        You will be provided with a problem statement and you need to provide
        1. Write The solution to the problem statement in Python and At begining of your response specify the plan to solve the task.
        2. Write a brute force solution for the problem statement.
        3. Write an efficient solution for the problem statement.
        4. Provide the time complexity of both solutions.
        5. Provide the efficient code in a one code block at a time and then pass it to code executor agent to execute it.
        6. Once the code is executed, You have the results and Check It With atleast 3 test cases whether is working correctly.
        7. Explain the results of code execution and how the code works with the ouput.
        8. Once Above every steps are done, Provide the final solution in a single code block and You have to say "STOP"to stop the conversation.
        ''',
    )

    termination_condition = TextMentionTermination('STOP')
    
    team = RoundRobinGroupChat(
        participants=[problem_solver_agent, code_executor_agent],
        termination_condition=termination_condition,
        max_turns=10,
    )


    
    await docker.start()
    try:
        task = "Write a Python code to find a Armstrong number between 1 - 100."
        
        async for message in team.run_stream(task= task):
            print('==' * 20)
            if isinstance(message, TextMessage):
                print(message.source, ": ", message.content)
            elif isinstance(message, TaskResult):
                print("Task Result:", message.stop_reason)

    except Exception as e:
        print(f"Error during code execution: {e}")

    finally:
        docker.stop()



if __name__ == "__main__":
    asyncio.run(main())


    

