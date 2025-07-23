from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from config.settings import TERMINATATION_WORD
import json



def save_state(agent, filename):
    """Saves the state of the agent to a JSON file."""
    try:
        state = agent.save_state()
        with open(filename,'w') as f:
            json.dump(state, f)
    except Exception as e:
        print(f"Error saving state: {e}")
        

def load_state(agent, filename):
    """Loads the state of the agent from a JSON file."""
    try:
        with open(filename, 'r') as f:
            state = json.load(f)
        agent.load_state(state)
    
    except Exception as e:
        print(f"Error loading state: {e}")


def get_termination_condition():
    """Returns the termination condition for the team."""
    termination = TextMentionTermination(TERMINATATION_WORD)
    print(f"Termination condition set to: {TERMINATATION_WORD}")

    return termination