#!/usr/bin/env python

"""
ask-ai.py: Query a local or remote LLM (Large Language Model) using the OpenAI API interface and return the response.

Author: Bernhard Enders
Date: 2025-06-13
Version: 0.1.0

Description:
    This script is designed for integration with Espanso, allowing users to send a prompt to an LLM and receive a direct answer, suitable for text expansion workflows.

Features:
    - Loads configuration (API key, base URL, model) from a .env file in the script directory.
    - Sends the user-provided prompt to the LLM with a system message enforcing non-interactive, assumption-based responses.
    - Prints the LLM's response to stdout for Espanso to capture.
    - Handles errors gracefully and provides clear error messages if configuration or API calls fail.

Usage:
    python ask-ai.py "<text>"

Requirements:
    - openai
    - python-dotenv
    - Python 3.9+

"""


import os
from openai import OpenAI
from dotenv import load_dotenv
import sys

sys.stdout.reconfigure(encoding="utf-8")

def ask_ai(text: str) -> str:
    """
    Sends a prompt to a local or remote LLM using the OpenAI API interface and returns the response.

    Args:
        text (str): The user prompt to send to the LLM.

    Returns:
        str: The LLM's response or an error message.
    """
    # Load .env file from the same directory as the script
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)

    # Get API key from .env file
    api_key = os.getenv("API_KEY")
    if not api_key:
        return "❌ Error: API_KEY variable not found in .env file"

    base_url = os.getenv("BASE_URL", "http://localhost:11434/v1")
    if not base_url:
        return "❌ Error: BASE_URL variable not found in .env file"

    model = os.getenv("MODEL")
    if not model:
        return "❌ Error: MODEL variable not found in .env file"

    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    try:
        # API call with stream=False
        response = client.chat.completions.create(
            model=model,
            messages=[
            {
                "role": "system",
                "content": (
                    "You are operating in a non-interactive mode.\n"
                    "Do NOT use introductory phrases, greetings, or opening messages.\n"
                    "You CANNOT ask the user for clarification, additional details, or preferences.\n"
                    "When given a request, make reasonable assumptions based on the context and provide a complete, helpful response immediately.\n"
                    "If a request is ambiguous, choose the most common or logical interpretation and proceed accordingly.\n"
                    "Always deliver a substantive response rather than asking questions.\n"
                    "NEVER ask the user for follow-up questions or clarifications."
                ),
            },
            {
                "role": "user",
                "content": text,
            },
            ],
            stream=False,
        )

        answer = response.choices[0].message.content.strip()
        return answer

    except Exception as e:
        error_message = str(e)
        return f"❌ Error: {error_message}"

def main():
    """
    Main entry point for the script. Parses arguments, validates input, calls ask_ai, and prints the result.
    """
    # check for required arguments
    if len(sys.argv) != 2:
        print('⚠ Usage: python ask-ai.py "<text>"')
        sys.exit(1)

    text = sys.argv[1]

    # validate inputs
    if not text.strip():
        print("❌ Error: No text/prompt provided")
        sys.exit(1)

    # perform the llm api call
    result = ask_ai(text)

    # output result (this gets captured by Espanso)
    print(result)


if __name__ == "__main__":
    main()
