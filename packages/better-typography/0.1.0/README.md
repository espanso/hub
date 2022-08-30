# Better Typography

This is an Espanso package to help with converting quotes into smart quotes. I created the file when I realized I had extensions or plugins in multiple apps meant to assist with these conversions. This particular config file is inspired by the [Smart Typography](https://github.com/mgmeyers/obsidian-smart-typography) plugin for Obsidian by mgmeyers.

## Replacements

*NOTE:* The pipe is the cursor position.

| Trigger | Replacement | Character                |
|---------|-------------|--------------------------|
| ,"      | “$\|$”      | smart quotes             |
| ,'      | ‘$\|$’      | single smart quote       |
| ''      | ’           | unicode apostrophe       |
| ,n      | –           | en dash                  |
| ,m      | —           | em dash                  |
| ...     | …           | ellipsis                 |
| <<      | «           | open guillemet           |
| >>      | »           | close guillemet          |
| <-      | ←           | left arrow               |
| ->      | →           | right arrow              |
| <=      | ≤           | less than or equal to    |
| >=      | ≥           | greater than or equal to |
| /=      | ≠           | not equal                |

## Regex Match

The first regex match is for typing fractions. It uses the Unicode fraction slash `⁄⁄` U+2044. It is written to allow any digits as the numerator or denominator. Although there is a space in the denominator regex, this prevents the match from triggering after a single digit. The other regex matches are for superscript and subscript, respectively.

*NOTE:* Whole numbers must be used. Decimals are currently unsupported.

*NOTE:* The superscript and subscript work only if the editor allows HTML markup.

| Regex                                  | Replacement                         |
|----------------------------------------|-------------------------------------|
| `(?P<num1>\d+)/(?P<num2>\d+ )`         | `{{num1}}⁄{{num2}}`                 |
| `(?P<letter1>\w+)](?P<letter2>\w{2} )` | `{{letter1}}<sup>{{letter2}}</sup>` |
| `(?P<letter1>\w+)}(?P<letter2>\w{2} )` | `{{letter1}}<sub>{{letter2}}</sub>` |
