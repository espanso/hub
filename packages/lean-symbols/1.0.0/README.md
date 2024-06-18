# Insert the lean unicode math symbols with espanso
Lean4 has a [VScode extension](https://github.com/leanprover/vscode-lean4). This extension provides the facility to insert a wide range of math symbols like ∑ Π α → ↦  Γ etc. This espanso library allows you to insert the same set of symbols using espanso, with the same shortcuts.

For example '\a\', '\a ', '\aTAB', all insert α, i.e. the greek alpha. TAB denotes a single press of the tab key.

The python script within this package can be used to automatically generate the correct mappings from [this file](https://raw.githubusercontent.com/leanprover/vscode-lean4/c7efb256743d3a5e35ffda21f09f6c32900ba69c/vscode-lean4/src/abbreviation/abbreviations.json) located in the github repository of the VScode extension. Note that this file needs to be downloaded and be located in the same directory as the script in order for this to work.
