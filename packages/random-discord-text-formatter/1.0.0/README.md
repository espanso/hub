# Random Discord Formatter

Minimal Python helper that takes text from an Espanso form, randomly applies Discord markdown (bold, italic, underline, strikethrough, code, spoiler, and combos) plus random case flipping, then prints the result to stdout so Espanso can paste it.

## What it does

- Prompts via Espanso form (multiline text field).
- Splits the input on whitespace (keeps spaces intact).
- Randomly flips the case of each letter (~50% chance).
- Wraps each word in one random Discord style.
- Prints the result to stdout.

Because formatting is applied per whole word and spaces stay between the markers, Discord parses it correctly (no stray asterisks).

## Usage

1. Type `:randytext`.
2. Espanso shows a form with a multiline text field.
3. Enter your text and submit (Submit button or Ctrl+Enter).
4. The formatted result is pasted.

## Requirements

- Python 3

## Files

- `random_discord_text_formatter.py` — the script
- `package.yml` — Espanso match + form definition
- `_manifest.yml` — package metadata

## Notes

- Formatting styles: bold, italic, bold italic, underline, bold underline, italic underline, strikethrough, bold strikethrough, italic strikethrough, inline code, spoiler.
- Case flipping only affects letters.
- Empty form submission produces no output.
- The script path in `package.yml` uses `%CONFIG%` so it resolves correctly after package installation.
