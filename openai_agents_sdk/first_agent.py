from agents import Agent, Runner
from dotenv import load_dotenv
from agents import ModelSettings
import asyncio

# Load environment variables (API key)
load_dotenv()

# Define detailed instructions for our weather assistant
weather_instructions = """
You are a weather information assistant who helps users understand weather patterns and phenomena.

YOUR EXPERTISE:
- Explaining weather concepts and terminology
- Describing how different weather systems work
- Answering questions about climate and seasonal patterns
- Explaining the science behind weather events

LIMITATIONS:
- You cannot provide real-time weather forecasts for specific locations
- You don't have access to current weather data
- You should not make predictions about future weather events

STYLE:
- Use clear, accessible language that non-meteorologists can understand
- Include interesting weather facts when relevant
- Be enthusiastic about meteorology and climate science
"""

# Create our specialized weather assistant
weather_assistant = Agent(
   name="WeatherWise",
   instructions=weather_instructions,
   model="gpt-3.5-turbo",
   model_settings=ModelSettings(
       temperature=0.5,  # Balanced temperature for natural but focused responses
       max_tokens=256,  # Maximum length of response
   )
)

async def run_agent_example():
   result = await Runner.run(weather_assistant, "Can you tell me about the relationship between climate change and extreme weather events?")
   print(result.final_output)

if __name__ == "__main__":
   asyncio.run(run_agent_example())