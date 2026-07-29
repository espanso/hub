# Italian ZIP Codes to City Names

An [espanso](https://espanso.org) package that expands an Italian postal code (CAP)
into the code followed by its comune.

```
:00184   →   00184 Roma
:20121   →   20121 Milano
```

The package ships **4657 triggers**, one per distinct CAP.

## Usage

Type a colon followed by the five-digit CAP `:00184` and espanso replaces it
with `00184 Roma`.

## Data

Triggers are generated from the [ISTAT](https://www.istat.it/note-legali/)-derived list of
Italian comuni with their CAP.

### One comune per CAP

The source data is a many-to-many mapping: a comune can hold several CAPs, and a
CAP can cover several comuni. Espanso only ever fires the *first* match for a
duplicated trigger, so a file containing every row would carry thousands of dead
entries.

Each CAP therefore resolves to a single comune, chosen by:

1. the comune flagged as capoluogo, if one of the candidates is;
2. otherwise the alphabetically first comune.

That collapses 8456 source rows into 4657 usable matches. If you need a specific
one of the shared comuni instead, override it in your own `match/base.yml`.