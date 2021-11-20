# espanso-package-wttr

An espanso package for getting the weather from [Igor Chubin's](https://github.com/chubin) console-oriented weather service [wttr.in](https://wttr.in).

For more information about espanso packages, read the [documentation](https://espanso.org/docs/).

## Usage

Available replacement examples:

| replacement           | sample output                    | description                           |
| --------------------- | -------------------------------- | ------------------------------------- |
| `:wttrin`             | Spring, United States: ⛅️ +80°F | Current location's current weather    |
| `:moonphase`          | 🌕                               | Current phase of the moon             |
| `:wttrat/{location}/` | dallas: ☀️ +88°F                 | Current weather in specified location.  Separate words with `+` instead of spaces. |

## Installation

`espanso install wttr`

## Dependencies

Requires `curl`.

## Package Details

Repository: [https://github.com/bradyjoslin/espanso-package-wttr/](https://github.com/bradyjoslin/espanso-package-wttr/)

This package has been edited by the Espanso Team to port it to the new v2 format.