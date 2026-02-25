import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_coordinates(location: str) -> dict:
    """Convert a location name to latitude and longitude using Open-Meteo geocoding API."""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": location, "count": 1, "language": "en", "format": "json"}
    response = requests.get(url, params=params)
    data = response.json()
    
    if not data.get("results"):
        return {"error": f"Location '{location}' not found."}
    
    result = data["results"][0]
    return {
        "name": result["name"],
        "country": result.get("country", ""),
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }


def get_weather(latitude: float, longitude: float, days: int = 3) -> dict:
    """Fetch current and forecast weather for given coordinates."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "precipitation", "weathercode", "windspeed_10m", "uv_index"],
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "weathercode", "uv_index_max", "windspeed_10m_max"],
        "forecast_days": days,
        "timezone": "auto"
    }
    response = requests.get(url, params=params)
    return response.json()


from smolagents import tool, CodeAgent
from smolagents.models import LiteLLMModel

# Wrap functions as smolagents tools
@tool
def get_coordinates_tool(location: str) -> dict:
    """
    Convert a location name into geographic coordinates.
    
    Args:
        location: City name or location string, e.g. 'Berlin' or 'Munich, Germany'
    
    Returns:
        Dictionary with name, country, latitude, and longitude
    """
    return get_coordinates(location)


@tool
def get_weather_tool(latitude: float, longitude: float, days: int = 3) -> dict:
    """
    Fetch current weather and multi-day forecast for a location.
    Returns temperature, precipitation, wind speed, UV index and weather codes.
    
    Args:
        latitude: Latitude coordinate of the location
        longitude: Longitude coordinate of the location
        days: Number of forecast days to retrieve (default 3, max 7)
    
    Returns:
        Dictionary with current weather and daily forecast data
    """
    return get_weather(latitude, longitude, days)


# System prompt — this is where the LLM gets its personality and instructions
SYSTEM_PROMPT = """You are a practical, friendly weather advisor. 

When a user asks about weather:
1. First get the coordinates for their location
2. Then fetch the weather data
3. Interpret the results in plain language
4. Always end with concrete recommendations: what to wear, what to bring, what to avoid

Be specific. Don't just say 'it might rain' — say 'bring an umbrella, there's 8mm of rain expected'.
Use the weathercode to describe conditions (0=clear, 1-3=partly cloudy, 61-67=rain, 71-77=snow, 95=thunderstorm).
"""

# Initialize model and agent
model = LiteLLMModel(
    model_id="anthropic/claude-haiku-4-5-20251001",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

agent = CodeAgent(
    tools=[get_coordinates_tool, get_weather_tool],
    model=model,
)

# Run it
if __name__ == "__main__":
    user_query = """You are a practical, friendly weather advisor.
When answering, always:
1. Get coordinates for the location
2. Fetch the weather data
3. Interpret results in plain language
4. End with concrete recommendations: what to wear, what to bring, what to avoid
Be specific - don't say 'it might rain', say 'bring an umbrella, 8mm of rain expected'.
Use weathercode to describe conditions (0=clear, 1-3=partly cloudy, 61-67=rain, 71-77=snow, 95=thunderstorm).

User question: Can I go sailing from port of Glueckstadt to Sylt this weekend?"""
    
    print(f"\nQuery: Can I go sailing from port of Glueckstadt to Sylt this weekend?\n")
    response = agent.run(user_query)
    print("\nAgent response:", response)