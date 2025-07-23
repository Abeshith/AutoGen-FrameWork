from agents.code_executor import get_code_executor_agent
from agents.problem_solver import get_problem_solver_agent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from config.constants import TERMINATATION_WORD, MAX_TURNS


def create_dsa_solver_team():
    """
    Creates the DSA solver team with problem solver and code executor agents.
    """
    problem_solver_agent = get_problem_solver_agent()
    code_executor_agent, docker = get_code_executor_agent()

    team = RoundRobinGroupChat(
        participants=[problem_solver_agent, code_executor_agent],
        termination_condition=TextMentionTermination(TERMINATATION_WORD),
        max_turns=MAX_TURNS,
    )
    print("DSA Solver team created with ProblemSolverAgent and CodeExecutorAgent.")
    return team, docker