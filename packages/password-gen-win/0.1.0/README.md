# Password Generator (Windows)

A powerful, zero-dependency Espanso package for generating random passwords instantly. Designed specifically for Windows, it leverages native PowerShell to generate secure strings, paste them into your active window, and automatically save them to your clipboard.

## Features

- ✨ **Smart Triggers**: Specify your desired length directly in the trigger.
- 📋 **Auto-Clipboard**: Every generated password is automatically copied to your Windows clipboard for easy use in secondary fields (like "Confirm Password").
- 🔒 **Secure**: Generates unpredictable strings using native system libraries.
- 🚀 **Zero Dependencies**: Works out-of-the-box on Windows using built-in PowerShell.

---

## How to Use

Simply type a trigger followed by the **2-digit length** you want.

> **Important:** The length must always be **two digits**. For lengths less than 10, use a leading zero (e.g., `08` instead of `8`).

### 1. Available Triggers

| Trigger        | Complexity   | Character Set                             | Example  |
| :------------- | :----------- | :---------------------------------------- | :------- |
| `:pw[length]`  | **Standard** | Letters (A-Z, a-z) + Numbers (0-9)        | `:pw12`  |
| `:pws[length]` | **Secure**   | Letters + Numbers + **Symbols** (!@#$...) | `:pws16` |
| `:pwn[length]` | **Numeric**  | **Numbers only** (PIN style)              | `:pwn06` |

### 2. Practical Examples

- Typing **`:pw12`** results in: `a7B2k9L1p4Xz`
- Typing **`:pws20`** results in: `k#9!2L$p*7xQ9^mN2@5z`
- Typing **`:pwn04`** results in: `8293` (Perfect for quick PINs!)

---

## Why Two Digits?

To ensure maximum speed and reliability, this package waits for exactly two digits after the prefix. This prevents the trigger from firing "too early" (e.g., firing on `:pw2` before you have time to type the `0` for `:pw20`).

## Installation

```
espanso package install password-gen-win
```

## Requirements

- **Operating System**: Windows
- **Engine**: PowerShell (Built-in)
