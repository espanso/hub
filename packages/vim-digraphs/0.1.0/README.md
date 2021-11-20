# vim-digraphs 

A package implementing most of the digraphs from vim-digraphs, themselves taken from the RFC1345 mnemonics. To use, prepend the digraph with comma.

Example: The digraph for α is `a*`. Type `,a*` to type α.

## general principles
(adapted from original helpfile)

To make it easy to remember the mnemonic, the ~~second~~ third character has
a standard meaning:

| char name             | char  | meaning                           | example | result |
|-----------------------|-------|-----------------------------------|---------|--------|
| Exclamation mark      | !     | Grave                             | ,a! | à |
| Apostrophe            | '     | Acute accent                      | ,a' | á |
| Greater-Than sign     | >     | Circumflex accent                 | ,a> | â |
| Question mark         | ?     | Tilde                             | ,a? | ã |
| Hyphen-Minus          | -     | Macron                            | ,a- | ā |
| Left parenthesis      | (     | Breve                             | ,a( | ă |
| Full stop             | .     | Dot above                         | ,e. | ė |
| Colon                 | :     | Diaeresis                         | ,a: | ä |
| Comma                 | ,     | Cedilla                           | ,c, | ç |
| Underline             | _     | Underline                         | ,h_ | ẖ |
| Solidus               | /     | Stroke                            | ,h/ | ħ |
| Quotation mark        | "     | Double acute accent               | ,o" | ő |
| Semicolon             | ;     | Ogonek                            | ,a; | ą |
| Less-Than sign        | <     | Caron                             | ,a< | ǎ |
| Zero                  | 0     | Ring above                        | ,U0 | Ů |
| Two                   | 2     | Hook                              | ,a2 | ả |
| Nine                  | 9     | Horn                              | ,o9 | ơ |
| Equals                | =     | Cyrillic (= used as second char)  | ,D= | Д |
| Asterisk              | *     | Greek                             | ,W* | Ω |
| Percent sign          | %     | Greek/Cyrillic special            | ,s% | ш |
| Plus                  | +     | smalls: Arabic, capitals: Hebrew  | ,A+ | א |
| Three                 | 3     | some Latin/Greek/Cyrillic letters | ,c3 | ҁ |
| Four                  | 4     | Bopomofo                          | ,b4 | ㄅ |
| Five                  | 5     | Hiragana                          | ,A5 | ぁ |
| Six                   | 6     | Katakana                          | ,A6 | ア |

## what did i leave out?

- The control characters from ASCII like Line Feed and Bell
- The control characters from Unicode like Padding Character and High Octet Preset

I could probably add them if there is a desire for that.

For the list of digraphs, read the [documentation of vim-digraph from
vim](https://vimhelp.org/digraph.txt.html#digraphs-default).