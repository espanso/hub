# RandTools

RandTools is a tool for espanso to generate random strings on the fly, which could be used in 
filling up random usernames/ passwords, generating API keys, etc.

This tool requires `openssl` to be installed on your system.

## Usage

`hrand{n};` generates a random string of length n, where n is an integer, using `openssl rand -hex`.

`brand{n};` generates a random string of length n, where n is an integer, using `openssl rand -base64`.

## Example
`hrand10;` -> `98a4c2179041ae37a8f5`