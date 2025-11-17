import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

if len(sys.argv) < 2:
    print("Error: You must provide a prompt as a command line argument.")
    print('Example: uv run main.py "Why are episodes 7-9 so much worse than 1-6?"')
    sys.exit(1)

user_prompt = sys.argv[1]

verbose = False 
if "--verbose" in sys.argv:
    verbose = True

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages)

print(response.text)

usage = response.usage_metadata
prompt_tokens = usage.prompt_token_count
response_tokens = usage.candidates_token_count

if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")

def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
