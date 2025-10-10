# ⚔️ CNSNNT Highlander Edition: *There Can Be Only One* ⚔️

>"Why waste time type lot letter when **few letter do trick**."

This package is a set of **zero-collision** shorthand triggers, allowing you to instantly expand common English words by typing (mostly) only their consonants. This "Highlander" edition ensures that every trigger maps to a single, most-common word, guaranteeing maximum accuracy.

>"**60% of the time, it works every time.**"

<small>**Looking for more flexibility?** For a package where you can choose between multiple possible words for a single trigger, see [CNSNNT Standard Edition](https://hub.espanso.org/cnsnnt).</small>


## 🎯 Core Philosophy: Maximum Efficiency

The system is engineered for speed by employing a few simple substitution rules:

* **Vowel Skipping:** Most vowels are omitted (`btwn` $\rightarrow$ `between`).
* **Repeated Letter Compression:** Skip redundant letters (`acs` $\rightarrow$ `access`).
* **Silent Letter Removal:** Letters that don't affect pronunciation are dropped (`bkbn` $\rightarrow$ `backbone`).
* **Phonetic Substitution:** Type it how it sounds like (`tlfn` $\rightarrow$ `telephone`, `bjt` $\rightarrow$ `budget`).


## 💡 Usage

While typing, simply input the consonant-based trigger. **Espanso** will instantly expand it into the full word.

* To **undo** an expansion, just press **backspace** immediately after it appears.

### Disambiguation

The first letter can be inputted to distinguish between words with similar consonant structures:

| Trigger | Expansion |
| :--- | :--- |
| **a**dtcn | **a**ddiction |
| **e**dtcn | **e**ducation |


## 📖 Examples


| Trigger | Expansion |
| :--- | :--- |
| `hwvr` | `however` |
| `btwn` | `between` |
| `blv` | `believe` |
| `nvlp` | `envelope` |
| `ftbl` | `football` |
| `gnrl` | `general` |
| `gnrll` | `generally` |
| `rqr` | `require` |
| `rqrd` | `required` |
| `nwn` | `known` |
| `nnwn` | `unknown` |
| `mprr` | `emperor` |
| `brj` | `bridge` |
| `flsf` | `philosophy` |
| `flpns` | `philippines` |
| `sftwr` `ngnr` | `software engineer` |
| `xtrml` `qkl` | `extremely quickly` |
| `imgn` `the` `psblts` | `imagine the possibilities` |


## 🚀 Installation

Make sure you have already installed **[Espanso](https://espanso.org/install/)** first.

```sh
espanso install cnsnnt-highlander
espanso restart
```

## 🤝 Contributing

If you think a trigger should expand to a different word or have ideas for new, efficient triggers, please contribute!

* Create a **pull request** with your suggested changes.
* **Open an issue** to discuss potential additions or improvements.
