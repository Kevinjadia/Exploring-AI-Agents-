from agents import Agent, handoff, RunContextWrapper
from datetime import datetime
import asyncio 

from dotenv import load_dotenv
load_dotenv()

# Create an agent that handles account-related questions
from agents import Agent, Runner
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


account_agent = Agent(
   name="Account Management",
   instructions="""You help customers with account-related issues such as
   password resets, account settings, and profile updates.""",
)


# Custom handoff callback function
async def log_account_handoff(ctx: RunContextWrapper[None]):
   print(
       f"[LOG] Account handoff triggered at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
   )
   # In a real app, you might log to a database or alert a human supervisor


# Create a triage agent with customized handoffs
enhanced_triage_agent = Agent(
   name="Enhanced Customer Service",
   instructions="""You are the initial customer service contact who directs
   customers to the right specialist.
  
   If the customer has billing or payment questions, hand off to the Billing Agent.
   If the customer has technical problems, hand off to the Technical Agent.
   If the customer needs to change account settings, hand off to the Account Management agent.
   For general inquiries, you can answer directly.""",
   handoffs=[
       billing_agent,  # Basic handoff
       handoff(  # Customized handoff
           agent=account_agent,
           on_handoff=log_account_handoff,  # Callback function
           tool_name_override="escalate_to_account_team",  # Custom tool name
           tool_description_override="Transfer the customer to the account management team for help with account settings, password resets, etc.",
       ),
       technical_agent,  # Basic handoff
   ],
)

async def handle_customer_request(request):
   runner = Runner()
   result = await runner.run(enhanced_triage_agent, request)
   return result

result = asyncio.run(
   handle_customer_request("I need to change my password.")
)
