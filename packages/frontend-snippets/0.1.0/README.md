# frontend-snippets

Make frontend easier and less time-consuming with this [Espanso](https://espanso.org/) package!

Forked from the html-utils-package with additional matches added.

# Triggers

## HTML

| Trigger            | Result                                                                       |
| ------------------ | ---------------------------------------------------------------------------- |
| `::docskel`        | Generates an empty document with `utf-8` and `viewport` headers (unindented) |
| `::doctype`        | `<!DOCTYPE html>`                                                            |
| `::charset`        | `<meta charset="">`                                                          |
| `::utf-8`          | `<meta charset="UTF-8">`                                                     |
| `::viewport`       | `<meta name="viewport" content="width=device-width, initial-scale=1">`       |
| `::meta-author`    | `<meta name="author" content="">`                                            |
| `::meta-desc`      | `<meta name="description" content="">`                                       |
| `::meta-keywords`  | `<meta name="keywords" content="">`                                          |
| `::title`          | `<title></title>`                                                            |
| `::div`            | `<div></div>`                                                                |
| `::html`           | `<html></html>`                                                              |
| `::head`           | `<head></head>`                                                              |
| `::body`           | `<body></body>`                                                              |
| `::a`              | `<a href=""></a>`                                                            |
| `::br`             | `<br>`                                                                       |
| `::button`         | `<button type="button"></button> `                                           |
| `::style`          | `<style></style>`                                                            |
| `::css`            | `<link rel="stylesheet" type="text/css" href="">`                            |
| `::script`         | `<script></script>`                                                          |
| `::js`             | `<script type="text/javascript" src=""></script>`                            |
| `::form`           | `<form action="" method=""></form>`                                          |
| `::label`          | `<label for=""></label>`                                                     |
| `::submit`         | `<input type="submit" value="">`                                             |
| `::img`            | `<img src="" alt="">`                                                        |
| `::input-text`     | `<input type="text" name="" id="">`                                          |
| `::input-password` | `<input type="password" name="" id="">`                                      |
| `::input-radio`    | `<input type="radio" name="" id="" value="">`                                |
| `::input-checkbox` | `<input type="checkbox" name="" id="" value="">`                             |
| `::input-file`     | `<input type="file" name="" id="">`                                          |

## JavaScript

| Trigger     | Result                            |
| ----------- | --------------------------------- |
| `::while`   | `while (){ }`                     |
| `::forup`   | `for (let i = 0; i < __; i++){ }` |
| `::fordown` | `for (let i = 0; i >= 0; i--){ }` |

## React

| Trigger   | Result                                                                                                                         |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `::rfcep` | Generates a React functional component with default props, prop types, and default export. Does **not** autogenerate the name. |

# Contributions

If you feel like there's any important tag/snippet missing, feel free to create a Pull Request or open an [Issue](https://github.com/irasanchez/frontend-snippets/issues/new).
