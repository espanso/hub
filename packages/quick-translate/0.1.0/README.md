# Espanso Translate-Shell Extension

This package utilizes the functionality of [translate-shell](https://github.com/soimort/translate-shell) to translate texts into various languages using [Espanso Open-Source Text-Expander](https://github.com/espanso/espanso).

## Installation

Before using this package, make sure you have [translate-shell](https://github.com/soimort/translate-shell/wiki/Distros) installed on your system. If you don't, you can install it for your OS [here](https://github.com/soimort/translate-shell/wiki/Distros). Make sure to install and use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) when using Windows.

Once you have it installed, you can install this package using the following command:

```bash
espanso install quick-translate
espanso restart
```

After Installing, you can change the `sourcelang` and `targetlang` variables in [defaultlang.yml](defaultlang.yml) to your desired default languages. You can find the valid names at the bottom of [package.yml](package.yml). Please note that if there's an update in the future, those files could be overwritten.

## Usage

- `::trans`: Translates the selected text to the target language (default: English)
- `::etrans`: Extended Translate - Translates the Text from a source language (default: German) to a target language (default: English)