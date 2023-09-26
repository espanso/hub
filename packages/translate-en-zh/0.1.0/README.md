This is a translation package.

It is for translation from **English** to **Chinese**.

Bi-directional translation support (Chinese to English too) may be added later - [Espanso has a bug with Chinese triggers](https://github.com/federico-terzi/espanso/issues/101). If you think you can help with that, please have a try!

Please note that it will use 2.5MB of disk storage, and 80MB of RAM when loaded into Espanso.

# Example matches
| Trigger       | Replace                           |
|---------------|-----------------------------------|
| television:zh | {电视/電視}(diàn shì)[television]     |
| apple:zh      | {苹果/蘋果}(píng guǒ)[apple] (choice) |
| sun:zh        | {太阳/太陽}(tài yang)[sun] (choice)   |

# Source code for package.yml generation

A Golang script turns an dictionary into Espanso trigger/replacement pairs.

The code is in the repository [espanso-translate-generator](https://github.com/IdiosApps/espanso-translate-generator)