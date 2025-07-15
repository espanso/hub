'''
ask-airia.py
This script is designed to interact with Airia Agents and get a response based on a user-provided prompt.

Author: Carles Ferrater
Date: 2025-07-07
Version: 0.1.0

Description:
    This script is designed for integration with Espanso, allowing users to send a prompt to a Airia Agents and receive a direct answer.

Features:
    - Loads configuration (API key, base URL, model) from a .env file in the script directory.
    - Allows user to select an existing Airia Agent.
    - Sends the user-provided prompt to the Airia Agents.
    - Prints the Airia Agents's response to stdout for Espanso to capture.

Suggested Prompt:


'''
import os
import sys
import json
import requests
from dotenv import load_dotenv


def load_info():
    """
    Loads environment variables from a .env file.
    If the file does not exist, it raises a FileNotFoundError.
    """
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if not os.path.exists(env_path):
        raise FileNotFoundError(f"❌ Error: Missing .env file in directory: '{os.path.dirname(__file__)}'.")
    load_dotenv(env_path)

    if not os.getenv("AIRIA_API_KEY"):
        raise ValueError("❌ Error: AIRIA_API_KEY is not set in the .env file.")
    global API_KEY
    API_KEY = os.getenv("AIRIA_API_KEY")

    if not os.getenv("BASE_URL"):
        raise ValueError("❌ Error: BASE_URL is not set in the .env file.")
    global BASE_URL
    BASE_URL = os.getenv("BASE_URL")
    

def get_agent_id(agent_name: str) -> str:
    """
    Retrieves the agent ID for a given agent name from the configuration file.
    
    Args:
        agent_name (str): The name of the Airia Agent.
    
    Returns:
        str: The ID of the Airia Agent.
    
    Raises:
        ValueError: If the agent name is not found in the configuration.
    """
    script_dir = os.path.dirname(__file__)
    config_path = os.path.join(script_dir, "agent_config.json")
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"❌ Error: Missing agent configuration file in directory: '{script_dir}'.")

    with open(config_path, 'r') as f:
        agents = json.load(f)

    for agent in agents:
        if agent['name'] == agent_name:
            return agent['id']
    
    raise ValueError(f"❌ Error: Agent '{agent_name}' not found in configuration.")
    

def ask_airia(prompt: str, agent_name: str) -> str:
    """
    Sends a prompt to the Airia Agent and returns the response.
    
    Args:
        prompt (str): The user-provided prompt.
        agent_id (str): The ID of the Airia Agent to use.
    
    Returns:
        str: The response from the Airia Agent.
    """
    agent_id = get_agent_id(agent_name)
    load_info()
    headers = {
        "X-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }    
    data = {
        "userInput": prompt,
        "asyncOutput": False,
    }
    response = requests.post(
        f"{BASE_URL}/v2/PipelineExecution/{agent_id}",
        headers=headers,
        json=data
    )
    
    if response.status_code != 200:
        raise Exception(f"❌ Error: Failed to get response from Airia Agent. Status code: {response.status_code}, Message: {response.text}")
    
    response_data = response.json()
    return(response_data['result'])
    #print(agent_id)


def main() -> None:
    """
    Main entry point for the script. Parses arguments, validates input, calls ask_ai, and prints the result.
    """
    if len(sys.argv) != 3:
        print('❌ Usage error: python ask-airia.py "<agent-name>" "<input>"')
        return
    input = sys.argv[2]
    if not input.strip():
        print("❌ Error: No prompt text provided!")
        return
    agent_name = sys.argv[1]
    if not agent_name.strip():
        print("❌ Error: No agent NAME provided!")
        return

    
    print(ouptput := ask_airia(input, agent_name))


if __name__ == "__main__":
    main()