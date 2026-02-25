from datapizza.memory import Memory
from datapizza.type import TextBlock, ROLE
from openai_client import client


def ask(question: str, prompts=None, system_prompt: str = None, temperature = None, max_tokens = None) -> str:
    if prompts is not None:
        memory = Memory()
        for prompt in prompts:
            response = client.invoke(prompt, memory=memory)
            print("Responded with: " + response.text)
            memory.add_turn(TextBlock(content=prompt), role=ROLE.USER)
            memory.add_turn(response.content, role=ROLE.ASSISTANT)
        return client.invoke(
            input=question,
            temperature=temperature,
            max_tokens=max_tokens,
            system_prompt=system_prompt,
            memory=memory
        ).text
    else:
        return client.invoke(
            input=question,
            temperature=temperature,
            max_tokens=max_tokens,
            system_prompt=system_prompt
        ).text

def main():
    answer = ask(
        "What's my name?",
        prompts=[
            "My name is Francesco",
        ],
        max_tokens=50
    )
    print(answer)


if __name__ == '__main__':
    main()