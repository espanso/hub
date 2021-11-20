# espanso-package-sharewifi

An espanso package for quickly sharing Wi-Fi passwords and connection details on macOS using [sharewifi](https://github.com/bradyjoslin/sharewifi). Generates QR codes that auto-configure iOS and Android devices. [Espanso](https://espanso.org/) is a free cross-platform text expander written in Rust.

![sharewifi](./images/sharewifi.gif)

For more information about espanso packages, read the [documentation](https://espanso.org/docs/).

## Usage

Available replacements:

| replacement    | description                                                  |
| -------------- | ------------------------------------------------------------ |
| `:sharewifi`   | Prints Wi-Fi password.                                       |
| `:qrsharewifi` | Prints Wi-Fi Network config QR Code for Android and iOS 11+. |
| `:vsharewifi`  | Verbose output. Prints SSID and Password.                    |

For proper formatting of qr codes when using `:qrsharewifi`, trigger the replacement in a plain text editor.

## Installation

`espanso install sharewifi`

## Dependencies

Requires [sharewifi](https://github.com/bradyjoslin/sharewifi).

## Package Details

Repository: [https://github.com/bradyjoslin/espanso-package-sharewifi/](https://github.com/bradyjoslin/espanso-package-sharewifi/)