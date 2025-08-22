# nsIPsum – Network Security Ipsum for Espanso

**nsIPsum** is an [Espanso](https://espanso.org) package that generates randomized, lorem-ipsum style filler text with a networking and security theme.  
It’s useful for creating mock documentation, demo configs, lab write-ups, or test fixtures where placeholder text is needed.  

---

## ✨ Features
- 100+ unique filler sentences inspired by networking, Cisco, and security concepts.  
- Generate 1–4 random sentences at a time.  
- Generate full paragraphs (5+ random sentences each).  
- Chaos mode: random length sentences or paragraphs for maximum variety.  
- Plug-and-play with Espanso, no extra setup.

---

## ⌨️ Usage

Type one of the triggers in any text field and Espanso will expand it:

### Sentences
- `:nsipsum` → one random sentence  
- `:2nsipsum`, `:3nsipsum`, `:4nsipsum` → multiple sentences  

### Paragraphs
- `:pnsipsum` → one paragraph (5+ random sentences)  
- `:2pnsipsum`, `:3pnsipsum`, `:4pnsipsum` → multiple paragraphs  

### Chaos
- `:rnsipsum` → 1–4 random sentences  
- `:rpnsipsum` → 1–4 random paragraphs
- 
## 📂 Example

Typing `:pnsipsum` might expand into:

```
BGP graviter sapit super backbone, dum route reflector sermonem repetit.
QoS oracula decernunt quis packetum primus transeat; VoIP tamen praeferendum est.
IDS vigilans somniat signaturas veteres et novas comparat.
Tor stratis cepae lacrimas parit; anonymitas pretium est.
Zabbix omnia scrutatur; alert fatigue disciplina mitigat.
```

## ⚠️ Disclaimer

This project is intended for educational and demonstration use only.
It produces filler text, not functional commands or configurations.
It should never be used as real configuration for live systems.

## 📜 License

MIT License

Copyright (c) 2025 Steven

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
