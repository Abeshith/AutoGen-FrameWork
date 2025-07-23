from config.settings import GOOGLE_API_KEY, MODEL, MAX_TURNS, TERMINATATION_WORD
from autogen_agentchat.teams import RoundRobinGroupChat
from utils.utilities import save_state, load_state, get_termination_condition
from agents.planner import planner_agent
from agents.researcher import researcher_agent

team = RoundRobinGroupChat(
    participants=[planner_agent, researcher_agent],
    termination_condition = get_termination_condition(),
    max_turns=MAX_TURNS,
)
