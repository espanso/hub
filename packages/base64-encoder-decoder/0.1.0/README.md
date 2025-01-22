## Base64 Encoder and Decoder

An Base64 Encoder and Decoder package for [espanso](https://espanso.org/) which provides triggers for encoding the clipboard to base64 and decoding base64 the clipboard contents.

### Usage

To use this package, just copy the text you want to encode or decode to the clipboard and type the following triggers:

- `:b64e` - Encode the clipboard contents to base64
- `:b64d` - Decode the clipboard contents from base64

### Examples

Encode:
- `Text to be encoded` -> `:b64e` -> `VGV4dCB0byBiZSBlbmNvZGVk`

Decode:
- `VGV4dCB0byBiZSBlbmNvZGVk` -> `:b64d` -> `Text to be encoded`

It's simple as that!

### Future Improvements

- [ ] Add support for encoding with form feed.
