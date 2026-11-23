# SnipBank

Easily collect snippets and recall them later with Espanso.

## Requirements

- Espanso 2.x or higher
- Python 3.x or higher with Pip
- PyYAML 5.x or higher

## Installation

```bash
pip install pyyaml
espanso install snipbank
```

## Keyboard Shortcuts

- Use `,,..` (two commas, two dots) to add a snippet.
- Use `..,,` (two dots, two commas) to remove a snippet.

## Pressing Tab and Enter in a Snippet

- Use `^TAB^` in a snippet for pressing the Tab key.
- Use `^ENTER^` in a snippet for pressing the Enter key.
- Use `$|$` in a snippet to bring the cursor there upon inserting it.

## Specifying a Form

You may optionally specify a popup form to go with a snippet in order to make
parts of the snippet editable before its insertion.

- Under "Form", enter the text to show in the popup. Use these to indicate fields:
    - Text field: `[[variable_name]]`
    - Text area: `[![variable_name]!]`
    - Dropdown: `[^[variable_name:opt1|opt2|...]^]`
    - List: `[>[variable_name:opt1|opt2|...]<]`
- You may specify a default value after a field name using `=`. Example:
`[[name=Anonymous]]`, `[^[greeting=Hello:Hello|Goodbye]^]`
- Use `{{variable_name}}` in the snippet to reference a form field.

## Rich Text Snippets

You may use Markdown or HTML to include rich text in your snippets.

- `replace`: (Default) Use plain text replacements.
- `markdown`: Markdown can be used in snippets.
- `html`: HTML can be used in snippets.

Notice that if you choose `markdown` or `html` and your snippet contains form input, the values from your form will also be interpreted as Markdown or HTML respectively.

## Paste/Silent Mode

When using `paste` mode (default), the snippet's replacement is printed. This
allows you to use `,,..` to add a new trigger and type at the same time, or 
`..,,` as the "paste" step of a disposable clipboard. **If a form is specified, 
nothing is printed as the output relies on user input.**

When using `silent` mode, nothing is printed. This is useful when you just want
to manage your snippets without writing them out.
