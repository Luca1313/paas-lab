import os
from dotenv import load_dotenv
from datapizza.clients.openai import OpenAIClient
from datapizza.embedders.openai import OpenAIEmbedder

load_dotenv()

GPT_MODEL = "gpt-4o-mini"
OPENAI_KEY = os.getenv("OPENAI_KEY")

openai_client = OpenAIClient(
    api_key=OPENAI_KEY,
    model=GPT_MODEL,
    # system_prompt="You are a helpful assistant",
    # temperature=0.7 # controls randomness (0-2)
)

embedder = OpenAIEmbedder(api_key=OPENAI_KEY, model_name="text-embedding-3-small")
