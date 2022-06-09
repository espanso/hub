This is a translation package.

It is for bidirectional translation between **English** and **French**.

# Example matches
| Trigger    | Replace                |
|------------|------------------------|
| apple:fr   | pomme                  |
| hello:fr   | bonjour/salut (choice) |
| soleil:en  | sun                    |
| jour:en    | aperture/day (choice)  |

# Source code for package.yml generation

A simple Go script turns an MIT-licensed French-English dictionary into Espanso trigger/replacement pairs.

The code is in the repository [espanso-translate-fr-en-generator](https://github.com/IdiosApps/espanso-translate-fr-en-generator)