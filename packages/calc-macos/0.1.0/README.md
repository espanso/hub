# espanso-calc-macos
Basic calculation package for espanso that works in macOS.

## Example

![Screen Recording 2022-06-23 at 10 13 21](https://user-images.githubusercontent.com/23709916/175312182-e6372ce2-b296-4d5b-bdc0-a9d8543ab85e.gif)

## Usage
1. Type `:calc`
2. You'll see a form, type the calculation
  <img width="185" alt="image" src="https://user-images.githubusercontent.com/23709916/175305102-2453d39b-b7d8-45f2-8a42-9286a2ab2d25.png"></img>
  3. The text will be replaced with the result

## Commands

| Command                    | Match  | Example       | Result     |
|----------------------------|--------|---------------|------------|
| Calculate                  | :calc  | Input: 10 - 3 | 7          |
| Calculate and show account | :ecalc | Input: 10 - 3 | 10 - 3 = 7 |

## Implementation

This package uses `bc` to do the calculations
```
echo '10 * 4' | bc
```
