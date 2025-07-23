from agents.code_executor_agent import GetCodeExecutorAgent
from agents.data_analyser_agent import GetDataAnalyzerAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from config.constants import MAX_TURNS, TERMINATATION_WORD
from autogen_agentchat.conditions import TextMentionTermination

def GetAnalyzerGPTTeam(docker, model_client):
    """
    Initializes and returns the AnalyzerGPT agent with a code executor.
    """
    
    code_executor_agent = GetCodeExecutorAgent(docker)

    data_analyser_agent = GetDataAnalyzerAgent(model_client)

    team = RoundRobinGroupChat(
        participants=[data_analyser_agent,code_executor_agent],
        max_turns=MAX_TURNS,
        termination_condition= TextMentionTermination(TERMINATATION_WORD)
    )

    print("AnalyzerGPT team initialized with DataAnalyserAgent and CodeExecutorAgent.")
    return team
    
