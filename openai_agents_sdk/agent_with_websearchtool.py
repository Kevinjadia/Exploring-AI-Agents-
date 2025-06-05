from agents import Agent, Runner, WebSearchTool
from dotenv import load_dotenv
import asyncio


load_dotenv()

# Create a research assistant with web search capability
research_assistant = Agent(
   name="Research Assistant",
   instructions="""You are a research assistant that helps users find and summarize information.
   When asked about a topic:
   1. Search the web for relevant, up-to-date information
   2. Synthesize the information into a clear, concise summary
   3. Structure your response with headings and bullet points when appropriate
   4. Always cite your sources at the end of your response
  
   If the information might be time-sensitive or rapidly changing, mention when the search was performed.
   """,
   tools=[WebSearchTool()]
)

async def research_topic(topic):
   result = await Runner.run(research_assistant, f"Please research and summarize: {topic}. Only return the found links with very minimal text.")
   print(result.final_output)

if __name__ == "__main__":
   asyncio.run(research_topic("Latest developments in personal productivity apps."))
