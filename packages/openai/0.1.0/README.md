# Espanso package `openai`

A package for querying openai (chatGPT!) from anywhere on the system.

This is a package for [Espanso](https://espanso.org/), which is a free cross-platform text expander written in Rust.

## Dependencies
1. Requires `espanso`
2. Requires `jq`
3. Requires `curl`
4. Requires an [open ai](https://platform.openai.com) api key (anyone can make an account on openai and generate this for free)

## Installation instructions
1. Install this package.
2. Use `espanso path` to get the config path <PATH> and add `export CONFIG="<PATH>"` to your zsh/bash rc
3. Store the open ai api key in $CONFIG/openai_api_key (or create a sym link here).
4. Do `chmod u+x $CONFIG/match/packages/openai/openai.sh` to make the curl script executable. This curl script is based on a medium article [How to use GPT3 API with Curl](https://medium.com/geekculture/2022-how-to-use-chatgpt-api-with-curl-88830dec8a65).


## Usage
### Clipboard queries:
- `:ask-gpt` (queries the content of the clipboard)
- `:rephrase` (rephrases the content of the clipboard)
- `:correct` (corrects grammatical errors in the contents of the clipboard)
- `:fact-check` (fact checks the content of the clipboard)
- `:respond` (writes a response to the content of the clipboard)
- `:explain` (explain the content of the clipboard in detail)
- `:eli5` (explain the clipboard content to me like I am 5)
- `:summarize` (summarize the content of the clipboard)
- `:write` (write an article on the content of the clipboard)
- `:debug` (debug the code in the clipboard)
- `:grade` (grade the content of the clipboard)

### Regex queries
- `:Q/{query}//` (regex query, char limit 25)
  - Example: `Q/rust quicksort//` returns the following:
  ```rust
    fn quicksort(vec: &mut [i32]) {
        if vec.len() < 2 {
            return;
        }
        let pivot = vec.len() - 1;
        let mut pos = 0;
        for i in 0..pivot {
            if vec[i] <= vec[pivot] {
                vec.swap(i, pos);
                pos += 1;
            }
        }
        vec.swap(pivot, pos);
        quicksort(&mut vec[..pos]);
        quicksort(&mut vec[pos+1..]);
    }
    ```

## Package details

Repository: [https://github.com/rohitna/espanso-package-openai](https://github.com/rohitna/espanso-package-openai)