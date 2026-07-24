# Person Names

Generate random person names on the fly with [espanso](https://espanso.org).

| Trigger | Expands to | Example |
| ------- | ---------- | ------- |
| `>c1`   | First name **+** last name | `Camila Rossi` |
| `>c2`   | First name only            | `Camila` |

Every time you type a trigger, espanso picks a fresh random value, so you get a
different name each time.

## What's inside

- **1000 distinct first names** and **450 last names**, curated from an
  international mix (European, Latin American, East & South Asian, Middle
  Eastern and African) so the output feels realistic and diverse.
- `>c1` combines a first name and a last name **independently**, which yields
  more than **450,000** possible full names.

## Usage

Type `>c1` or `>c2` anywhere espanso is active and it expands instantly:

```
>c1  ->  Kenji Alvarez
>c2  ->  Priya
```

Great for filling forms, seeding test data, or generating placeholder people.

## Customizing

The names live in `package.yml` under the `first_name` and `last_name` global
variables. Add, remove or edit entries in the `choices` lists to fit your needs.
