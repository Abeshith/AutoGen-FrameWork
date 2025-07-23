from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.settings import GOOGLE_API_KEY, MODEL, MAX_TURNS, TERMINATATION_WORD

model_client = OpenAIChatCompletionClient(
    model=MODEL,
    api_key=GOOGLE_API_KEY,
)