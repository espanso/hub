# README

`english-lorem` is a simple package to generate random lorem ipsum sentences
or paragraphs but in English! This is based on the lorem package.

The text is based on [Harris Rackham's 1914 translation](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cicero/de_Finibus/home.html) of Cicero's work "De finibus bonorum et malorum"
(On the Extremes of Good and Evil).

### Installation

```
espanso install english-lorem
```

### Usage

Sentences are generated using the format `>elorem`.

|   Trigger  |    Replace   |
|------------|--------------|
| `>elorem`  | 1 sentence.  |
| `>2elorem` | 2 sentences. |
| `>3elorem` | 3 sentences. |
| `>4elorem` | 4 sentences. |

<br>

Paragraphs are generated using the format `#elorem`.

|   Trigger   |    Replace    |
|-------------|---------------|
| `#elorem`   | 1 paragraph.  |
| `#2elorem`  | 2 paragraphs. |
| `#3elorem`  | 3 paragraphs. |
| `#4elorem`  | 4 paragraphs. |