# CNSNNT Highlander Edition

>"Why waste time type lot letter when few letter do trick."

This package contains shortcuts that allow autocompletion of English words from (mostly) consonants. This the highlander edition which means there are no collisions. Every trigger can only map to a single word. It's been configured to give you whichever word is the most common.

>"60% of the time, it works every time."

## Usage

While typing, try inputting long words with just consonants. Espanso should expand them into the full word. Triggers can begin with a vowel for disambiguation. For example, adtcn for addiction and edtcn for education. To undo an expansion, just press backspace.

## Other Features

Besides first vowel disambiguation, other features include skipping repeated letters (acs -> access), skipping silent letters (bkbn -> backbone) and phonetic substitution (tlfn -> telephone, bjt -> budget) 

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
brj -> bridge
flsf -> philosophy
flpns -> philippines 
imgn the psblts -> imagine the possibilities
sftwr ngnr -> software engineer
xtrml qkl -> extremely quickly

## Installation

Make sure you have already installed [Espanso](https://espanso.org/install/) first.

```sh
espanso install cnsnnt-highlander
espanso restart
```

## Contributing

If you think a trigger should expand into something else or would like to contribute in any other way, please create a pull request or open an issue.
