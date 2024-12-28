# Date Offsets

Espanso's inbuilt `date` extension is handy, but very limited, particularly because it **cannot** accept a `{{variable}}` for its `offset:` value. 

This package contains short Espanso snippets to return dates offset from today, utilising the date-handling facilities of four different scripting languages, partly as an exercise for me in working out how this can be done.

As supplied, typing a trigger, e.g.:
```
-18d, +2w, -3m, +5y
```
will present you with a choice box, listing the different scripts, each of which will return the relevant (hopefully the same!) date.

Any of the languages you don't have installed will generate Espanso errors:
  - Bash (Linux/macOS) or WSL (Windows)
  - Powershell (Windows) or pwsh (Linux/macOS)
  - Python
  - Javascript

My tests (Linux) indicate that in speed, Bash > Python > Node > PowerShell, but PowerShell is likely to be faster (but not necessarily the *fastest*) in Windows.

Ultimately, adopt one and delete or comment-out the others you don't need.

See my package `timezone-date` for timezone offsets.

Stephen Meech
(@smeech)
