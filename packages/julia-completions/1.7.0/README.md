[![lukeburns - espanso-julia-completions](https://img.shields.io/static/v1?label=lukeburns&message=espanso-julia-completions&color=blue&logo=github)](https://github.com/lukeburns/espanso-julia-completions)

Julia 1.7.0 REPL completions for espanso.

All Latex and emoji symbols available in the Julia REPL are made available with this package. The package version indicates the version of Julia used to generate the substitutions.

Note: you must use the spacebar for autocompletion instead of the tab key. See https://github.com/federico-terzi/espanso/issues/140 for more details.

### Installation

Install [espanso](https://espanso.org/install/), then run

```
espanso install julia-completions
```

### Example

```
i\hbar \gamma \^j \partial \_j \psi  = mc\psi
```
expands to
```
iħγʲ∂ⱼψ = mcψ.
```