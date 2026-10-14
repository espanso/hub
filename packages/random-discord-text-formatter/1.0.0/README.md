# Random Discord Formatter

Minimal Tkinter helper that takes text, randomly applies Discord markdown (bold, italic, underline, strikethrough, code, spoiler, and combos) plus random case flipping, then prints the result to stdout.

Designed to be launched from [Espanso](https://espanso.org/) so the formatted text gets pasted automatically.

## What it does

- Splits the input on whitespace (keeps spaces intact).
- Randomly flips the case of each letter (~50% chance).
- Wraps each word in one random Discord style (~70% chance; otherwise leaves it plain).
- Prints the result to stdout and exits.

Because formatting is applied per whole word and spaces stay between the markers, Discord parses it correctly (no stray asterisks).

## Espanso setup

Trigger: `:randytext`

Example snippet (adjust the path to wherever you keep the script):

```yaml
- trigger: ":randytext"
  replace: "{{output}}"
  force_mode: clipboard
  vars:
    - name: output
      type: shell
      params:
        cmd: "python3 /path/to/random_discord_formatter.py"
```

`force_mode: clipboard` is recommended so multi-line results paste cleanly into Discord and other Electron apps.

## Usage

1. Type `:randytext` and hit your Espanso trigger key.
2. A small window appears.
3. Type your text.
   - **Return** or **OK** → formats it, prints to stdout, closes.
   - **Shift+Return** → inserts a newline.
   - **Cancel** / **Escape** / window close → exits with no output.
4. Espanso pastes the result.

## Requirements

- Python 3 with Tkinter (usually included; on some Linux distros you may need the `python3-tk` package).

## Files

- `random_discord_formatter.py` — the script

## Notes

- Formatting styles used: plain, bold, italic, bold italic, underline, bold underline, italic underline, strikethrough, bold strikethrough, italic strikethrough, inline code, spoiler.
- Case flipping only affects letters.
- Empty input shows a message and stays open so you can try again.
