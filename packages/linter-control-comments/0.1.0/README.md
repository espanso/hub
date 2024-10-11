# Linter Control Comments

A collection of linter control comments for
[Rubocop](https://rubocop.org)/Ruby
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
