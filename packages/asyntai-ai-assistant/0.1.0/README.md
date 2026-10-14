# Asyntai AI Assistant

[Asyntai](https://asyntai.com) is an AI chatbot for your website. It answers your visitors from your own pages, docs and FAQ. This package brings those answers into every text field on your computer: your email, your help desk, Slack, Word, a browser form.

Type `:ask`, write a question, and Espanso types the answer your chatbot gives, with the same facts, prices and links your visitors get.

## Triggers

- `:ask` opens a small form. Write a question, press Enter, and the answer is typed where your cursor is.
- `:clipask` answers the text on your clipboard. Copy a customer's question from an email or a ticket, type `:clipask` in your reply, and the answer is typed in.
- `:asyntaikey` saves your Asyntai API key. You do this one time.

Links in an answer are typed as `text (https://...)`, so they work in plain text fields too.

## Setup

1. Install the package:

   ```
   espanso install asyntai-ai-assistant
   ```

2. Sign in to [Asyntai](https://asyntai.com), open **Settings**, then **API**, and copy your API key.
3. Open an empty text field, for example a new note, and type `:asyntaikey`. Paste the key and press Enter. Asyntai checks the key, and the package saves it in your user folder (`%APPDATA%\asyntai` on Windows, `~/.config/asyntai` on macOS and Linux).
4. Type `:ask` anywhere and ask your first question.

The package is free. It uses the Asyntai API, which needs an Asyntai account on the Starter plan or higher.

## Requirements

- Espanso 2
- Windows: nothing else. The package uses Windows PowerShell, which every Windows 10 and 11 has.
- macOS and Linux: Python 3 (`python3`). The package uses only the Python standard library, so there is nothing to `pip install`. Your default shell must be sh, bash or zsh.

## Support

Documentation: https://asyntai.com/documentation/integrations/espanso/

Questions: hello@asyntai.com
