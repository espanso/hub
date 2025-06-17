# Named HTML Entities package for Espanso

Wish you could use HTML entities in regular text? Now you can! For any HTML entity, type it with a `:` prefix instead of `&`, and have it replaced with the Unicode character.

For instance:

| Shortcut      | Character | Unicode Name            |
|---------------|-----------|-------------------------|
| `:amp;`       | `&`       | Ampersand               |
| `:copy;`      | `©`       | Copyright sign          |
| `:mdash;`     | `—`       | Em dash                 |
| `:hellip;`    | `…`       | Horizontal ellipsis     |
| `:infin;`     | `∞`       | Infinity                |
| `:rarr;`      | `→`       | Rightwards arrow        |
| `:larr;`      | `←`       | Leftwards arrow         |
| `:ne;`        | `≠`       | Not equal to            |
| `:harr;`      | `↔`       | Left right arrow        |
| `:spades;`    | `♠`       | Black spade suit        |
| `:starf;`     | `★`       | Black star              |
| `:there4;`    | `∴`       | Therefore               |
| `:fnof;`      | `ƒ`       | Latin small f with hook |

The [full list](https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references) is huge!

Note that this package does NOT support typing Unicode escape sequences like `&#NNNN`, where the `N` characters are digits.

## HTML entity reference

- [List of XML and HTML character entity references (Wikipedia)](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references)
- [Named character references (WHATWG HTML Living Standard)](https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references)

## This package

This package is built from [mrled/espanso-named-html-entities](https://github.com/mrled/espanso-named-html-entities).
