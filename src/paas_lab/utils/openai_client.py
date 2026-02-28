import os
from dotenv import load_dotenv
from datapizza.clients.openai import OpenAIClient
from datapizza.embedders.openai import OpenAIEmbedder
from datapizza.clients.openai_like import OpenAILikeClient

load_dotenv()

GPT_MODEL = "gpt-4o-mini"
OPENAI_KEY = os.getenv("OPENAI_KEY")

openai_client = OpenAIClient(
    api_key=OPENAI_KEY,
    model=GPT_MODEL,
    # system_prompt="You are a helpful assistant",
    # temperature=0.7 # controls randomness (0-2)
)

regolo_client_120 = OpenAILikeClient(
    api_key=os.getenv("REGOLO_KEY"),
    model="gpt-oss-120b",
    base_url="https://api.regolo.ai/v1",
)

regolo_client_20 = OpenAILikeClient(
    api_key=os.getenv("REGOLO_KEY"),
    model="gpt-oss-20b",
    base_url="https://api.regolo.ai/v1",
)

embedder = OpenAIEmbedder(api_key=OPENAI_KEY, model_name="text-embedding-3-small")
