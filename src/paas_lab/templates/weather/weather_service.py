import json
import urllib.request
from urllib.parse import quote
from datetime import datetime, timedelta


def get_weekly_weather(location: str) -> str:
    """
    Retrieves weather forecast for the next 7 days for a specified location.
    Returns a formatted string with daily weather information.
    """
    # Encode location safely for URL
    encoded_location = quote(location)

    # Get geocoding data for the location
    geo_url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={encoded_location}&count=1&language=en&format=json"
    )

    with urllib.request.urlopen(geo_url) as geo_resp:
        geo_data = json.load(geo_resp)

    if not geo_data.get("results"):
        return f"Location '{location}' not found."

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]
    location_name = geo_data["results"][0]["name"]

    # Get weather forecast for the next 7 days
    wx_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode"
        f"&timezone=auto"
    )

    with urllib.request.urlopen(wx_url) as wx_resp:
        wx_data = json.load(wx_resp)

    # Format the response
    daily = wx_data["daily"]
    result = [f"Weather forecast for {location_name} - Next 7 days:\n"]

    for i in range(7):
        date = daily["time"][i]
        temp_max = daily["temperature_2m_max"][i]
        temp_min = daily["temperature_2m_min"][i]
        precipitation = daily["precipitation_sum"][i]

        # Parse and format the date
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        day_name = date_obj.strftime("%A")

        result.append(
            f"{day_name}, {date}: "
            f"Max {temp_max}°C, Min {temp_min}°C, "
            f"Precipitation: {precipitation}mm"
        )

    return "\n".join(result)


def get_weather(location: str, when: str) -> str:
    """
    Retrieves current weather information for a specified location and time.
    This is the original function for compatibility with existing code.
    """
    # Encode location safely for URL
    encoded_location = quote(location)

    geo_url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={encoded_location}&count=1&language=en&format=json"
    )

    with urllib.request.urlopen(geo_url) as geo_resp:
        geo_data = json.load(geo_resp)

    if not geo_data.get("results"):
        return f"Location '{location}' not found."

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    wx_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current=temperature_2m"
    )

    with urllib.request.urlopen(wx_url) as wx_resp:
        wx_data = json.load(wx_resp)

    return f"{wx_data['current']['temperature_2m']} °C"