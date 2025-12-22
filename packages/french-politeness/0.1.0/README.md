# Espanso French Politeness Package

Improve your French communication experience using these snippet triggers.
A package of the most common and important French expressions.
Become more respectful in daily interactions.

## Installation

This package can be installed using the Espanso package manager:

```bash
espanso install french-politeness
```

Or manually by cloning this repository into your Espanso configuration folder.

## Usage

Type any trigger and it will be automatically replaced with the corresponding French expression. Most triggers support case propagation, meaning that if you type the trigger in uppercase, the replacement will also be in uppercase.

## Triggers

### Opening Expressions

| Trigger | Replacement | Notes |
| ------- | ----------- | ----- |
| bjr | bonjour | Case-sensitive (Bjr → Bonjour) |
| bapm | bonne après-midi | Case-sensitive (Bapm → Bonne Après-Midi) |
| bsr | bonsoir | Case-sensitive (Bsr → Bonsoir) |
| mr, m. | monsieur, | Case-sensitive (Mr → Monsieur,) |
| mme, mme. | madame, | Case-sensitive (Mme → Madame,) |
| mlle | mademoiselle, | Case-sensitive (Mlle → Mademoiselle,) |
| :cher | [[dear]] [[name]], | Interactive form (dear: Cher/Chère) |
| :alattde | À l'attention de [[name]], | Interactive form |
| slt | salut, | Case-sensitive (Slt → Salut,) |
| cc | coucou, | Case-sensitive (Cc → Coucou,) |
| jqtb | J'espère que tu vas bien | |
| jqvb | J'espère que vous allez bien | |

### Closure Expressions

| Trigger | Replacement |
| ------- | ----------- |
| bat | Bien à toi, |
| bav | Bien à vous, |
| cdt | Cordialement, |
| sltd | Salutations distinguées, |
| eslt | En vous envoyant mes salutations distinguées, |
| aslt | Avec l'expression de mes salutations distinguées, |
| rsp | Respectueusement, |
| scr | Sincèrement, |
| sslt | Sincères salutations, |
| amslt | Avec mes meilleures salutations, |
| mpat | Merci pour votre attention, |
| attret | Dans l'attente de votre retour, |

## Features

- **Case Propagation**: Most triggers support automatic case propagation. Type "Bjr" to get "Bonjour" or "bjr" to get "bonjour".
- **Word Boundary Detection**: Triggers only activate when typed as complete words, preventing unwanted replacements.
- **Interactive Forms**: Some triggers like `:cher` and `:alattde` open interactive forms to customize the output.

## License

This package is licensed under the Apache License 2.0. See the LICENSE file for details.

---
