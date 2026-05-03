# Base64 Utils

A cross-platform Espanso package to encode and decode Base64 strings using your clipboard.

## Installation

```bash
espanso package install base64-utils
```

## Usage

1. Copy the text you want to encode/decode to your clipboard.
2. Type one of the triggers below:

| Trigger | Action |
| --- | --- |
| `:b64e` | Encodes clipboard content to Base64 |
| `:b64d` | Decodes Base64 from clipboard |

## Requirements

- **Windows:** PowerShell (Built-in)
- **macOS/Linux:** `base64` and `openssl` utilities (Standard)
