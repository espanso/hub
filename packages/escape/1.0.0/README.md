# Escape Text

A simple Espanso package for encoding and decoding various common escape formats in programming (JSON, XML, URL-encoding, regular expressions)

## Requirements

- Python 3.x
- Espanso 2.x or higher

## Installation

```
espanso install escape
```

## Usage

### Encoding

All encoding triggers start with `>>`

|  Trigger  | Conversion |
|-----------|---------|
| `>>json` | Text -> JSON/backslash |
| `>>xml` | Text -> XML |
| `>>url` | Text -> URL encoding |
| `>>regex` | Text -> Regular expression literal |

### Decoding

All decoding triggers start with `<<`

|  Trigger  | Conversion |
|-----------|---------|
| `<<json` | JSON/backslash -> Text |
| `<<xml` | XML -> Text |
| `<<url` | URL encoding -> Text |
