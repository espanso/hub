# ask-airia

**ask-airia** is an [Espanso](https://espanso.org/) package that enables you to interact with [Airia Agents](https://airia.com) directly from your Espanso extension.

## Features

- Run Airia Agents from Espanso using custom triggers.
- Easily configure and manage multiple Airia Agents.

## Installation

1. **Copy or clone this package** into your Espanso match packages directory:

    - On Linux:
      ```
      ~/.config/espanso/match/packages/
      ```
    - On macOS:
      ```
      ~/Library/Application Support/espanso/match/packages/
      ```

2. **Install dependencies:**  
   Ensure all packages listed in `requirements.txt` are installed and valid.

3. **Configure your agents:**  
   Edit the `agent_config.json` file to add your Agent IDs and descriptions.  
   You can add or remove agents as needed following same structure

4. **Set up environment variables:**  
   Create a `.env` file in this folder and add your Airia domain and API key. Follow the `example.env` for more details

5. **Restart Espanso:**  
   Apply your changes by restarting Espanso:
   ```
   espanso restart
   ```
6. **Run the extension** 
    Use *"<ai"* to trigger this extension or modify the trigger from the `package.yml` file

## Support

For more information, visit the [Espanso documentation](https://espanso.org/docs/) or [Airia](https://airia.com).

---


