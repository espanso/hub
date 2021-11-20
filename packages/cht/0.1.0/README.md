# espanso-package-cht

An espanso package for getting code snippets from [Igor Chubin's](https://github.com/chubin) console-oriented cheat sheet service [cht.sh](https://cht.sh). [Espanso](https://espanso.org/) is a free cross-platform text expander written in Rust.

![usage](https://github.com/bradyjoslin/espanso-package-cht/raw/master/images/chtjs.gif)

For more information about espanso packages, read the [documentation](https://espanso.org/docs/).

## Usage

Available replacements:

| replacement      | description                 |
| ---------------- | --------------------------- |
| `:cht/{query}/`  | Code only, no comments.     |
| `:vcht/{query}/` | Verbose. Code and comments. |

## Installation

`espanso install cht`

## Dependencies

Requires `curl`.

## Package Details

Repository: [https://github.com/bradyjoslin/espanso-package-cht/](https://github.com/bradyjoslin/espanso-package-cht/)

This package has been edited by the Espanso Team to port it to the new v2 format.