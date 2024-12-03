# `tailwindcss-colors`

An [**Espanso**](https://github.com/espanso/espanso) [package](https://espanso.org/docs/packages/basics/) that provides [**TailwindCSS**](https://tailwindcss.com/)'s [default color palette](https://tailwindcss.com/docs/customizing-colors#default-color-palette) as hex color codes. This package is perfect for those who want quick access to TailwindCSS's hex color codes without needing to look them up in the documentation.

## Features

- Integrates smoothly with Espanso.
- Outputs color hex codes of default TailwindCSS colors (e.g., `#3B82F6` for `blue-500`).
- Provides simple triggers for fast and efficient use.

## Installation

1. Ensure you have [Espanso](https://espanso.org/) installed on your system.
2. Install the `tailwindcss-colors` package:

```bash
espanso install tailwindcss-colors
```

## Usage

The triggers follow a straightforward pattern: `:<color_name>-<shade>`. Simply type the trigger to insert the corresponding TailwindCSS hex color codes into your text. Here are a few examples:

| Trigger          | Output     |
|------------------|------------|
| `:blue-500`      | `#3B82F6`  |
| `:gray-300`      | `#D1D5DB`  |
| `:red-700`       | `#B91C1C`  |
| `:yellow-400`    | `#FACC15`  |

To explore the full range of TailwindCSS colors and their hex color codes, check out the [official TailwindCSS color documentation](https://tailwindcss.com/docs/customizing-colors#default-color-palette).

## Uninstalling

If you no longer need the `tailwindcss-colors` package, you can remove it easily:

```bash
espanso uninstall tailwindcss-colors
```
