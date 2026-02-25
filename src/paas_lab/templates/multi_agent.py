from datapizza.agents.agent import Agent
from datapizza.tools import tool
from weather.weather_service import get_weekly_weather

from paas_lab.utils.openai_client import client


@tool
def get_weather(city: str) -> str:
    return get_weekly_weather(city)


def main():
    weather_agent = Agent(
        name="weather_expert",
        client=client,
        system_prompt="You are a weather expert. Provide detailed weather information and forecasts.",
        tools=[get_weather]
    )

    planner_agent = Agent(
        name="planner",
        client=client,
        system_prompt="You are a trip planner. Use weather and analysis info to make recommendations."
    )

    planner_agent.can_call(weather_agent) # Allow planner_agent to call weather_agent for information

    response = planner_agent.run(
        "I need to plan a hiking trip in Seattle next week. Can you help analyze the weather and make recommendations?"
    )
    print(response.text)

if __name__ == "__main__":
    main()