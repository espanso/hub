# About
**single-steno** is an Estenso package that converts single character inputs into the 26 most commonly used words in the English language.

# Conversions
b → because
c → come
d → could
e → even
f → for
g → give
h → have
i → I
j → just
k → know
l → like
m → most
n → and
N → not
o → other
p → people
q → question
r → are
s → some
t → the
u → under
v → very
w → with
x → exactly
y → you
z → these

# Notes
- Since `a` is a word already, it has no conversion.
- Lowercase `i` gets automatically converted into uppercase `I`, removing the need to push the shift key.
- `n` is mapped to `and`. Since a sentence cannot start with `and` it can never be uppercase. This leaves us free to map uppercase `N` to `not`.
