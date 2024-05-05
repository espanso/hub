# Lean abbreviations

This package contains all input abbreviations
used by the [Lean theorem prover](https://leanprover.github.io).
They are the same abbreviations used by the editor plugins
for VS Code, neovim, and (with some differences) Emacs.

For example, you can type `L\ex \al N` to get `L∃∀N`.

Please note that the behavior of the espanso expansions
is slightly different from how the editor plugins work:
you need to type a space after every abbreviation.

If you want to use a leader character other than `\`
(e.g., `,all ` instead of `\all `),
please check out and adapt the
[Python script](https://github.com/gebner/espanso-lean)
that generates this package.

## Installation

Install [espanso](https://espanso.org/install/), then run:
```
espanso install lean
```
