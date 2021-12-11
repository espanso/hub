## An Espanso package for typing Chinese pinyin tones

This package allows you to quickly and easily write characters marked with pinyin tones. For example, marked characters for the letter "e" can be created as follows:

| Input      | Output |
| ----------- | ----------- |
| :e1      | ē       |
| :e2   | é        |
| :e3      | ě       |
| :e4   | è        |
| :e5      | e       |

Similarly, other tones can be created:

| letter | 1st tone  |  2nd tone | 3rd tone  | 4th tone
|---|---|---|---|---|---|
| a  | ā  | á  | ǎ  | à  | 
| e  | ē  | é  | ě  |  è |
| i  | ī  |  í | ǐ  | ì  |
| o  | ō  |  ó | ǒ  | ò  |
| u  | ū  |  ú | ǔ  | ù  |
| ü  | ǖ  |  ǘ | ǚ  | ǜ  |

The only exception is that the marked characters for "ü" are typed a bit differently: either with {:u:5 -> ü}, {:u:1 -> ǖ}, etc., or with {:v5 -> ü}, {:v1 -> ǖ}, etc.

