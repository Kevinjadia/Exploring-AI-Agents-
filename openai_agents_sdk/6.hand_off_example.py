from agents import Agent, handoff, Runner
from dotenv import load_dotenv
import asyncio

load_dotenv()

# Create specialist agents
billing_agent = Agent(
   name="Billing Agent",
   instructions="""You are a billing specialist who helps customers with payment issues.
   Focus on resolving billing inquiries, subscription changes, and refund requests.
   If asked about technical problems or account settings, explain that you specialize
   in billing and payment matters only.""",
)

technical_agent = Agent(
   name="Technical Agent",
   instructions="""You are a technical support specialist who helps with product issues.
   Assist users with troubleshooting, error messages, and how-to questions.
   Focus on resolving technical problems only.""",
)

# Create a triage agent that can hand off to specialists
triage_agent = Agent(
   name="Customer Service",
   instructions="""You are the initial customer service contact who helps direct
   customers to the right specialist.
  
   If the customer has billing or payment questions, hand off to the Billing Agent.
   If the customer has technical problems or how-to questions, hand off to the Technical Agent.
   For general inquiries or questions about products, you can answer directly.
  
   Always be polite and helpful, and ensure a smooth transition when handing off to specialists.""",
   handoffs=[billing_agent, technical_agent],  # Direct handoff to specialist agents
)

async def handle_customer_request(request):
   runner = Runner()
   result = await runner.run(triage_agent, request)
   return result


# Example customer inquiries
billing_inquiry = (
   "I was charged twice for my subscription last month. Can I get a refund?"
)
technical_inquiry = (
   "The app keeps crashing when I try to upload photos. How can I fix this? Give me the shortest solution possible."
)
general_inquiry = "What are your business hours?"

# Process the different types of inquiries
billing_response = asyncio.run(handle_customer_request(billing_inquiry))
print(f"Billing inquiry response:\n{billing_response.final_output}\n")

technical_response = asyncio.run(handle_customer_request(technical_inquiry))
print(f"Technical inquiry response:\n{technical_response.final_output}\n")

general_response = asyncio.run(handle_customer_request(general_inquiry))
print(f"General inquiry response:\n{general_response.final_output}")
