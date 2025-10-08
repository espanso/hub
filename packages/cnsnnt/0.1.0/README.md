# CNSNNT

"Why waste time type lot letter when few letter do trick."

This package contains shortcuts that allow autocompletion of English words from (mostly) consonants.

## Usage

While typing, try inputting long words with just consonants. Espanso should expand them into the full word. If there are multiple possible expansions for a given trigger, a menu will appear that will allow you to choose the word that you want. Triggers can begin with a vowel for disambiguation. For example, adtcn for addiction and edtcn for education. To undo an expansion, just press backspace.

## Other Features

Besides first vowel disambiguation, other features include skipping repeated letters (acs -> access) and skipping silent letters (bkbn -> backbone). 

## Examples

btwn -> between
hwvr -> however
ftbl -> football
nvlp -> envelope
blv -> believe
mprr -> emperor
nwn -> known
nnwn -> unknown
gnrl -> general
gnrll -> generally
rqr -> require
rqrd -> required
imgn the psblts -> imagine the possibilities
sftwr ngnr -> software engineer
xtrml qkl -> extremely quickly

## Installation

Make sure you have already installed [Espanso](https://espanso.org/install/) first.

```sh
espanso install cnsnnt
espanso restart
```

## Contributions

If you find any triggers that shouldn't be expanded or would like to contribute in any other way, please create a pull request or open an issue.
