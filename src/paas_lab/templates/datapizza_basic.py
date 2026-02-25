from openai_client import client


def ask(question: str, system_prompt: str = None, temperature = None, max_tokens = None) -> str:
    response = client.invoke(
        input=question,
        temperature=temperature,
        max_tokens=max_tokens,
        system_prompt=system_prompt
    )

    return response.text

def main():
    print(ask(
        "Explain quantum computing in simple terms",
        system_prompt="You are a physics professor"
    ))

if __name__ == '__main__':
    main()