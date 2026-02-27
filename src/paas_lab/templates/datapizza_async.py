import asyncio

from paas_lab.utils.openai_client import client


async def a_ask(
    question: str, system_prompt: str = None, temperature=None, max_tokens=None
) -> str:
    response = await client.a_invoke(
        input=question,
        temperature=temperature,
        max_tokens=max_tokens,
        system_prompt=system_prompt,
    )
    return response.text


def main():
    answer = asyncio.run(
        a_ask(
            "Tell me a brief peculiarity of each planet in the solar system",
            system_prompt="You are a astro-physics professor",
            max_tokens=200,
        )
    )
    print(answer)


if __name__ == "__main__":
    main()
