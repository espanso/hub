# Random Discord Formatter

Minimal Python helper that takes text, randomly applies Discord markdown (bold, italic, underline, strikethrough, code, spoiler, and combos) plus random case flipping, then prints the result to stdout.

Designed to be launched from [Espanso](https://espanso.org/) so the formatted text gets pasted automatically.

## What it does

- Splits the input on whitespace (keeps spaces intact).
- Randomly flips the case of each letter (~50% chance).
- Wraps each word in one random Discord style (~70% chance; otherwise leaves it plain).
- Prints the result to stdout and exits.

Because formatting is applied per whole word and spaces stay between the markers, Discord parses it correctly (no stray asterisks).

## Usage

1. Type `:randytext`.
2. A small window appears.
3. Type your text.
4. Espanso pastes the result.

## Requirements

- Python

## Files

- `random_discord_text_formatter.py` — the script

## Notes

- Formatting styles used: plain, bold, italic, bold italic, underline, bold underline, italic underline, strikethrough, bold strikethrough, italic strikethrough, inline code, spoiler.
- Case flipping only affects letters.
- Empty input shows a message and stays open so you can try again.

