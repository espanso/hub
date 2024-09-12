# bib-generator
Generates a bib entry from a matching regex using espanso.

Requires Python 3 installed on your system.

## Usage
Just write `:cite:<your search>:` anywhere, it will show 5 results in a form and then replace your text with the .bib entry you selected in the form. It uses the [DBLP](https://dblp.org/) API under the hood, which is restricted to computer science papers only. I highly recommend searching with `<Author> <Some parts of the title>` to improve the search results, as `<Some parts of the title>` often results in irrelevant results.

Note: Espanso limits the regex matches to 30 characters ([Source](https://github.com/espanso/espanso/security)), so you must limit your query.