# Another UUID generation tool
This is a stand-in replacement for the `uuid` package that doesn't require Python. To prevent conflicts, you should make sure that `uuid` is not installed before adding `uuid-nix`.

Usage is exactly the same: `:uuid` creates a UUID with dashes, and `:nuuid` creates a UUID without dashes.

Note that this package only works on Linux distros and macOS; Windows (except when using WSL) is not currently supported.
