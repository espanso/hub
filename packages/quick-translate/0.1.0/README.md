# Espanso Translate-Shell Extension

This package utilizes the functionality of [translate-shell](https://github.com/soimort/translate-shell) to translate texts into various languages using [Espanso Open-Source Text-Expander](https://github.com/espanso/espanso).

## Installation

Before using this package, make sure you have [translate-shell](https://github.com/soimort/translate-shell/wiki/Distros) installed on your system. If you don't, you can install it for your OS [here](https://github.com/soimort/translate-shell/wiki/Distros)

Once you have it installed, you can install this package using the following command:

```bash
espanso install quick-translate --git https://github.com/p0ly60n/quick-translate --external
```

After Installing, you can change the `sourcelang` and `targetlang` variables in [defaultlang.yml](defaultlang.yml) to your desired default languages. You can find the valid names at the bottom of [package.yml](package.yml)

## Usage

- `::trans`: Translates the selected text to the target language (default: English)
- `::etrans`: Extended Translate - Translates the Text from a source language (default: German) to a target language (default: English)