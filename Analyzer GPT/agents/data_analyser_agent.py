from autogen_agentchat.agents import AssistantAgent
from config.constants import MODEL
from prompts.data_analyser_prompt import DATA_ANALYSER_PROMPT


def GetDataAnalyzerAgent(model_client):
    """
    Initializes and returns the AnalyzerGPT agent with a code executor.
    """    
    analyzer_agent = AssistantAgent(
        name="DataAnalyzerAgent",
        model_client=model_client,
        system_message=DATA_ANALYSER_PROMPT
    )
    
    print("AnalyzerGPT agent initialized with CodeExecutorAgent.")
    
    return analyzer_agent