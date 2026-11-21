# UniRate Currency Converter

Convert amounts and look up live exchange rates without leaving whatever you're
typing in. Powered by the [UniRate API](https://unirateapi.com) via the small,
zero-dependency [`unirate` CLI](https://github.com/UniRate-API/unirate-cli).

## Triggers

| Trigger | What it does | Example output |
|---|---|---|
| `:fx` | Opens a form (amount / from / to) and converts | `100 USD = 92.5 EUR` |
| `:rate` | Opens a form (from / to) and returns the unit rate | `1 USD = 150 JPY` |

Currency codes are the usual ISO-4217 codes (`USD`, `EUR`, `JPY`, `GBP`, …);
170+ fiat and crypto currencies are supported.

## Setup

This package shells out to the `unirate` CLI, so you need two things:

1. **Install the CLI** — pick one:

   ```bash
   # macOS (Homebrew)
   brew install --cask UniRate-API/unirate/unirate

   # Windows (Scoop)
   scoop bucket add unirate https://github.com/UniRate-API/scoop-unirate
   scoop install unirate

   # Any platform with a Go toolchain
   go install github.com/UniRate-API/unirate-cli@latest
   ```

   Prebuilt binaries for linux/macOS/windows are also attached to each
   [GitHub release](https://github.com/UniRate-API/unirate-cli/releases).

2. **Set a free API key** — [get one here](https://unirateapi.com) (no credit
   card), then export it so espanso's shell commands can see it:

   ```bash
   export UNIRATE_API_KEY="your-api-key"
   ```

   Put that line in your shell profile (`~/.bashrc`, `~/.zshrc`, or the Windows
   equivalent) and restart espanso so it inherits the variable.

Verify the CLI works on its own first:

```bash
unirate convert 100 USD EUR
# 100 USD = 92.5 EUR
```

## Notes

- Both triggers are **read-only** — they make an HTTPS GET to the UniRate API
  and print the result. Nothing is written to or changed on your system.
- If a trigger expands to nothing, the CLI probably isn't on espanso's PATH or
  `UNIRATE_API_KEY` isn't set in the environment espanso was launched from.

## License

MIT — see the [`unirate-cli` repository](https://github.com/UniRate-API/unirate-cli).
