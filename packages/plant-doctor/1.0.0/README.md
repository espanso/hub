# Plant Doctor Health Briefs

Prepare better plant-health context wherever you type. This Espanso package helps
plant parents describe visible symptoms, take useful photos, check watering and
pest clues, and compare recovery observations. It supports the context-gathering
part of [Plant Doctor](https://plantdoctor.app)'s photo-based plant-health workflow.

It does **not** identify plants, analyze images, diagnose disease, prescribe
treatments, or connect to the app. All five shortcuts work locally, without an
account, API key, upload, analytics, shell command, or remote service.

## Shortcuts

| Type, then press Space | Result |
| --- | --- |
| `:pdbrief` | Form for plant, symptoms, onset, moisture, watering, light, drainage and recent changes |
| `:pdphotos` | Seven steps for clearer symptom photos and relevant care context |
| `:pdwatercheck` | Moisture and drainage observations without assuming wilting means thirst |
| `:pdpestcheck` | Visible-pest observation and photo checklist without prescribing treatment |
| `:pdfollowup` | Form to compare symptoms and care actions with a previous observation |

The two forms use Espanso's native text fields and choice boxes. Unchecked
moisture and drainage stay **Not checked**, rather than becoming an assumption.
Submit the form to insert the brief in the focused text field; Cancel closes it.
You choose whether and where to share the resulting text. No photos or notes
are sent anywhere by this package.

Try shortcuts in an empty scratch note first. As with any text expander, generated
text goes into the focused application. Avoid password fields, terminals and
one-line send boxes. Replacements deliberately have no trailing newline to reduce
accidental sends. Trigger words require a word boundary, so typing a longer word
such as `:pdbriefly` will not expand the brief.

General observation prompts are not a diagnosis. Species, environment and symptoms
matter; seek qualified advice for rapid decline or uncertain treatment risk.

## Install

Requires Espanso 2.x. Once approved on the Hub:

```sh
espanso install plant-doctor
```

Before Hub approval, download the release ZIP from
[the public source repository](https://github.com/zzheer/plant-doctor-espanso/releases),
extract it, and copy its `plant-doctor` folder into the directory shown by
`espanso path packages`. Reload Espanso using your normal workflow. Remove that
folder to uninstall a manual installation. After Hub installation, use
`espanso uninstall plant-doctor`. Neither action removes notes you already made.

## Publisher and privacy

Created by **Moruk LLC**, makers of [Plant Doctor](https://plantdoctor.app).
[About Plant Doctor and its developer](https://plantdoctor.app/about).
Contact: **hi@moruk.co**. MIT license. Version **1.0.0**.

This package only inserts local text. The privacy and data behavior of the app
where you insert or later share the text is separate. There are no automatic
links or promotional text in generated briefs and checklists.

Canonical source: https://gitlab.com/moruk-hq/plant-doctor-espanso
Public release mirror: https://github.com/zzheer/plant-doctor-espanso
