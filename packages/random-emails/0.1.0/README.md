# Random Emails

Generate random but realistic-looking fake email addresses with
[espanso](https://espanso.org).

| Trigger  | Expands to | Examples |
| -------- | ---------- | -------- |
| `>email` | A random fake address | `eduar@gmail.com` · `j.smith@cocacola.com` · `mgarcia87@mycompany.com` |

Every time you type `>email`, espanso picks a fresh random address, so you get a
different one each time.

## What's inside

The address is **fake, but every part looks real**:

- **~900 real-style usernames** built from real name patterns
  (`eduar`, `j.smith`, `maria.garcia`, `mgarcia87`, `jonnydeep`, …).
- **185 real domains**, mixing real email providers (`gmail.com`,
  `outlook.com`, `proton.me`), real companies (`cocacola.com`, `nike.com`,
  `tesla.com`) and plausible business domains (`mycompany.com`, `myemail.com`).

The username and the domain are combined **independently**, which yields more
than **160,000** possible addresses.

## Usage

Type `>email` anywhere espanso is active and it expands instantly:

```
>email  ->  kenji.tanaka@spotify.com
>email  ->  priya88@gmail.com
```

Great for filling forms, seeding test data, or generating placeholder contacts.

> These are randomly generated addresses. Any resemblance to a real, existing
> mailbox is coincidental — they are meant as placeholder/test data.

## Customizing

The usernames and domains live in `package.yml` under the `local` and `domain`
global variables. Add, remove or edit entries in the `choices` lists to fit your
needs.
