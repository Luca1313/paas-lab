from datapizza.clients.openai_like import OpenAILikeClient

client = OpenAILikeClient(
    api_key="",  # Ollama doesn't require an API key
    model="deepseek-r1:8b",
    base_url="http://localhost:11434/v1",
    # system_prompt=".",
)

response = client.invoke("What is the capital of France?")
print(response.content)
