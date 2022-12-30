This is a translation package.

It is for bidirectional translation between **English** and **Spanish**.

Please note that it will use 6MB of disk storage, and 250MB of RAM when loaded into Espanso.

# Example matches
| Trigger    | Replace                               |
|------------|---------------------------------------|
| apple:es   | manzana {f}                           |
| biscuit:es | galetta / biscocho {m}, bizcocho {m}  |
| sol:en     | sun                                   |
| hoy:en     | daylight/sunlight/sunny side (choice) |

# Source code for package.yml generation

A Go script turns "Creative Commons Attribution-ShareAlike 3.0 Unported License"-licensed Spanish-English dictionaries into Espanso trigger/replacement pairs.

The code is in the repository [espanso-translate-generator](https://github.com/IdiosApps/espanso-translate-generator)