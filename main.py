import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

def main():
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    client = genai.Client(api_key = api_key)

    parser = argparse.ArgumentParser(description='AI Agent')
    parser.add_argument("user_prompt", type=str, help='Model to use')
    parser.add_argument("--verbose", action = "store_true", help = "open/close verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages
    )

    if (response.usage_metadata == None):
        raise RuntimeError("Usage metadata is None")
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if args.verbose:
        print(f"User pdrompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    print(response.text)

if __name__ == "__main__":
    main()
