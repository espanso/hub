# UUID v4 Package for Espanso

### Please note that `python` is required to run this package.

Adds various UUID commands to Espanso.

Casing is preserved, so typing `:UUID` will generate a fully uppercase UUID.

* `:uuid` - Standard UUIDv4, lowercase
  * Ex: 79a455be-f7bf-4875-955a-459e16eda4de
* `:nuuid` - Standard UUIDv4, lowercase, without dashes
  * Ex: c03aeca4b8034f21a61add7fca8b1dc7

If you don't want to use Python for UUID generation, consider installing the [`uuid-nix`](https://hub.espanso.org/uuid-nix) package instead; it's a shell-based replacement for `uuid`.
