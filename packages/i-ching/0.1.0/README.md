# I Ching (Book of Changes) Unicode Symbols

A text expander package providing quick access to I Ching hexagrams, trigrams, bigrams, and monograms with multiple information formats.

## About I Ching

The I Ching, or Book of Changes, is an ancient Chinese divination text consisting of 64 hexagrams (六十四卦) that represent different life situations and transformations.

## Installation

espanso install i-ching

## Usage Rules

**Hexagrams:** Use `:ic` followed by a 6-digit binary code (1s and 0s). Examples:

- `:ic111111` → ䷀ (The Creative)
- `:ic000000` → ䷁ (The Receptive)

**Information Formats:**

- `:icc` = Chinese name with symbol
- `:ice` = English name with symbol
- `:icl` = Link to ctext.org reference

**Trigrams:** Use `:ict` followed by 3-digit binary code (`:ict111` → ☰)

**Bigrams:** Use `:icb` followed by 2-digit binary code (`:icb11` → ⚌)

**Monograms:** Use `:icm` followed by single digit (`:icm1` → ⚊)
