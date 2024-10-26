# Linter Control Comments

A collection of linter control comments for:

Language | Linter
-- | --
Go | [Golint](https://golangci-lint.run/)
Ruby | [Rubocop](https://rubocop.org)
Rust | [Clippy](https://doc.rust-lang.org/stable/clippy/)
Shell | [Shellcheck](https://www.shellcheck.net/)

## How to use

1. Copy a particular linting rule name (from docs, terminal output, etc.).
1. Triggering the espansion. Most `replace`ments use the `{{clipboard}}`.

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
`/nol` | `//nolint:{{clipboard}}`
`/noa` | `//nolint:all`
`#rcd` | `# rubocop:disable {{clipboard}}`
`#rce` | `# rubocop:enable {{clipboard}}`
`#rct` | `# rubocop:todo {{clipboard}}`
`#cla` | `#[allow({{clipboard}})]`
`#clw` | `#[warn({{clipboard}})]`
`#cld` | `#[deny({{clipboard}})]`
`#clp` | `#![deny(clippy::pedantic)]`
`#scd` | `# shellcheck disable={{clipboard}}`
