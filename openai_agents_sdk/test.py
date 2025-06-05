from agents import Agent, Runner
from dotenv import load_dotenv
import asyncio


load_dotenv()



async def test_installation():
    agent = Agent(
        name="Test Agent",
        instructions="You are a helpful assistant that provides concise responses."
    )
    result = await Runner.run(agent, "Hello! Are you working correctly?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(test_installation())

#Hello! Yes, I'm here and ready to help. How can I assist you today?