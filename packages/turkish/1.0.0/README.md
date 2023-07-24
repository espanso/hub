# Turkish Characters 🇹🇷

A simple package to convert English characters to Turkish.

## Vowels
| Trigger | Replacement |
|:-------------:|:-------------:|
| U-            | Ü     |
| O-            | Ö     |
| I-            | İ     |
| u-            | ü     |
| o-            | ö     |
| i-            | ı    |


## Consonants
| Trigger | Replacement |
|:-------------:|:-------------:|
| C-            | Ç     |
| S-            | Ş     |
| G-            | Ğ     |
| c-            | ç     |
| s-            | ş     |
| g-            | ğ     |

## Criteria for the 'trigger character'
- Should be accessible with one key stroke.
    - This is why `:` is not good enough.
- Should be *caps lock agnostic*
    - This is why repetions are not good enough.
    - E.g. `Ii` and `II` should both be replaced with `İ`. What about `iI`? Is it `İ` or `ı`?
- It should come **after** the base character. It just feels more natural.
    - `:` won't work, e.g. "numbers: 1, 2, 3" would get replaced with "numberş 1, 2, 3"
- [base] + [trigger] is not a valid combination otherwise.
    - `e` after vowels: Goethe
    - `x` after consonants: Matrix
    - `'`: Marc's
    - `-`: `i--` (programming)

### Decision
`-` satisfies almost all of the criteria, except for one: it can have a special meaning in some programming languages. But I prefer `i -= 1` over `i--`, you don't need it that often in most of the modern programming languages anyway (because we have for-in loops). And most people don't write code, so it should be okay. This why I decided to go with `-`.