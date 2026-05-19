# Math Calculator for Espanso

Evaluate math expressions inline using Python's math engine.

**Requires Python installed on the system.**

## Triggers

| Trigger | Output | Example |
|---------|--------|---------|
| `:calc` | Result only | `1013.5` |
| `:xcalc` | Expression = Result | `(10^3) + sqrt(144) = 1012` |

## Supported operations

- Basic: `+`, `-`, `*`, `/`
- Power: `^` or `**`
- `sqrt(x)`, `pow(x, y)`
- `sin(x)`, `cos(x)`, `tan(x)`, `asin`, `acos`, `atan`
- `log(x)`, `log2(x)`, `log10(x)`
- `ceil(x)`, `floor(x)`, `factorial(x)`
- Constants: `pi`, `e`, `tau`
- Parentheses and nested expressions

## Examples

- `(19+1)^2` → `400`
- `sqrt(144)` → `12`
- `sin(pi/2)` → `1`
- `log10(1000)` → `3`
- `factorial(6)` → `720`
- `(sqrt(2)+1)^2` → `5.828427124`

## Reference

Full list of available functions: https://docs.python.org/3/library/math.html
