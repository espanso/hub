# Linter Control Comments

A collection of linter control comments for
[Rubocop](https://rubocop.org)/Ruby,
[Clippy](https://doc.rust-lang.org/stable/clippy/)/Rust,
and [Shellcheck](https://www.shellcheck.net/)/Shell
.

## Trigger composition

Symbol | Why that one in particular?
-- | --
`#` | Comment symbol for the relevant language.
`rb` | Abbreviated name of the linter, ideally following its syllables.
`d` | First letter of the linter's keyword

This hopefully helps to reuse existing muscle memory,
from having already used these linters manually.

## Espansions

Trigger | Replace
-- | --
`#rcd` | `# rubocop:disable {clipboard}`
`#rce` | `# rubocop:enable {clipboard}`
`#rct` | `# rubocop:todo {clipboard}`
`#cla` | `#[allow({clipboard})]`
`#clw` | `#[warn({clipboard})]`
`#cld` | `#[deny({clipboard})]`
`#clp` | `#![deny(clippy::pedantic)]`
`#scd` | `# shellcheck disable={clipboard}`
