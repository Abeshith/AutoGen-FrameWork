import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL, MAX_TURNS, TERMINATATION_WORD, WORK_DIR, TIMEOUT

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def get_model_client():
    model_client = OpenAIChatCompletionClient(
        model=MODEL,
        api_key=api_key
    )
    print(f"Model client initialized with model: {MODEL}")
    return model_client


