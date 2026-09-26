# Accent Letters

Type any accented letter by its shape. `;e'` gives **é**, `;n~` gives **ñ**, `;c,` gives **ç**,
`;o/` gives **ø**.

257 triggers covering the accented letters of 55 languages.

## The grammar

`;` then the plain letter, then a symbol that looks like the mark:

| Type | Get | | Type | Get |
| --- | --- | --- | --- | --- |
| `;e'` | é | | `;a*` | å |
| ``;e` `` | è | | `;z.` | ż |
| `;e^` | ê | | `;a-` | ā |
| `;e"` | ë | | `;c<` | č |
| `;n~` | ñ | | `;a(` | ă |
| `;c,` | ç | | `;a;` | ą |
| `;o=` | ő | | `;o/` | ø |

The symbol is chosen to look like the mark it adds: `'` rises like an acute, `` ` `` falls like a
grave, `^` is the circumflex's hat, `"` is the two dots of a diaeresis, `~` is a tilde. Capitals
work the same way — `;E'` gives **É**.

The same grammar works in the accent keyboard at
[accentletters.wiki/tools/accent-keyboard/](https://accentletters.wiki/tools/accent-keyboard/), so
a trigger learned in one works in the other.

## Why `;`

A leading `;` is an escape, so the triggers cannot fire while you are writing ordinary prose — a
semicolon is followed by a space, not by a letter and a punctuation mark. Change it by editing
`package.yml` if it clashes with how you type.

## Where the letters come from

Generated from Unicode 16.0.0 and CLDR 48.2.0 — the same data as the
[Accent Letters](https://accentletters.wiki/) website, apps and add-ons, so a letter cannot differ
between them. A trigger exists only where the base letter and the mark really compose into a single
character, which is why there is no `;q'`: there is no such letter to give you.

Letters that are not a base plus a mark at all — `ø ł đ` and their capitals, where the stroke goes
through the letter rather than sitting on it — are reached with `/`: `;o/`, `;l/`, `;d/`.
