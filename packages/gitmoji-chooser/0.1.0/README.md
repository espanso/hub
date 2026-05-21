# gitmoji-chooser

An espanso package that provides a choice picker for [gitmoji](https://gitmoji.dev/) emoji.

## Usage

Type `:gitmoji` to open a choice dialog with all 75 gitmoji entries. Select one to insert the emoji character into your text.

Each entry shows the emoji, its shortcode, and a description — for example:

    🎨 :art: Improve structure / format of the code.

Selecting it inserts `🎨`.

Compare with the [gitmojis support](https://hub.espanso.org/gitmojis) package, which directly offers triggers for the gitmoji. This package uses the [choice extension](https://espanso.org/docs/matches/extensions/#choice-extension) for a nice UI.

## Installation

```
espanso install gitmoji-chooser
```

## Source

All emoji and descriptions come from https://gitmoji.dev/.
