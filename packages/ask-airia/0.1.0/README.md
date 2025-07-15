# ask-airia

**ask-airia** is an [Espanso](https://espanso.org/) package that enables you to interact with [Airia Agents](https://airia.com) directly from your Espanso extension.

## Features

- Run Airia Agents from Espanso using custom triggers.
- Easily configure and manage multiple Airia Agents.

## Requirements

- **Python 3.8+** must be installed on your system.
- **python-dotenv** is required for environment variable management.
- **requests** is required to do HTTP requests to Airia

To install `python-dotenv`, run:
```
python3 -m pip install requests python-dotenv

```

## Installation

To install from espanso hub: 

```
espanso install ask-airia

```

1. **Configure your agents:**  
   Edit the `agent_config.json` file to add your Agent IDs and descriptions.  
   You can add or remove agents as needed following same structure

2. **Set up environment variables:**  
   Create a `.env` file in this folder and add your Airia domain and API key. Follow the `example.env` for more details

5. **Restart Espanso:**  
   Apply your changes by restarting Espanso:
   ```
   espanso restart
   ```
6. **Run the extension** 
    Use *"<ai"* to trigger this extension or modify the trigger from the `package.yml` file

    ```
    <ai

    ```

## Support

For more information, visit the [Espanso documentation](https://espanso.org/docs/) or [Airia](https://airia.com).

---


