# libreoffice-ppt-math

Type math natively in **LibreOffice Impress & Writer** just like PowerPoint's Math AutoCorrect (`\alpha` → `α`, `^2` → `²`, `^{n+1}` → `ⁿ⁺¹`, `->` → `→`), powered by [Espanso](https://espanso.org).

## Demo

https://github.com/user-attachments/assets/04532d7d-3800-45fc-a8ed-c40ffbd63c70

*Typing `\alpha^2 + \beta^2 -> \infty` natively in LibreOffice Impress.*

---

## Step 1: Install Prerequisites

Before installing, make sure you have these free tools:

1. **Espanso** *(converts shortcuts into math symbols)*
   * Install via the official guide: **[Espanso Installation Docs](https://espanso.org/docs/install/)** (Linux, macOS, Windows)
   * Verify it is running: `espanso status`
2. **Python 3** *(for multi-character superscripts/subscripts and rule generation)*
   * Usually pre-installed on Linux/macOS. Check with `python3 --version` (or **[Python Downloads](https://www.python.org/downloads/)**)
3. **Git** *(only needed for Option 2 below)*
   * Ubuntu/Debian/Mint: `sudo apt install git` (or **[Git Downloads](https://git-scm.com/downloads)**)

---

## Step 2: Install

### Option 1: Fastest (1-Line Espanso Install)
Works on Linux, macOS, and Windows without cloning the repo:

```bash
espanso install libreoffice-ppt-math --git [https://github.com/PavanMohanN/libreoffice-ppt-math](https://github.com/PavanMohanN/libreoffice-ppt-math) --external
espanso restart
