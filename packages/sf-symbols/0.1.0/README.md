# SF Symbols

An Espanso package to insert Apple’s [SF Symbols](https://developer.apple.com/sf-symbols/), which are part of the [SF Pro System Font](https://developer.apple.com/fonts/) used within Apple’s platforms.

The package currently includes the 5,359 symbols available in SF Symbols Version 5.2 (macOS 14.2+, iOS 17.2+).

## Installation

```
espanso install sf-symbols
espanso restart
```

## Triggers

### Selection Dialog

A selection dialog containing all SF Symbols can be triggered through `:sf:`. On macOS (where this package is primarily useful), a preview of each symbol is visible within the dialog.

Where provided by Apple, search keywords are appended to symbols’ names to make searching easier.

### Individual Symbols

Individual symbols can be inserted using `:sf.name.of.symbol:`. For example, the `checkmark.square` symbol is triggered through `:sf.checkmark.square:`. In cases where a symbol has alternate or deprecated names, all of these names are available as a trigger.