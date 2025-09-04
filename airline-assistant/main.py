import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

# Load config from .env file
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("OPENROUTER_MODEL", "meta-llama/llama-3.1-8b-instruct")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is not set in the environment variables.")
# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

# System persona and fake database
system_message = """"You are a helpful assistant for an Airline called FlightAI. "
    "Give short, courteous answers, no more than 1 sentence. "
    "Always be accurate. If you don't know the answer, say so. "
    "If a customer asks for a ticket price, use the ticket price tool."""

# Fake database of ticket prices
ticket_prices = {
    "london": "$799",
    "paris": "$899",
    "tokyo": "$1400",
    "berlin": "$499",
}

def get_ticket_price(destination_city: str) -> str:
    """Our real Python function (the tool)."""
    print(f"[tool] get_ticket_price({destination_city})")
    city = (destination_city or "").strip().lower()
    return ticket_prices.get(city, "Unknown")

# Tool schema
price_function_schema = {
    "name": "get_ticket_price",
    "description": (
        "Get the price of a return ticket to the destination city. "
        "Call this whenever the user asks for the price to a specific city."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city the customer wants to travel to (e.g., 'Tokyo').",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False,
    },
}

tools = [
    {"type": "function", "function": price_function_schema}
]

# Tool-call handler
def handle_tool_call(message):
    """Executes the function requested by the model and returns a 'tool' message."""
    tool_call = message.tool_calls[0]  # handle single-tool call
    fn_name = tool_call.function.name
    args = json.loads(tool_call.function.arguments or "{}")

    if fn_name == "get_ticket_price":
        city = args.get("destination_city", "")
        price = get_ticket_price(city)
        tool_response = {"destination_city": city, "price": price}
    else:
        tool_response = {"error": f"Unknown tool: {fn_name}"}

    # This is how you return tool outputs to the model
    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(tool_response),
    }

# chat function
def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [
        {"role": "user", "content": message}
    ]

    # Ask the model
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
    )

    choice = response.choices[0]
    msg = choice.message

    # 🔍 Debug
    print("DEBUG: choice.finish_reason =", choice.finish_reason)
    print("DEBUG: msg =", msg)

    # If model is calling a tool
    if getattr(msg, "tool_calls", None):
        tool_message = handle_tool_call(msg)

        messages.append(msg)           # the tool request
        messages.append(tool_message)  # our tool response

        # Ask model again to generate final reply
        final = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )
        return final.choices[0].message.content

    # Otherwise just return normal text
    return msg.content if msg.content else "(No response)"


#  UI

demo = gr.ChatInterface(
    fn=chat,
    type="messages",
    title="🛫 FlightAI – Airline Assistant",
    description="Ask about tickets, destinations, or prices (e.g., 'How much is a return ticket to Tokyo?')"
)

if __name__ == "__main__":
    demo.launch()