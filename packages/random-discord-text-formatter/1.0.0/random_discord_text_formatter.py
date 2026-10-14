#!/usr/bin/env python3
"""
Random Discord Formatter for Espanso
Reads text from the Espanso form (via ESPANSO_FORM1_TEXT),
applies random Discord markdown + case flipping, and prints the result.
"""

import os
import random
import re
import sys

FORMATTERS = [
    lambda s: f"**{s}**",          # bold
    lambda s: f"*{s}*",            # italic
    lambda s: f"***{s}***",        # bold italic
    lambda s: f"__{s}__",          # underline
    lambda s: f"**__{s}__**",      # bold underline
    lambda s: f"*__{s}__*",        # italic underline
    lambda s: f"~~{s}~~",          # strikethrough
    lambda s: f"**~~{s}~~**",      # bold strikethrough
    lambda s: f"*~~{s}~~*",        # italic strikethrough
    lambda s: f"`{s}`",            # inline code
    lambda s: f"||{s}||",          # spoiler
]

def random_case_word(word: str) -> str:
    """Randomly flip case of each letter (~50% chance)."""
    return "".join(
        c.swapcase() if c.isalpha() and random.random() < 0.5 else c
        for c in word
    )

def apply_random_discord(text: str) -> str:
    """
    Split on whitespace (preserve spaces), randomly case-flip letters,
    then wrap each word in one Discord style.
    """
    if not text or not text.strip():
        return ""
    parts = re.split(r"(\s+)", text)
    result = []
    for part in parts:
        if not part or part.isspace():
            result.append(part)
            continue
        word = random_case_word(part)
        formatter = random.choice(FORMATTERS)
        result.append(formatter(word))
    return "".join(result)

def main() -> None:
    # Form field "text" is exposed as ESPANSO_FORM1_TEXT
    raw = os.environ.get("ESPANSO_FORM1_TEXT", "").strip()
    if not raw:
        # Empty form → nothing to expand
        sys.exit(0)
    print(apply_random_discord(raw), flush=True)

if __name__ == "__main__":
    main()
