#!/usr/bin/env python3
"""
Random Discord Formatter for Espanso
Minimal GUI: type text, hit Return or OK → prints formatted result to stdout and exits.
Cancel exits with no output.
"""

import tkinter as tk
from tkinter import messagebox
import random
import re
import sys

FORMATTERS = [
    lambda s: s,
    lambda s: f"**{s}**",
    lambda s: f"*{s}*",
    lambda s: f"***{s}***",
    lambda s: f"__{s}__",
    lambda s: f"**__{s}__**",
    lambda s: f"*__{s}__*",
    lambda s: f"~~{s}~~",
    lambda s: f"**~~{s}~~**",
    lambda s: f"*~~{s}~~*",
    lambda s: f"`{s}`",
    lambda s: f"||{s}||",
]

def random_case_word(word: str) -> str:
    return "".join(
        c.swapcase() if c.isalpha() and random.random() < 0.5 else c
        for c in word
    )

def apply_random_discord(text: str) -> str:
    if not text.strip():
        return text
    parts = re.split(r'(\s+)', text)
    result = []
    for part in parts:
        if not part or part.isspace():
            result.append(part)
            continue
        word = random_case_word(part)
        if random.random() < 0.7:
            word = random.choice(FORMATTERS)(word)
        result.append(word)
    return "".join(result)

class App:
    def __init__(self, root):
        self.root = root
        root.title("Discord Format")
        root.geometry("420x140")
        root.resizable(False, False)

        # Center-ish and stay on top
        root.attributes("-topmost", True)
        root.after(100, lambda: root.attributes("-topmost", False))

        tk.Label(root, text="Text:").pack(anchor="w", padx=10, pady=(10, 0))

        self.entry = tk.Text(root, height=3, wrap=tk.WORD)
        self.entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.entry.focus_set()

        btn_frame = tk.Frame(root)
        btn_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Button(btn_frame, text="OK", width=10, command=self.ok).pack(side=tk.RIGHT, padx=5)
        tk.Button(btn_frame, text="Cancel", width=10, command=self.cancel).pack(side=tk.RIGHT)

        # Return and Ctrl+Return both submit
        self.entry.bind("<Return>", self.on_return)
        self.entry.bind("<Control-Return>", self.on_return)
        root.bind("<Escape>", lambda e: self.cancel())

        root.protocol("WM_DELETE_WINDOW", self.cancel)

    def on_return(self, event):
        # Allow Shift+Return for newline, plain Return submits
        if event.state & 0x1:  # Shift held
            return
        self.ok()
        return "break"

    def ok(self):
        raw = self.entry.get("1.0", tk.END).rstrip("\n")
        if not raw.strip():
            messagebox.showinfo("Empty", "Enter some text first.", parent=self.root)
            return
        result = apply_random_discord(raw)
        print(result, flush=True)
        self.root.destroy()

    def cancel(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
    sys.exit(0)
