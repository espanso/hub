# Base64 Utils (Windows)

A zero-dependency Espanso package to encode and decode Base64 strings using your clipboard. This package uses native PowerShell and is designed specifically for Windows.

## Installation

```bash
espanso package install base64-win
```

## Usage

1. Copy the text you want to encode/decode to your clipboard.
2. Type one of the triggers below:

| Trigger | Action                              |
| ------- | ----------------------------------- |
| `:b64e` | Encodes clipboard content to Base64 |
| `:b64d` | Decodes Base64 from clipboard       |

## Requirements

- **Windows:** PowerShell (Built-in, no external dependencies required).
- **macOS / Linux:** PowerShell (`pwsh`) must be installed separately. The package will work, but note that PowerShell on Linux is significantly slower than native shell or python workarounds.
