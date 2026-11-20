# libreoffice-ppt-math

**PowerPoint-style Math AutoCorrect for LibreOffice.** Type `\int_0^1`, press Space, get `∫₀¹`.
Write maths the way you'd write LaTeX or PowerPoint's linear format, and it turns into clean Unicode as you type, in Impress, Writer or any other app. Powered by [Espanso](https://espanso.org).

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/PavanMohanN/libreoffice-ppt-math/blob/main/LICENSE)
![Platforms](https://img.shields.io/badge/platforms-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)
![Commands](https://img.shields.io/badge/commands-900%2B-brightgreen)
[![Cheat sheet](https://img.shields.io/badge/docs-cheat%20sheet-orange)](https://github.com/PavanMohanN/libreoffice-ppt-math/blob/main/CHEATSHEET.md)

## Demo

https://github.com/user-attachments/assets/04532d7d-3800-45fc-a8ed-c40ffbd63c70

*Typing `\alpha^2 + \beta^2 -> \infty` in LibreOffice Impress (AI-generated).*

## Why you'll like it

* **One rule to learn:** type the formula without spaces, press Space. Nothing converts while you're still typing, so nothing jumps ahead of you.
* **Whole formulas, not just symbols:** limits, sums, integrals, roots over whole terms, fractions, nested powers, vectors, set notation, geometry marks.
* **900+ commands:** every Greek letter, operator, relation, arrow and set symbol you know from LaTeX or Word/PowerPoint, plus `\mathbb`, `\mathcal`, `\mathfrak` and bold fonts.
* **Leaves your normal writing alone:** `snake_case`, `don't`, URLs, `24/7` and file paths are never changed.
* **Undo in one key:** Backspace straight after a conversion gives back exactly what you typed.
* **Works offline, everywhere:** plain Unicode text, so it copies into email, chat, slides and PDFs.

## Quick start (about 60 seconds)

1. Install [Espanso](https://espanso.org/docs/install/) and make sure Python 3 is available (`python3 --version`).
2. Run `espanso install libreoffice-ppt-math`.
3. Open LibreOffice, type `x^2`, press Space, and you get `x²`.

Then open the **[cheat sheet](https://github.com/PavanMohanN/libreoffice-ppt-math/blob/main/CHEATSHEET.md)**: every command, with ready-to-type recipes for algebra, calculus, statistics, physics, geometry and more. Do Step 4 below as well, so LibreOffice's own AutoCorrect doesn't interfere.

## What you can type

| You type | You get |
|---|---|
| `\alpha`, `\Delta`, `\infty` | α, Δ, ∞ |
| `x^2`, `x^{n+1}`, `x^(n+1)`, `a_{ij}` | x², xⁿ⁺¹, xⁿ⁺¹, aᵢⱼ |
| `\alpha^2`, `\theta_0`, `e^{-x^2}` | α², θ₀, e⁻ˣ² |
| `{a+b}^2`, `\frac{a}{b}^2` | (a+b)², (a/b)² |
| `\int_0^1`, `\int_{0}^{\infty}` | ∫₀¹, ∫₀^∞ |
| `\sum_{i=1}^{n}x_i`, `\prod_{k=1}^n` | ∑ᵢ₌₁ⁿ xᵢ, ∏ₖ₌₁ⁿ |
| `\lim_{x\to0}` | lim\_(x→0) |
| `\sqrt{x^2+1}`, `\sqrt[3]{x}` | √x̅²̅+̅1̅, ∛x |
| `\frac{1}{3}`, `\frac{a+b}{c}`, `1/2` | ⅓, (a+b)/c, ½ |
| `A\cup{B}`, `A\cap{B}`, `x\notin{A}`, `A\subseteq{B}` | A∪B, A∩B, x∉A, A⊆B |
| `\overline{AB}`, `\ray{AB}`, `\line{AB}`, `\arc{AB}`, `\angle{ABC}` | A̅B̅, A⃗B⃗, A⃖B⃗, A͡B, ∠ABC |
| `\vec{v}`, `\hat{x}`, `\dot{x}` | v⃗, x̂, ẋ |
| `\mathbb{R}`, `\R^n`, `\mathcal{L}` | ℝ, ℝⁿ, ℒ |
| `a<=b`, `a!=b`, `a->b`, `p<=>q`, `a<->b` | a≤b, a≠b, a→b, p⇔q, a↔b |
| `\forall{x}\exists{y}`, `p\land{q}`, `\neg{p}` | ∀x∃y, p∧q, ¬p |

**The full list, with a beginner's guide and troubleshooting, is in the [cheat sheet](https://github.com/PavanMohanN/libreoffice-ppt-math/blob/main/CHEATSHEET.md).**

**Tips**
* Put spaces *around* an expression, not inside it. `A \cup B` gives `A ∪ B`; `\frac{a b}{c}` won't work.
* Need a space inside an expression? Use `~` or `\,`.
* Expressions up to 25 characters convert with Espanso's default settings. For longer ones (like `\frac{\partial{B}}{\partial{c}}`), add this line to your Espanso `config/default.yml` (run `espanso path config` to find the folder); expressions up to 59 characters then convert:
  ```yaml
  max_regex_buffer_size: 64
  ```
* Pressing **Backspace** straight after a conversion undoes it (Espanso's built-in undo).

---

## Step 1: Prerequisites

1. **Espanso**: follow the [Espanso installation guide](https://espanso.org/docs/install/), then check it runs with `espanso status`.
2. **Python 3**: the conversion runs a small Python script embedded in `package.yml` (standard library only, no network; it only reads `max_regex_buffer_size` from Espanso's `default.yml`).
   Usually pre-installed on Linux and macOS; check with `python3 --version`.
   On **Windows** the package calls `python3`; if that command doesn't exist, use the *Advanced* install below.

## Step 2: Install

### From Espanso Hub
```bash
espanso install libreoffice-ppt-math
```

### Or straight from GitHub
```bash
espanso install libreoffice-ppt-math --git https://github.com/PavanMohanN/libreoffice-ppt-math --external
```

Espanso reloads by itself after installing; no restart is needed.

## Step 3 (recommended): use it only in LibreOffice

By default the rules work in every application. Each keystroke costs well under a microsecond, but every time you press space after a math expression a Python process starts (~20 ms), and arrows such as `->` would also convert in code editors and terminals.
To limit the package to LibreOffice, use an [app-specific configuration](https://espanso.org/docs/configuration/app-specific-configurations/):

1. In your Espanso `config/default.yml` (run `espanso path config` to find the folder), add:
   ```yaml
   extra_excludes:
     - "../match/packages/libreoffice-ppt-math/*"
   ```
2. Create `config/libreoffice.yml` next to it:
   ```yaml
   filter_exec: "(?i)soffice"
   extra_excludes: []
   extra_includes:
     - "../match/packages/libreoffice-ppt-math/package.yml"
   ```

App-specific configurations work on X11, Windows and macOS, but not on Wayland.
(If `default.yml` already had other `extra_excludes`, repeat them in `libreoffice.yml` instead of `[]`.)

**On Linux (X11), if long expressions flicker or leave text behind**, LibreOffice is dropping Espanso's fast synthetic keystrokes. Add this line to `config/libreoffice.yml` (or to `default.yml`):
```yaml
disable_x11_fast_inject: true
```

## Step 4: Stop LibreOffice's own AutoCorrect from interfering (important)

LibreOffice's AutoCorrect list rewrites some of the same sequences first, which corrupts the result (for example `a<->b` becomes `←>`).
In LibreOffice, open **Tools ▸ AutoCorrect Options…**:

* **Replace** tab: delete these entries (for each language you type in):
  `.*->.*` `.*<-.*` `<->` `-->` `<--` `<-->` `.*...` `1/2` `1/4` `3/4` `.*(C)` `.*(R)` `.*(tm)`
* **Options** tab: untick *Automatic \*bold\*, /italic/, -strikeout- and \_underline\_* (and *Replace dashes* if you use `-->`).

Or untick **Use replacement table** to switch LibreOffice's list off entirely.

---

## Limitations

* Unicode has no subscript form for b, c, d, f, g, q, w, y, z, capital letters, → or ∞, so those fall back to readable linear format: `v_y`, `lim_(x→0)`, `∫_(−∞)^∞`.
* Stacked layouts (big fractions, matrices, limits written under the symbol) are impossible in plain text. Use LibreOffice's formula editor (**Insert ▸ Object ▸ Formula**) for those.
* Fonts: see *Fonts* below.
* `\epsilon` and `\phi` follow LaTeX (ϵ, ϕ). Use `\varepsilon` and `\varphi` for ε and φ.

## Fonts (getting sans-serif math automatically)

Espanso types plain text, so the font always comes from LibreOffice. LibreOffice's default fonts (Carlito in Impress, Liberation Sans/Serif in Writer) lack most super/subscripts, accents and many symbols, so LibreOffice borrows each missing character from another font, often a serif one. That gives the mixed look. Two one-time fixes:

* **Everything in one sans font.** Use **DejaVu Sans** for text that contains math; it has 594 of the 619 characters this package produces.
  Writer: *Tools ▸ Options ▸ LibreOffice Writer ▸ Basic Fonts (Western)*, set *Default* to DejaVu Sans (applies to new documents).
  Impress: *View ▸ Master Slide*, select the text placeholders, set the font to DejaVu Sans, then save as your default template.
* **Keep your font, take only the missing characters from DejaVu Sans** (Linux): run the generator (see below) with `--sans-fallback`, then restart LibreOffice. It adds a small fontconfig rule (`~/.config/fontconfig/conf.d/99-libreoffice-ppt-math.conf`) for Carlito, Calibri, Liberation Sans, Arial, Noto Sans, Open Sans, Ubuntu, Cantarell and Helvetica. Delete that file to undo.

## Advanced: the generator (from the homepage)

`package.yml` is built by `generate_rules.py`, which is **not** part of the Hub package.
It lives in the [project homepage](https://github.com/PavanMohanN/libreoffice-ppt-math) under `scripts/`. Download the repository ([ZIP](https://github.com/PavanMohanN/libreoffice-ppt-math/archive/refs/heads/main.zip)), unzip it, and run from that folder. It can:

* **Install for LibreOffice only, set the buffer size, or install on Windows** (it records the full path of your Python):
  ```bash
  python3 scripts/generate_rules.py --install --libreoffice-only --buffer-size 64
  ```
  Remove the Hub/GitHub package first (`espanso uninstall libreoffice-ppt-math`) so the rules aren't loaded twice.
* **Sans-serif fallback for math characters** (Linux): `python3 scripts/generate_rules.py --sans-fallback`
* **Add your own symbols**: edit the `USER_SYMBOLS` block at the top of the script (for example `"\\eps": "ε"`), then rerun the install command.
* **Check and preview**: `--check` (finds duplicate copies, clashing triggers and LibreOffice conflicts), `--self-test`, `--try "\int_0^1"`, `--list arrow`.

On Linux/macOS, `bash install.sh` and `bash uninstall.sh` in the repository wrap the same commands.

## Contributing and feedback

Found a formula that converts wrongly, or a symbol you miss? Please [open an issue](https://github.com/PavanMohanN/libreoffice-ppt-math/issues) with what you typed and what you expected.
Pull requests are welcome. Edit the tables in `scripts/generate_rules.py`, then run `--self-test` (it checks over 1,200 conversions, including every example in the cheat sheet) and `--cheatsheet` to refresh `CHEATSHEET.md`.
If this saves you time, a ⭐ on [GitHub](https://github.com/PavanMohanN/libreoffice-ppt-math) helps other people find it.

## Uninstall

```bash
espanso uninstall libreoffice-ppt-math
```
Also remove the Step 3 lines from `default.yml` and delete `config/libreoffice.yml` if you added them.
If you installed with the generator, run `python3 scripts/generate_rules.py --uninstall` instead.

## License

[MIT](https://github.com/PavanMohanN/libreoffice-ppt-math/blob/main/LICENSE)
