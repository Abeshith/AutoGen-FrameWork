from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client
from config.constants import MODEL

model_client = get_model_client()

def get_problem_solver_agent():
    """
    Initializes and returns the ProblemSolverAgent with the model client.
    """
    problem_solver_agent = AssistantAgent(
            name="ProblemSolverAgent",
            model_client=model_client,
            system_message="""You are a problem solver agent. Your task is to assist users in solving programming problems by providing code solutions
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
            8. Once everything is done, Ask the code executor agent to save the code in a file.
            Like this:
            ```python
            code = '''
                # Your code here
                print("Hello, World!")
            '''
            with open("solution.py", "w") as file:
                file.write(code)
            ```
            The filename should be determined according to the problem statement.
            like if the problem statement is about finding Armstrong numbers, the file name should be `armstrong_numbers.py`.
            Make sure the code in the block is properly formatted and executable.
            9. Once Above every steps are done, Provide the final solution in a single code block and You have to say "STOP"to stop the conversation.
            """,
        )
    print(f"ProblemSolverAgent initialized with model: {MODEL}")

    return problem_solver_agent