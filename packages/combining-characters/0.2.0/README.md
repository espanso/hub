# Available matches
| Trigger                  | Replace   |
|--------------------------|-----------|
| :vec:                    | x⃗         |
| :underrightarrow:, :ura: | x⃯         |
| :underleftarrow:, :ula:  | x⃮         |
| :overleftarrow:, :ola:   | x⃡         |
| :underline:, :ul:        | x̲         |
| :bar:                    | x̅         |
| :acute:                  | x́         |
| :macron:                 | x̄         |
| :breve:                  | x̆         |
| :caron:                  | x̌         |
| :ddddot:                 | x⃜         |
| :dddot:                  | x⃛         |
| :ddot:                   | ẍ         |
| :dot:                    | ẋ         |
| :grave:                  | x̀         |
| :hat:                    | x̂         |
| :widehat:                | x̂         |
| :tilde:                  | x̃         |
| :widetilde:              | x̃         |
| :​ring:                   | x̊         |
| :not:, :slash:           | x̸         |

# How to use this package
All you have to do in order to use this package is to type a combining character trigger (e.g. `:vec:`) in front of any character you would like (e.g. a or γ) and obtain the resulting combination (in this example a⃗ or γ⃗).

Each combining character should work for any character, not only for the character `x`, as long as it corresponds to a valid unicode character.

If you are facing issues with the rendering on your program, you might have to install adequate fonts. I myself use Droid Sans (the Mono variant) and JuliaMono and haven't faced any issues rendering any unicode character.
