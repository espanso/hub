# libreoffice-ppt-math

Type math in **LibreOffice Impress & Writer** the way PowerPoint's Math AutoCorrect works, powered by [Espanso](https://espanso.org).
Write LaTeX-style linear math, press **space**, and the whole expression turns into Unicode.

## Demo

https://github.com/user-attachments/assets/04532d7d-3800-45fc-a8ed-c40ffbd63c70

*Typing `\alpha^2 + \beta^2 -> \infty` in LibreOffice Impress (AI-generated).*

---

## How it works

Type an expression **without spaces**, then press **space**. The whole expression is converted in one go.

| You type | You get |
|---|---|
| `\alpha`, `\Delta`, `\infty` | α, Δ, ∞ |
| `x^2`, `x^{n+1}`, `x^(n+1)`, `a_{ij}` | x², xⁿ⁺¹, xⁿ⁺¹, aᵢⱼ |
| `\alpha^2`, `\theta_0`, `e^{-x^2}` | α², θ₀, e⁻ˣ² |
| `\int_0^1`, `\int_{0}^{\infty}` | ∫₀¹, ∫₀^∞ |
| `\sum_{i=1}^{n}x_i`, `\prod_{k=1}^n` | ∑ᵢ₌₁ⁿ xᵢ, ∏ₖ₌₁ⁿ |
| `\lim_{x\to0}` | lim_(x→0) |
| `\sqrt{x^2+1}`, `\sqrt[3]{x}` | √x̅²̅+̅1̅, ∛x |
| `\frac{1}{3}`, `\frac{a+b}{c}`, `1/2` | ⅓, (a+b)/c, ½ |
| `A\cup{B}`, `A\cap{B}`, `x\notin{A}`, `A\subseteq{B}` | A∪B, A∩B, x∉A, A⊆B |
| `\overline{AB}`, `\ray{AB}`, `\line{AB}`, `\arc{AB}`, `\angle{ABC}` | A̅B̅, A⃗B⃗, A⃖B⃗, A͡B, ∠ABC |
| `\vec{v}`, `\hat{x}`, `\dot{x}` | v⃗, x̂, ẋ |
| `\mathbb{R}`, `\R^n`, `\mathcal{L}` | ℝ, ℝⁿ, ℒ |
| `a<=b`, `a!=b`, `a->b`, `p<=>q`, `a<->b` | a≤b, a≠b, a→b, p⇔q, a↔b |
| `\forall{x}\exists{y}`, `p\land{q}`, `\neg{p}` | ∀x∃y, p∧q, ¬p |

Around 900 commands are supported: Greek, operators, relations, arrows, sets, logic, big operators, geometry, delimiters, accents and font styles (`\mathbb`, `\mathcal`, `\mathfrak`, `\mathbf`, …).

**Tips**
* Put spaces *around* an expression, not inside it. `A \cup B` gives `A ∪ B`; `\frac{a b}{c}` won't work.
* Need a space inside an expression? Use `~` or `\,`.
* Pressing **Backspace** straight after a conversion undoes it (Espanso's built-in undo).
* Text without math syntax (`snake_case`, `don't`, URLs, `24/7`) is never touched.

---

## Step 1: Prerequisites

1. **Espanso**: follow the [Espanso installation guide](https://espanso.org/docs/install/), then check it runs with `espanso status`.
2. **Python 3**: the conversion runs a small local Python script (standard library only, no network or file access).
   Usually pre-installed on Linux and macOS; check with `python3 --version`.
   On **Windows** the package calls `python3`; if that command doesn't exist, use Option C below instead.

## Step 2: Install

### Option A: from Espanso Hub
```bash
espanso install libreoffice-ppt-math
```

### Option B: straight from GitHub
```bash
espanso install libreoffice-ppt-math --git https://github.com/PavanMohanN/libreoffice-ppt-math --external
```

Espanso reloads by itself after installing; no restart is needed.
Options A and B make the rules work in every application.

### Option C: LibreOffice only, longer expressions, or Windows
Download this repository ([ZIP](https://github.com/PavanMohanN/libreoffice-ppt-math/archive/refs/heads/main.zip)), unzip it, and run from that folder:

```bash
python3 scripts/generate_rules.py --install --libreoffice-only --buffer-size 64
```

* `--libreoffice-only` activates the rules only while LibreOffice is focused (X11, Windows and macOS; not Wayland).
* `--buffer-size 64` raises Espanso's `max_regex_buffer_size`, so expressions up to 59 characters convert (default: 25).
* It records the full path of the Python you run it with, so it also works on Windows.
* Leave out either flag if you don't want it. If you used Option A or B before, remove that first: `espanso uninstall libreoffice-ppt-math`.

On Linux/macOS, `bash install.sh` does the same as Option C (add `--libreoffice-only` if wanted).

## Step 3: Stop LibreOffice's own AutoCorrect from interfering (important)

LibreOffice's AutoCorrect list rewrites some of the same sequences first, which corrupts the result (for example `a<->b` becomes `←>`).
In LibreOffice, open **Tools ▸ AutoCorrect Options…**:

* **Replace** tab: delete these entries (for each language you type in):
  `.*->.*` `.*<-.*` `<->` `-->` `<--` `<-->` `.*...` `1/2` `1/4` `3/4` `.*(C)` `.*(R)` `.*(tm)`
* **Options** tab: untick *Automatic \*bold\*, /italic/, -strikeout- and \_underline\_* (and *Replace dashes* if you use `-->`).

Or untick **Use replacement table** to switch LibreOffice's list off entirely.

---

## Checking and troubleshooting

```bash
python3 scripts/generate_rules.py --check          # finds duplicate copies, clashing triggers, LibreOffice conflicts
python3 scripts/generate_rules.py --self-test      # runs 358 built-in conversion tests
python3 scripts/generate_rules.py --try "\int_0^1" # previews a conversion
python3 scripts/generate_rules.py --list arrow     # lists every command matching "arrow"
```

## Limitations

* Unicode has no subscript form for b, c, d, f, g, q, w, y, z, capital letters, → or ∞, so those fall back to readable linear format: `v_y`, `lim_(x→0)`, `∫_(−∞)^∞`.
* Stacked layouts (big fractions, matrices, limits written under the symbol) are impossible in plain text. Use LibreOffice's formula editor (**Insert ▸ Object ▸ Formula**) for those.
* Some fonts lack these symbols or place accents badly. DejaVu Sans, STIX Two Math or Cambria Math give the best results.
* `\epsilon` and `\phi` follow LaTeX (ϵ, ϕ). Use `\varepsilon` and `\varphi` for ε and φ.

## Adding your own symbols

Edit the `USER_SYMBOLS` block at the top of [`scripts/generate_rules.py`](scripts/generate_rules.py), for example `"\\eps": "ε"`, then run the install command again.
`package.yml` is generated from that script; don't edit it by hand.

## Uninstall

```bash
espanso uninstall libreoffice-ppt-math              # Options A and B
python3 scripts/generate_rules.py --uninstall      # Option C (or: bash uninstall.sh)
```

## License

[MIT](LICENSE)
