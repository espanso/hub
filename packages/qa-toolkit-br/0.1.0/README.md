# QA Toolkit BR

Snippets for **Quality Assurance** work, focused on Brazilian test data. Type a trigger and Espanso pastes freshly generated test data: valid CPF/CNPJ, names, phones, UUIDs, tokens, JWTs, Lorem ipsum, edge-case inputs and bug report templates.

> **Português:** atalhos para QA que geram CPF/CNPJ válidos (fake), nomes, celulares, UUID, token, JWT, Lorem ipsum, payloads de teste e templates de bug report.

## Requirements

Most generators run a small **Python 3** script (standard library only, no extra packages).

- `python3` must be available in your `PATH`.
- **Windows:** if your Python is called `python` or `py`, replace `python3` with that command in `package.yml`.

All snippets use `force_mode: clipboard` so the value is pasted at once. This avoids problems with input masks in web forms.

## Triggers

### Brazilian documents (check digits are valid)

| Trigger | Example |
|---|---|
| `:fakecpf` | `123.456.789-09` |
| `:fakencpf` | `12345678909` (digits only) |
| `:fakecnpj` | `12.345.678/0001-95` |
| `:fakencnpj` | `12345678000195` (digits only) |

### Personal data

| Trigger | Output |
|---|---|
| `:fakenome` | Random Brazilian full name |
| `:fakeemail` | Unique address at `@example.com` (reserved domain, never delivers) |
| `:fakecel` | Mobile number, e.g. `(11) 98765-4321` |
| `:fakecep` | Real CEP from a state capital, e.g. `01001-000` |
| `:fakeplaca` | Mercosul license plate, e.g. `ABC1D23` |
| `:fakecartao` | Visa test card number that passes the Luhn check |
| `:fakesenha` | Strong 16-character password |

### Identifiers

| Trigger | Output |
|---|---|
| `:uuid` | UUID v4 |
| `:token` | Random URL-safe token (32 bytes) |
| `:jwt` | HS256 JWT valid for 1 hour, signed with the key `qa-secret` |

### Date and time

| Trigger | Output |
|---|---|
| `:iso` | Current local time in ISO 8601, e.g. `2026-10-21T14:30:00-03:00` |
| `:epoch` | Current Unix timestamp |

### Test inputs

| Trigger | Output |
|---|---|
| `:lorem` | One paragraph of Lorem ipsum |
| `:lipsum3` | Three paragraphs of Lorem ipsum |
| `:max255` | Exactly 255 characters, for field length limits |
| `:unicode` | Accents, CJK, Arabic, emoji, quotes and HTML characters |
| `:xss` | `<script>alert('XSS')</script>` |
| `:sqli` | `' OR '1'='1' -- ` |

### Templates (Portuguese)

| Trigger | Output |
|---|---|
| `:bug` | Bug report template with today's date |
| `:gherkin` | BDD scenario (Funcionalidade / Cenário / Dado / Quando / Então) |

## Disclaimer

All generated data is fake and intended **only for software testing**. The CPF, CNPJ and card numbers are mathematically valid but random. Do not use them to impersonate people or companies, or for fraud.

The `:xss` and `:sqli` payloads are classic test strings. Only use them on systems you are authorized to test.
