from datapizza.agents import Agent
from datapizza.tools import tool

from paas_lab.utils.openai_client import client
from weather.weather_service import get_weather as _get_weather


@tool
def get_weather(location: str, when: str) -> str:
    """Retrieves weather information for a specified location and time."""
    return _get_weather(location, when)

def simple_invoke(input: str) -> str:
    agent = Agent(name="weather_agent", tools=[get_weather], client=client)
    # `tool_choice` controls how the agent decides to use tools:
    # auto: the model will decide if use a tool or not.
    # required_first: force to use a tool only at the first step, then auto.
    # required: force to use a tool at every step.
    # none: force to not use any tool.
    response = agent.run(input, tool_choice="required_first")
    return response.text

def stream_invoke(input: str) -> list:
    agent = Agent(name="weather_agent", tools=[get_weather],
                  client=client)

    steps = []
    for step in agent.stream_invoke(input):
        print(f"Step {step.index} starting...")
        print(step.text)
        steps.append(step.text)

    return steps

def main():
    # print(simple_invoke("What's the weather tomorrow in Milan?"))
    print(stream_invoke("What's the weather tomorrow in Milan?"))

if __name__ == "__main__":
    main()
