# passwordgeneratorwin
[Espanso](https://espanso.org) extension for generating passwords and copy it to cliboard. For now this extension is only supported on windows systems, beacause of the difference of path between `dos` an `unix` systems. If your are looking this extension for `linux` or `mac` go to [passwordgeneratorlinux](https://github.com/viera97/passwordgeneratorlinux).
## Installation
This espanso extension requires `pyperclip` in order to copy the generated password to clipboard.

```bash
python -m pip install --upgrade pip
python -m pip install pyperclip
```

After installing pyperclip you can install `passwordgeneratorwin` extension by doing:

```bash
espanso install passwordgeneratorwin --git https://github.com/viera97/passwordgeneratorwin --external
```
## Usage

* By typing `:genpass:` a 12 length password will be generated containing lower and upper characters, symbols and digits.
* By typing `:genpass(n)` where $n>4$ is an integer number you can generate a $n$-length password containing lower and upper characters, symbols and digits.

### Not installing pyperclip
I case you didn't install `pyperclip` the extension still woks but it won't copy the generated password to clipboard.