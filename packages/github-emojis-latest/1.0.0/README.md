# We developers love GitHub Emojis!

All emojis supported by GitHub can be found here: [comprehensive list](https://api.github.com/emojis). This package is automatically generate by a home-brewed Bash script. It's accurate and synchronized with official GitHub emoji list.

The following syntax is chosen for the ease of typing:

> `;smile;` → 😄
> `;ringed planet;` → 🪐

## East Asian character emojis ㊗️ 🈶️ 🈯️ 🈳️

Quick primer on written Japanese characters. There are 3 character types: Hiragana, Katakana and Kanji. Hiragana and Katakana are syllabary, which means they represent the sounds that make up the words.

Hiragana is curved and flowing, and mainly used for native Japanese words and word-endings. Katakana is simple and angular, and mainly used for writing of loanwords, scientific or technical terms. Kanji are Han characters, adopted from Chinese characters. Now that that’s out of the way, here we go.

- 🈁️ Japanese “here” button
- 🈂️ Japanese “service charge” button
- 🈷️ Japanese “monthly amount” button
- 🈶️ Japanese “not free of charge” button
- 🈯️ Japanese “reserved” button
- 🉐️ Japanese “bargain” button
- 🈹️ Japanese “discount” button
- 🈚️ Japanese “free of charge” button
- 🈲️ Japanese “prohibited” button
- 🉑️ Japanese “acceptable” button
- 🈸️ Japanese “application” button
- 🈴️ Japanese “passing grade” button
- 🈳️ Japanese “vacancy” button
- ㊗️ Japanese “congratulations” button
- ㊙️ Japanese “secret” button
- 🈺️ Japanese “open for business” button
- 🈵️ Japanese “no vacancy” button

[🔗 Read more background info](https://chenhuijing.com/blog/east-asian-character-emojis/#👾)

Some of these Japanese button emojis don't have proper names, but only codes like 'u5272'. To make the trigger more understandable, let's use following names as triggers:

- u5272 → 🈹 discount
- u5408 → 🈴 passed
- u55b6 → 🈺 opening
- u6307 → 🈯 reserved
- u6708 → 🈷️ monthly
- u6709 → 🈶 paid
- u6e80 → 🈵 occupied
- u7121 → 🈚 free2
- u7533 → 🈸 application
- u7981 → 🈲 prohibited
- u7a7a → 🈳 vacant

For example, you type `;reserved;` to get 🈯

## We use Unicode format

You'll notice that when using emojis in commits, it's possible to use either the shortcode or the unicode format.

The difference between both is that the unicode represents the emoji itself while the shortcode is a text representation of the emoji that will be converted to the unicode character when rendered on a Git platform, such as GitHub, GitLab etc. We prefer to use Unicode in this package to get the most out of espanso text expansion easeness.

### Shortcode vs Unicode format

**Unicode**

| Pros ✅                                                        | Cons ❌                                                      |
| :------------------------------------------------------------- | :----------------------------------------------------------- |
| It represents the actual emoji no external systems are needed. | Might not be supported in all terminals / operating systems. |
| Better git log.                                                | Shortcode                                                    |
| Easier to type.                                                |                                                              |
| Takes less characters of the commit title.                     |                                                              |

**Shortcode**

| Pros ✅                                                          | Cons ❌                                                                                                           |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Supported everywhere as it's a text representation of the emoji. | You'll need a platform / system that knows how to properly render the shortcode.                                  |
|                                                                  | Different platforms / systems might use different shortcode namings, eg: GitHub and GitLab have some differences. |
|                                                                  | Takes more characters of the commit title.                                                                        |

## Caveat

These exclusively created emojis by GitHub don't have their unicodes, and they aren't compatable with most platforms. They are excluded by this package. If you type ";basecamp;", you'll get "N/A", which means it's not available.

- accessibility
- atom
- basecamp
- basecampy
- bowtie
- dependabot
- electron
- feelsgood
- finnadie
- fishsticks
- goberserk
- godmode
- hurtrealbad
- neckbeard
- octocat
- rage1
- rage2
- rage3
- rage4
- shipit
- suspect
- trollface

## dmoji (d for Developer)

We picked `dmoji` as trigger word, no `;` or `:`, since it's a made-up word and should seldom conflict with others. `dmoji` wakes up a search box, you can input the emoji's name or words from its related usage description to find it.

For example, you're writing a git commit message, and it's about adding new features to your product, just search: `feature` or `new` or `sparkle`, use any of them to locate the ✨ emoji quickly!

| emoji | name                      | usage description                                             |
| ----- | ------------------------- | ------------------------------------------------------------- |
| 🎨    | art                       | Improve structure / format of the code.                       |
| ⚡️   | zap                       | Improve performance.                                          |
| 🔥    | fire                      | Remove code or files.                                         |
| 🐛    | bug                       | Fix a bug.                                                    |
| 🚑️   | ambulance                 | Critical hotfix.                                              |
| ✨    | sparkles                  | Introduce new features.                                       |
| 📝    | memo                      | Add or update documentation.                                  |
| 🚀    | rocket                    | Deploy stuff.                                                 |
| 💄    | lipstick                  | Add or update the UI and style files.                         |
| 🎉    | tada                      | Begin a project.                                              |
| ✅    | white_check_mark          | Add, update, or pass tests.                                   |
| 🔒️   | lock                      | Fix security or privacy issues.                               |
| 🔐    | closed_lock_with_key      | Add or update secrets.                                        |
| 🔖    | bookmark                  | Release / Version tags.                                       |
| 🚨    | rotating_light            | Fix compiler / linter warnings.                               |
| 🚧    | construction              | Work in progress.                                             |
| 💚    | green_heart               | Fix CI Build.                                                 |
| ⬇️    | arrow_down                | Downgrade dependencies.                                       |
| ⬆️    | arrow_up                  | Upgrade dependencies.                                         |
| 📌    | pushpin                   | Pin dependencies to specific versions.                        |
| 👷    | construction_worker       | Add or update CI build system.                                |
| 📈    | chart_with_upwards_trend  | Add or update analytics or track code.                        |
| ♻️    | recycle                   | Refactor code.                                                |
| ➕    | heavy_plus_sign           | Add a dependency.                                             |
| ➖    | heavy_minus_sign          | Remove a dependency.                                          |
| 🔧    | wrench                    | Add or update configuration files.                            |
| 🔨    | hammer                    | Add or update development scripts.                            |
| 🌐    | globe_with_meridians      | Internationalization and localization.                        |
| ✏️    | pencil2                   | Fix typos.                                                    |
| 💩    | poop                      | Write bad code that needs to be improved.                     |
| ⏪️   | rewind                    | Revert changes.                                               |
| 🔀    | twisted_rightwards_arrows | Merge branches.                                               |
| 📦️   | package                   | Add or update compiled files or packages.                     |
| 👽️   | alien                     | Update code due to external API changes.                      |
| 🚚    | truck                     | Move or rename resources (e.g.: files, paths, routes).        |
| 📄    | page_facing_up            | Add or update license.                                        |
| 💥    | boom                      | Introduce breaking changes.                                   |
| 🍱    | bento                     | Add or update assets.                                         |
| ♿️   | wheelchair                | Improve accessibility.                                        |
| 💡    | bulb                      | Add or update comments in source code.                        |
| 🍻    | beers                     | Write code drunkenly.                                         |
| 💬    | speech_balloon            | Add or update text and literals.                              |
| 🗃️    | card_file_box             | Perform database related changes.                             |
| 🔊    | loud_sound                | Add or update logs.                                           |
| 🔇    | mute                      | Remove logs.                                                  |
| 👥    | busts_in_silhouette       | Add or update contributor(s).                                 |
| 🚸    | children_crossing         | Improve user experience / usability.                          |
| 🏗️    | building_construction     | Make architectural changes.                                   |
| 📱    | iphone                    | Work on responsive design.                                    |
| 🤡    | clown_face                | Mock things.                                                  |
| 🥚    | egg                       | Add or update an easter egg.                                  |
| 🙈    | see_no_evil               | Add or update a .gitignore file.                              |
| 📸    | camera_flash              | Add or update snapshots.                                      |
| ⚗️    | alembic                   | Perform experiments.                                          |
| 🔍️   | mag                       | Improve SEO.                                                  |
| 🏷️    | label                     | Add or update types.                                          |
| 🌱    | seedling                  | Add or update seed files.                                     |
| 🚩    | triangular_flag_on_post   | Add, update, or remove feature flags.                         |
| 🥅    | goal_net                  | Catch errors.                                                 |
| 💫    | dizzy                     | Add or update animations and transitions.                     |
| 🗑️    | wastebasket               | Deprecate code that needs to be cleaned up.                   |
| 🛂    | passport_control          | Work on code related to authorization, roles and permissions. |
| 🩹    | adhesive_bandage          | Simple fix for a non-critical issue.                          |
| 🧐    | monocle_face              | Data exploration/inspection.                                  |
| ⚰️    | coffin                    | Remove dead code.                                             |
| 🧪    | test_tube                 | Add a failing test.                                           |
| 👔    | necktie                   | Add or update business logic.                                 |
| 🩺    | stethoscope               | Add or update healthcheck.                                    |
| 🧱    | bricks                    | Infrastructure related changes.                               |
| 🧑‍💻    | technologist              | Improve developer experience.                                 |
| 💸    | money_with_wings          | Add sponsorships or money related infrastructure.             |
| 🧵    | thread                    | Add or update code related to multithreading or concurrency.  |
| 🦺    | safety_vest               | Add or update code related to validation.                     |

## Table of Contents (🔖 Bookmark this)

We love emojis but can't memorize them all, afterall they are a huge amount. It's good to have a comprehensive list to check from time to time!

> 🚧 Just use `; emoji name ;` for ease of typing! And seperate multiple words with space, rather than underscores.

- [Smileys & Emotion](#smileys--emotion)
- [People & Body](#people--body)
- [Animals & Nature](#animals--nature)
- [Food & Drink](#food--drink)
- [Travel & Places](#travel--places)
- [Activities](#activities)
- [Objects](#objects)
- [Symbols](#symbols)
- [Flags](#flags)
- [GitHub Custom Emoji](#github-custom-emoji)

### Smileys & Emotion

- [Face Smiling](#face-smiling)
- [Face Affection](#face-affection)
- [Face Tongue](#face-tongue)
- [Face Hand](#face-hand)
- [Face Neutral Skeptical](#face-neutral-skeptical)
- [Face Sleepy](#face-sleepy)
- [Face Unwell](#face-unwell)
- [Face Hat](#face-hat)
- [Face Glasses](#face-glasses)
- [Face Concerned](#face-concerned)
- [Face Negative](#face-negative)
- [Face Costume](#face-costume)
- [Cat Face](#cat-face)
- [Monkey Face](#monkey-face)
- [Heart](#heart)
- [Emotion](#emotion)

#### Face Smiling

|                          |           ico           | shortcode                         |        ico         | shortcode            |                           |
| ------------------------ | :---------------------: | --------------------------------- | :----------------: | -------------------- | ------------------------- |
| [TOC](#smileys--emotion) |       :grinning:        | `:grinning:`                      |      :smiley:      | `:smiley:`           | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |         :smile:         | `:smile:`                         |       :grin:       | `:grin:`             | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :laughing:        | `:laughing:` <br /> `:satisfied:` |   :sweat_smile:    | `:sweat_smile:`      | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |         :rofl:          | `:rofl:`                          |       :joy:        | `:joy:`              | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :slightly_smiling_face: | `:slightly_smiling_face:`         | :upside_down_face: | `:upside_down_face:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |         :wink:          | `:wink:`                          |      :blush:       | `:blush:`            | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :innocent:        | `:innocent:`                      |                    |                      | [TOC](#table-of-contents) |

#### Face Affection

|                          |               ico                | shortcode                          |          ico           | shortcode                |                           |
| ------------------------ | :------------------------------: | ---------------------------------- | :--------------------: | ------------------------ | ------------------------- |
| [TOC](#smileys--emotion) | :smiling_face_with_three_hearts: | `:smiling_face_with_three_hearts:` |      :heart_eyes:      | `:heart_eyes:`           | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |          :star_struck:           | `:star_struck:`                    |    :kissing_heart:     | `:kissing_heart:`        | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |            :kissing:             | `:kissing:`                        |       :relaxed:        | `:relaxed:`              | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |      :kissing_closed_eyes:       | `:kissing_closed_eyes:`            | :kissing_smiling_eyes: | `:kissing_smiling_eyes:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |     :smiling_face_with_tear:     | `:smiling_face_with_tear:`         |                        |                          | [TOC](#table-of-contents) |

#### Face Tongue

|                          |              ico               | shortcode                        |        ico         | shortcode            |                           |
| ------------------------ | :----------------------------: | -------------------------------- | :----------------: | -------------------- | ------------------------- |
| [TOC](#smileys--emotion) |             :yum:              | `:yum:`                          | :stuck_out_tongue: | `:stuck_out_tongue:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :stuck_out_tongue_winking_eye: | `:stuck_out_tongue_winking_eye:` |    :zany_face:     | `:zany_face:`        | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :stuck_out_tongue_closed_eyes: | `:stuck_out_tongue_closed_eyes:` | :money_mouth_face: | `:money_mouth_face:` | [TOC](#table-of-contents) |

#### Face Hand

|                          |       ico       | shortcode         |        ico        | shortcode           |                           |
| ------------------------ | :-------------: | ----------------- | :---------------: | ------------------- | ------------------------- |
| [TOC](#smileys--emotion) |     :hugs:      | `:hugs:`          | :hand_over_mouth: | `:hand_over_mouth:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :shushing_face: | `:shushing_face:` |    :thinking:     | `:thinking:`        | [TOC](#table-of-contents) |

#### Face Neutral Skeptical

|                          |         ico         | shortcode             |       ico        | shortcode          |                           |
| ------------------------ | :-----------------: | --------------------- | :--------------: | ------------------ | ------------------------- |
| [TOC](#smileys--emotion) | :zipper_mouth_face: | `:zipper_mouth_face:` | :raised_eyebrow: | `:raised_eyebrow:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |   :neutral_face:    | `:neutral_face:`      | :expressionless: | `:expressionless:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |     :no_mouth:      | `:no_mouth:`          | :face_in_clouds: | `:face_in_clouds:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :smirk:       | `:smirk:`             |    :unamused:    | `:unamused:`       | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |     :roll_eyes:     | `:roll_eyes:`         |   :grimacing:    | `:grimacing:`      | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |   :face_exhaling:   | `:face_exhaling:`     |   :lying_face:   | `:lying_face:`     | [TOC](#table-of-contents) |

#### Face Sleepy

|                          |    ico     | shortcode    |       ico       | shortcode         |                           |
| ------------------------ | :--------: | ------------ | :-------------: | ----------------- | ------------------------- |
| [TOC](#smileys--emotion) | :relieved: | `:relieved:` |    :pensive:    | `:pensive:`       | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |  :sleepy:  | `:sleepy:`   | :drooling_face: | `:drooling_face:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :sleeping: | `:sleeping:` |                 |                   | [TOC](#table-of-contents) |

#### Face Unwell

|                          |           ico            | shortcode                  |           ico           | shortcode                 |                           |
| ------------------------ | :----------------------: | -------------------------- | :---------------------: | ------------------------- | ------------------------- |
| [TOC](#smileys--emotion) |          :mask:          | `:mask:`                   | :face_with_thermometer: | `:face_with_thermometer:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :face_with_head_bandage: | `:face_with_head_bandage:` |    :nauseated_face:     | `:nauseated_face:`        | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |     :vomiting_face:      | `:vomiting_face:`          |     :sneezing_face:     | `:sneezing_face:`         | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |        :hot_face:        | `:hot_face:`               |       :cold_face:       | `:cold_face:`             | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :woozy_face:       | `:woozy_face:`             |      :dizzy_face:       | `:dizzy_face:`            | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :face_with_spiral_eyes:  | `:face_with_spiral_eyes:`  |    :exploding_head:     | `:exploding_head:`        | [TOC](#table-of-contents) |

#### Face Hat

|                          |        ico        | shortcode           |       ico       | shortcode         |                           |
| ------------------------ | :---------------: | ------------------- | :-------------: | ----------------- | ------------------------- |
| [TOC](#smileys--emotion) | :cowboy_hat_face: | `:cowboy_hat_face:` | :partying_face: | `:partying_face:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :disguised_face:  | `:disguised_face:`  |                 |                   | [TOC](#table-of-contents) |

#### Face Glasses

|                          |      ico       | shortcode        |     ico     | shortcode     |                           |
| ------------------------ | :------------: | ---------------- | :---------: | ------------- | ------------------------- |
| [TOC](#smileys--emotion) |  :sunglasses:  | `:sunglasses:`   | :nerd_face: | `:nerd_face:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :monocle_face: | `:monocle_face:` |             |               | [TOC](#table-of-contents) |

#### Face Concerned

|                          |           ico            | shortcode                  |           ico           | shortcode                 |                           |
| ------------------------ | :----------------------: | -------------------------- | :---------------------: | ------------------------- | ------------------------- |
| [TOC](#smileys--emotion) |        :confused:        | `:confused:`               |        :worried:        | `:worried:`               | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :slightly_frowning_face: | `:slightly_frowning_face:` |     :frowning_face:     | `:frowning_face:`         | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :open_mouth:       | `:open_mouth:`             |        :hushed:         | `:hushed:`                | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :astonished:       | `:astonished:`             |        :flushed:        | `:flushed:`               | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |     :pleading_face:      | `:pleading_face:`          |       :frowning:        | `:frowning:`              | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :anguished:        | `:anguished:`              |        :fearful:        | `:fearful:`               | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :cold_sweat:       | `:cold_sweat:`             | :disappointed_relieved: | `:disappointed_relieved:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |          :cry:           | `:cry:`                    |          :sob:          | `:sob:`                   | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |         :scream:         | `:scream:`                 |      :confounded:       | `:confounded:`            | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :persevere:        | `:persevere:`              |     :disappointed:      | `:disappointed:`          | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |         :sweat:          | `:sweat:`                  |         :weary:         | `:weary:`                 | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :tired_face:       | `:tired_face:`             |     :yawning_face:      | `:yawning_face:`          | [TOC](#table-of-contents) |

#### Face Negative

|                          |      ico      | shortcode       |          ico           | shortcode                |                           |
| ------------------------ | :-----------: | --------------- | :--------------------: | ------------------------ | ------------------------- |
| [TOC](#smileys--emotion) |   :triumph:   | `:triumph:`     |         :pout:         | `:pout:` <br /> `:rage:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |    :angry:    | `:angry:`       |     :cursing_face:     | `:cursing_face:`         | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :smiling_imp: | `:smiling_imp:` |         :imp:          | `:imp:`                  | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |    :skull:    | `:skull:`       | :skull_and_crossbones: | `:skull_and_crossbones:` | [TOC](#table-of-contents) |

#### Face Costume

|                          |       ico       | shortcode                                  |        ico        | shortcode           |                           |
| ------------------------ | :-------------: | ------------------------------------------ | :---------------: | ------------------- | ------------------------- |
| [TOC](#smileys--emotion) |    :hankey:     | `:hankey:` <br /> `:poop:` <br /> `:shit:` |   :clown_face:    | `:clown_face:`      | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :japanese_ogre: | `:japanese_ogre:`                          | :japanese_goblin: | `:japanese_goblin:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |     :ghost:     | `:ghost:`                                  |      :alien:      | `:alien:`           | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :space_invader: | `:space_invader:`                          |      :robot:      | `:robot:`           | [TOC](#table-of-contents) |

#### Cat Face

|                          |      ico      | shortcode       |        ico        | shortcode           |                           |
| ------------------------ | :-----------: | --------------- | :---------------: | ------------------- | ------------------------- |
| [TOC](#smileys--emotion) | :smiley_cat:  | `:smiley_cat:`  |    :smile_cat:    | `:smile_cat:`       | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |   :joy_cat:   | `:joy_cat:`     | :heart_eyes_cat:  | `:heart_eyes_cat:`  | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |  :smirk_cat:  | `:smirk_cat:`   |   :kissing_cat:   | `:kissing_cat:`     | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :scream_cat:  | `:scream_cat:`  | :crying_cat_face: | `:crying_cat_face:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :pouting_cat: | `:pouting_cat:` |                   |                     | [TOC](#table-of-contents) |

#### Monkey Face

|                          |       ico       | shortcode         |      ico       | shortcode        |                           |
| ------------------------ | :-------------: | ----------------- | :------------: | ---------------- | ------------------------- |
| [TOC](#smileys--emotion) |  :see_no_evil:  | `:see_no_evil:`   | :hear_no_evil: | `:hear_no_evil:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :speak_no_evil: | `:speak_no_evil:` |                |                  | [TOC](#table-of-contents) |

#### Heart

|                          |        ico         | shortcode            |            ico            | shortcode                   |                           |
| ------------------------ | :----------------: | -------------------- | :-----------------------: | --------------------------- | ------------------------- |
| [TOC](#smileys--emotion) |   :love_letter:    | `:love_letter:`      |          :cupid:          | `:cupid:`                   | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |    :gift_heart:    | `:gift_heart:`       |     :sparkling_heart:     | `:sparkling_heart:`         | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |    :heartpulse:    | `:heartpulse:`       |        :heartbeat:        | `:heartbeat:`               | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :revolving_hearts: | `:revolving_hearts:` |       :two_hearts:        | `:two_hearts:`              | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :heart_decoration: | `:heart_decoration:` | :heavy_heart_exclamation: | `:heavy_heart_exclamation:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |   :broken_heart:   | `:broken_heart:`     |      :heart_on_fire:      | `:heart_on_fire:`           | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |  :mending_heart:   | `:mending_heart:`    |          :heart:          | `:heart:`                   | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |   :orange_heart:   | `:orange_heart:`     |      :yellow_heart:       | `:yellow_heart:`            | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |   :green_heart:    | `:green_heart:`      |       :blue_heart:        | `:blue_heart:`              | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |   :purple_heart:   | `:purple_heart:`     |       :brown_heart:       | `:brown_heart:`             | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |   :black_heart:    | `:black_heart:`      |       :white_heart:       | `:white_heart:`             | [TOC](#table-of-contents) |

#### Emotion

|                          |         ico          | shortcode              |         ico          | shortcode                     |                           |
| ------------------------ | :------------------: | ---------------------- | :------------------: | ----------------------------- | ------------------------- |
| [TOC](#smileys--emotion) |        :kiss:        | `:kiss:`               |        :100:         | `:100:`                       | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :anger:        | `:anger:`              |        :boom:        | `:boom:` <br /> `:collision:` | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |       :dizzy:        | `:dizzy:`              |    :sweat_drops:     | `:sweat_drops:`               | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |        :dash:        | `:dash:`               |        :hole:        | `:hole:`                      | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |   :speech_balloon:   | `:speech_balloon:`     | :eye_speech_bubble:  | `:eye_speech_bubble:`         | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) | :left_speech_bubble: | `:left_speech_bubble:` | :right_anger_bubble: | `:right_anger_bubble:`        | [TOC](#table-of-contents) |
| [TOC](#smileys--emotion) |  :thought_balloon:   | `:thought_balloon:`    |        :zzz:         | `:zzz:`                       | [TOC](#table-of-contents) |

### People & Body

- [Hand Fingers Open](#hand-fingers-open)
- [Hand Fingers Partial](#hand-fingers-partial)
- [Hand Single Finger](#hand-single-finger)
- [Hand Fingers Closed](#hand-fingers-closed)
- [Hands](#hands)
- [Hand Prop](#hand-prop)
- [Body Parts](#body-parts)
- [Person](#person)
- [Person Gesture](#person-gesture)
- [Person Role](#person-role)
- [Person Fantasy](#person-fantasy)
- [Person Activity](#person-activity)
- [Person Sport](#person-sport)
- [Person Resting](#person-resting)
- [Family](#family)
- [Person Symbol](#person-symbol)

#### Hand Fingers Open

|                      |                ico                 | shortcode                            |          ico          | shortcode                       |                           |
| -------------------- | :--------------------------------: | ------------------------------------ | :-------------------: | ------------------------------- | ------------------------- |
| [TOC](#people--body) |               :wave:               | `:wave:`                             | :raised_back_of_hand: | `:raised_back_of_hand:`         | [TOC](#table-of-contents) |
| [TOC](#people--body) | :raised_hand_with_fingers_splayed: | `:raised_hand_with_fingers_splayed:` |        :hand:         | `:hand:` <br /> `:raised_hand:` | [TOC](#table-of-contents) |
| [TOC](#people--body) |          :vulcan_salute:           | `:vulcan_salute:`                    |                       |                                 | [TOC](#table-of-contents) |

#### Hand Fingers Partial

|                      |        ico        | shortcode           |        ico         | shortcode            |                           |
| -------------------- | :---------------: | ------------------- | :----------------: | -------------------- | ------------------------- |
| [TOC](#people--body) |     :ok_hand:     | `:ok_hand:`         | :pinched_fingers:  | `:pinched_fingers:`  | [TOC](#table-of-contents) |
| [TOC](#people--body) |  :pinching_hand:  | `:pinching_hand:`   |        :v:         | `:v:`                | [TOC](#table-of-contents) |
| [TOC](#people--body) | :crossed_fingers: | `:crossed_fingers:` | :love_you_gesture: | `:love_you_gesture:` | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :metal:      | `:metal:`           |   :call_me_hand:   | `:call_me_hand:`     | [TOC](#table-of-contents) |

#### Hand Single Finger

|                      |     ico      | shortcode      |      ico      | shortcode                       |                           |
| -------------------- | :----------: | -------------- | :-----------: | ------------------------------- | ------------------------- |
| [TOC](#people--body) | :point_left: | `:point_left:` | :point_right: | `:point_right:`                 | [TOC](#table-of-contents) |
| [TOC](#people--body) | :point_up_2: | `:point_up_2:` |     :fu:      | `:fu:` <br /> `:middle_finger:` | [TOC](#table-of-contents) |
| [TOC](#people--body) | :point_down: | `:point_down:` |  :point_up:   | `:point_up:`                    | [TOC](#table-of-contents) |

#### Hand Fingers Closed

|                      |     ico     | shortcode                       |     ico      | shortcode                                               |                           |
| -------------------- | :---------: | ------------------------------- | :----------: | ------------------------------------------------------- | ------------------------- |
| [TOC](#people--body) |    :+1:     | `:+1:` <br /> `:thumbsup:`      |     :-1:     | `:-1:` <br /> `:thumbsdown:`                            | [TOC](#table-of-contents) |
| [TOC](#people--body) |   :fist:    | `:fist:` <br /> `:fist_raised:` | :facepunch:  | `:facepunch:` <br /> `:fist_oncoming:` <br /> `:punch:` | [TOC](#table-of-contents) |
| [TOC](#people--body) | :fist_left: | `:fist_left:`                   | :fist_right: | `:fist_right:`                                          | [TOC](#table-of-contents) |

#### Hands

|                      |     ico      | shortcode      |         ico         | shortcode             |                           |
| -------------------- | :----------: | -------------- | :-----------------: | --------------------- | ------------------------- |
| [TOC](#people--body) |    :clap:    | `:clap:`       |   :raised_hands:    | `:raised_hands:`      | [TOC](#table-of-contents) |
| [TOC](#people--body) | :open_hands: | `:open_hands:` | :palms_up_together: | `:palms_up_together:` | [TOC](#table-of-contents) |
| [TOC](#people--body) | :handshake:  | `:handshake:`  |       :pray:        | `:pray:`              | [TOC](#table-of-contents) |

#### Hand Prop

|                      |      ico       | shortcode        |     ico     | shortcode     |                           |
| -------------------- | :------------: | ---------------- | :---------: | ------------- | ------------------------- |
| [TOC](#people--body) | :writing_hand: | `:writing_hand:` | :nail_care: | `:nail_care:` | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :selfie:    | `:selfie:`       |             |               | [TOC](#table-of-contents) |

#### Body Parts

|                      |          ico           | shortcode                |        ico         | shortcode            |                           |
| -------------------- | :--------------------: | ------------------------ | :----------------: | -------------------- | ------------------------- |
| [TOC](#people--body) |        :muscle:        | `:muscle:`               |  :mechanical_arm:  | `:mechanical_arm:`   | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :mechanical_leg:    | `:mechanical_leg:`       |       :leg:        | `:leg:`              | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :foot:         | `:foot:`                 |       :ear:        | `:ear:`              | [TOC](#table-of-contents) |
| [TOC](#people--body) | :ear_with_hearing_aid: | `:ear_with_hearing_aid:` |       :nose:       | `:nose:`             | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :brain:         | `:brain:`                | :anatomical_heart: | `:anatomical_heart:` | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :lungs:         | `:lungs:`                |      :tooth:       | `:tooth:`            | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :bone:         | `:bone:`                 |       :eyes:       | `:eyes:`             | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :eye:          | `:eye:`                  |      :tongue:      | `:tongue:`           | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :lips:         | `:lips:`                 |                    |                      | [TOC](#table-of-contents) |

#### Person

|                      |         ico         | shortcode             |          ico          | shortcode                                      |                           |
| -------------------- | :-----------------: | --------------------- | :-------------------: | ---------------------------------------------- | ------------------------- |
| [TOC](#people--body) |       :baby:        | `:baby:`              |        :child:        | `:child:`                                      | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :boy:        | `:boy:`               |        :girl:         | `:girl:`                                       | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :adult:       | `:adult:`             | :blond_haired_person: | `:blond_haired_person:`                        | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :man:        | `:man:`               |   :bearded_person:    | `:bearded_person:`                             | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :man_beard:     | `:man_beard:`         |     :woman_beard:     | `:woman_beard:`                                | [TOC](#table-of-contents) |
| [TOC](#people--body) |  :red_haired_man:   | `:red_haired_man:`    |  :curly_haired_man:   | `:curly_haired_man:`                           | [TOC](#table-of-contents) |
| [TOC](#people--body) | :white_haired_man:  | `:white_haired_man:`  |      :bald_man:       | `:bald_man:`                                   | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :woman:       | `:woman:`             |  :red_haired_woman:   | `:red_haired_woman:`                           | [TOC](#table-of-contents) |
| [TOC](#people--body) |  :person_red_hair:  | `:person_red_hair:`   | :curly_haired_woman:  | `:curly_haired_woman:`                         | [TOC](#table-of-contents) |
| [TOC](#people--body) | :person_curly_hair: | `:person_curly_hair:` | :white_haired_woman:  | `:white_haired_woman:`                         | [TOC](#table-of-contents) |
| [TOC](#people--body) | :person_white_hair: | `:person_white_hair:` |     :bald_woman:      | `:bald_woman:`                                 | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :person_bald:    | `:person_bald:`       | :blond_haired_woman:  | `:blond_haired_woman:` <br /> `:blonde_woman:` | [TOC](#table-of-contents) |
| [TOC](#people--body) | :blond_haired_man:  | `:blond_haired_man:`  |     :older_adult:     | `:older_adult:`                                | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :older_man:     | `:older_man:`         |     :older_woman:     | `:older_woman:`                                | [TOC](#table-of-contents) |

#### Person Gesture

|                      |            ico            | shortcode                                                  |         ico          | shortcode                                 |                           |
| -------------------- | :-----------------------: | ---------------------------------------------------------- | :------------------: | ----------------------------------------- | ------------------------- |
| [TOC](#people--body) |     :frowning_person:     | `:frowning_person:`                                        |    :frowning_man:    | `:frowning_man:`                          | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :frowning_woman:      | `:frowning_woman:`                                         |    :pouting_face:    | `:pouting_face:`                          | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :pouting_man:       | `:pouting_man:`                                            |   :pouting_woman:    | `:pouting_woman:`                         | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :no_good:         | `:no_good:`                                                |       :ng_man:       | `:ng_man:` <br /> `:no_good_man:`         | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :ng_woman:         | `:ng_woman:` <br /> `:no_good_woman:`                      |     :ok_person:      | `:ok_person:`                             | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :ok_man:          | `:ok_man:`                                                 |      :ok_woman:      | `:ok_woman:`                              | [TOC](#table-of-contents) |
| [TOC](#people--body) | :information_desk_person: | `:information_desk_person:` <br /> `:tipping_hand_person:` |     :sassy_man:      | `:sassy_man:` <br /> `:tipping_hand_man:` | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :sassy_woman:       | `:sassy_woman:` <br /> `:tipping_hand_woman:`              |    :raising_hand:    | `:raising_hand:`                          | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :raising_hand_man:     | `:raising_hand_man:`                                       | :raising_hand_woman: | `:raising_hand_woman:`                    | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :deaf_person:       | `:deaf_person:`                                            |      :deaf_man:      | `:deaf_man:`                              | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :deaf_woman:        | `:deaf_woman:`                                             |        :bow:         | `:bow:`                                   | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :bowing_man:        | `:bowing_man:`                                             |    :bowing_woman:    | `:bowing_woman:`                          | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :facepalm:         | `:facepalm:`                                               |  :man_facepalming:   | `:man_facepalming:`                       | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :woman_facepalming:    | `:woman_facepalming:`                                      |       :shrug:        | `:shrug:`                                 | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :man_shrugging:      | `:man_shrugging:`                                          |  :woman_shrugging:   | `:woman_shrugging:`                       | [TOC](#table-of-contents) |

#### Person Role

|                      |             ico             | shortcode                         |            ico            | shortcode                                      |                           |
| -------------------- | :-------------------------: | --------------------------------- | :-----------------------: | ---------------------------------------------- | ------------------------- |
| [TOC](#people--body) |       :health_worker:       | `:health_worker:`                 |    :man_health_worker:    | `:man_health_worker:`                          | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :woman_health_worker:    | `:woman_health_worker:`           |         :student:         | `:student:`                                    | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :man_student:        | `:man_student:`                   |      :woman_student:      | `:woman_student:`                              | [TOC](#table-of-contents) |
| [TOC](#people--body) |          :teacher:          | `:teacher:`                       |       :man_teacher:       | `:man_teacher:`                                | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :woman_teacher:       | `:woman_teacher:`                 |          :judge:          | `:judge:`                                      | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :man_judge:         | `:man_judge:`                     |       :woman_judge:       | `:woman_judge:`                                | [TOC](#table-of-contents) |
| [TOC](#people--body) |          :farmer:           | `:farmer:`                        |       :man_farmer:        | `:man_farmer:`                                 | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :woman_farmer:        | `:woman_farmer:`                  |          :cook:           | `:cook:`                                       | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :man_cook:          | `:man_cook:`                      |       :woman_cook:        | `:woman_cook:`                                 | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :mechanic:          | `:mechanic:`                      |      :man_mechanic:       | `:man_mechanic:`                               | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :woman_mechanic:       | `:woman_mechanic:`                |     :factory_worker:      | `:factory_worker:`                             | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :man_factory_worker:     | `:man_factory_worker:`            |  :woman_factory_worker:   | `:woman_factory_worker:`                       | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :office_worker:       | `:office_worker:`                 |    :man_office_worker:    | `:man_office_worker:`                          | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :woman_office_worker:    | `:woman_office_worker:`           |        :scientist:        | `:scientist:`                                  | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :man_scientist:       | `:man_scientist:`                 |     :woman_scientist:     | `:woman_scientist:`                            | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :technologist:        | `:technologist:`                  |    :man_technologist:     | `:man_technologist:`                           | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :woman_technologist:     | `:woman_technologist:`            |         :singer:          | `:singer:`                                     | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :man_singer:         | `:man_singer:`                    |      :woman_singer:       | `:woman_singer:`                               | [TOC](#table-of-contents) |
| [TOC](#people--body) |          :artist:           | `:artist:`                        |       :man_artist:        | `:man_artist:`                                 | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :woman_artist:        | `:woman_artist:`                  |          :pilot:          | `:pilot:`                                      | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :man_pilot:         | `:man_pilot:`                     |       :woman_pilot:       | `:woman_pilot:`                                | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :astronaut:         | `:astronaut:`                     |      :man_astronaut:      | `:man_astronaut:`                              | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :woman_astronaut:      | `:woman_astronaut:`               |       :firefighter:       | `:firefighter:`                                | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :man_firefighter:      | `:man_firefighter:`               |    :woman_firefighter:    | `:woman_firefighter:`                          | [TOC](#table-of-contents) |
| [TOC](#people--body) |            :cop:            | `:cop:` <br /> `:police_officer:` |        :policeman:        | `:policeman:`                                  | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :policewoman:        | `:policewoman:`                   |        :detective:        | `:detective:`                                  | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :male_detective:       | `:male_detective:`                |    :female_detective:     | `:female_detective:`                           | [TOC](#table-of-contents) |
| [TOC](#people--body) |           :guard:           | `:guard:`                         |        :guardsman:        | `:guardsman:`                                  | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :guardswoman:        | `:guardswoman:`                   |          :ninja:          | `:ninja:`                                      | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :construction_worker:    | `:construction_worker:`           | :construction_worker_man: | `:construction_worker_man:`                    | [TOC](#table-of-contents) |
| [TOC](#people--body) | :construction_worker_woman: | `:construction_worker_woman:`     |         :prince:          | `:prince:`                                     | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :princess:          | `:princess:`                      |   :person_with_turban:    | `:person_with_turban:`                         | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :man_with_turban:      | `:man_with_turban:`               |    :woman_with_turban:    | `:woman_with_turban:`                          | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :man_with_gua_pi_mao:    | `:man_with_gua_pi_mao:`           |  :woman_with_headscarf:   | `:woman_with_headscarf:`                       | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :person_in_tuxedo:      | `:person_in_tuxedo:`              |      :man_in_tuxedo:      | `:man_in_tuxedo:`                              | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :woman_in_tuxedo:      | `:woman_in_tuxedo:`               |    :person_with_veil:     | `:person_with_veil:`                           | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :man_with_veil:       | `:man_with_veil:`                 |     :bride_with_veil:     | `:bride_with_veil:` <br /> `:woman_with_veil:` | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :pregnant_woman:       | `:pregnant_woman:`                |     :breast_feeding:      | `:breast_feeding:`                             | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :woman_feeding_baby:     | `:woman_feeding_baby:`            |    :man_feeding_baby:     | `:man_feeding_baby:`                           | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :person_feeding_baby:    | `:person_feeding_baby:`           |                           |                                                | [TOC](#table-of-contents) |

#### Person Fantasy

|                      |        ico         | shortcode            |         ico          | shortcode              |                           |
| -------------------- | :----------------: | -------------------- | :------------------: | ---------------------- | ------------------------- |
| [TOC](#people--body) |      :angel:       | `:angel:`            |       :santa:        | `:santa:`              | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :mrs_claus:     | `:mrs_claus:`        |      :mx_claus:      | `:mx_claus:`           | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :superhero:     | `:superhero:`        |   :superhero_man:    | `:superhero_man:`      | [TOC](#table-of-contents) |
| [TOC](#people--body) | :superhero_woman:  | `:superhero_woman:`  |    :supervillain:    | `:supervillain:`       | [TOC](#table-of-contents) |
| [TOC](#people--body) | :supervillain_man: | `:supervillain_man:` | :supervillain_woman: | `:supervillain_woman:` | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :mage:       | `:mage:`             |      :mage_man:      | `:mage_man:`           | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :mage_woman:    | `:mage_woman:`       |       :fairy:        | `:fairy:`              | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :fairy_man:     | `:fairy_man:`        |    :fairy_woman:     | `:fairy_woman:`        | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :vampire:      | `:vampire:`          |    :vampire_man:     | `:vampire_man:`        | [TOC](#table-of-contents) |
| [TOC](#people--body) |  :vampire_woman:   | `:vampire_woman:`    |     :merperson:      | `:merperson:`          | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :merman:      | `:merman:`           |      :mermaid:       | `:mermaid:`            | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :elf:        | `:elf:`              |      :elf_man:       | `:elf_man:`            | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :elf_woman:     | `:elf_woman:`        |       :genie:        | `:genie:`              | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :genie_man:     | `:genie_man:`        |    :genie_woman:     | `:genie_woman:`        | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :zombie:      | `:zombie:`           |     :zombie_man:     | `:zombie_man:`         | [TOC](#table-of-contents) |
| [TOC](#people--body) |   :zombie_woman:   | `:zombie_woman:`     |                      |                        | [TOC](#table-of-contents) |

#### Person Activity

|                      |               ico                | shortcode                          |              ico              | shortcode                           |                           |
| -------------------- | :------------------------------: | ---------------------------------- | :---------------------------: | ----------------------------------- | ------------------------- |
| [TOC](#people--body) |            :massage:             | `:massage:`                        |         :massage_man:         | `:massage_man:`                     | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :massage_woman:          | `:massage_woman:`                  |           :haircut:           | `:haircut:`                         | [TOC](#table-of-contents) |
| [TOC](#people--body) |          :haircut_man:           | `:haircut_man:`                    |        :haircut_woman:        | `:haircut_woman:`                   | [TOC](#table-of-contents) |
| [TOC](#people--body) |            :walking:             | `:walking:`                        |         :walking_man:         | `:walking_man:`                     | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :walking_woman:          | `:walking_woman:`                  |       :standing_person:       | `:standing_person:`                 | [TOC](#table-of-contents) |
| [TOC](#people--body) |          :standing_man:          | `:standing_man:`                   |       :standing_woman:        | `:standing_woman:`                  | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :kneeling_person:         | `:kneeling_person:`                |        :kneeling_man:         | `:kneeling_man:`                    | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :kneeling_woman:         | `:kneeling_woman:`                 |  :person_with_probing_cane:   | `:person_with_probing_cane:`        | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :man_with_probing_cane:      | `:man_with_probing_cane:`          |   :woman_with_probing_cane:   | `:woman_with_probing_cane:`         | [TOC](#table-of-contents) |
| [TOC](#people--body) | :person_in_motorized_wheelchair: | `:person_in_motorized_wheelchair:` | :man_in_motorized_wheelchair: | `:man_in_motorized_wheelchair:`     | [TOC](#table-of-contents) |
| [TOC](#people--body) | :woman_in_motorized_wheelchair:  | `:woman_in_motorized_wheelchair:`  | :person_in_manual_wheelchair: | `:person_in_manual_wheelchair:`     | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :man_in_manual_wheelchair:    | `:man_in_manual_wheelchair:`       | :woman_in_manual_wheelchair:  | `:woman_in_manual_wheelchair:`      | [TOC](#table-of-contents) |
| [TOC](#people--body) |             :runner:             | `:runner:` <br /> `:running:`      |         :running_man:         | `:running_man:`                     | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :running_woman:          | `:running_woman:`                  |           :dancer:            | `:dancer:` <br /> `:woman_dancing:` | [TOC](#table-of-contents) |
| [TOC](#people--body) |          :man_dancing:           | `:man_dancing:`                    |  :business_suit_levitating:   | `:business_suit_levitating:`        | [TOC](#table-of-contents) |
| [TOC](#people--body) |            :dancers:             | `:dancers:`                        |         :dancing_men:         | `:dancing_men:`                     | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :dancing_women:          | `:dancing_women:`                  |        :sauna_person:         | `:sauna_person:`                    | [TOC](#table-of-contents) |
| [TOC](#people--body) |           :sauna_man:            | `:sauna_man:`                      |         :sauna_woman:         | `:sauna_woman:`                     | [TOC](#table-of-contents) |
| [TOC](#people--body) |            :climbing:            | `:climbing:`                       |        :climbing_man:         | `:climbing_man:`                    | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :climbing_woman:         | `:climbing_woman:`                 |                               |                                     | [TOC](#table-of-contents) |

#### Person Sport

|                      |            ico             | shortcode                                           |           ico            | shortcode                                       |                           |
| -------------------- | :------------------------: | --------------------------------------------------- | :----------------------: | ----------------------------------------------- | ------------------------- |
| [TOC](#people--body) |      :person_fencing:      | `:person_fencing:`                                  |      :horse_racing:      | `:horse_racing:`                                | [TOC](#table-of-contents) |
| [TOC](#people--body) |          :skier:           | `:skier:`                                           |      :snowboarder:       | `:snowboarder:`                                 | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :golfing:          | `:golfing:`                                         |      :golfing_man:       | `:golfing_man:`                                 | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :golfing_woman:       | `:golfing_woman:`                                   |         :surfer:         | `:surfer:`                                      | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :surfing_man:        | `:surfing_man:`                                     |     :surfing_woman:      | `:surfing_woman:`                               | [TOC](#table-of-contents) |
| [TOC](#people--body) |         :rowboat:          | `:rowboat:`                                         |       :rowing_man:       | `:rowing_man:`                                  | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :rowing_woman:       | `:rowing_woman:`                                    |        :swimmer:         | `:swimmer:`                                     | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :swimming_man:       | `:swimming_man:`                                    |     :swimming_woman:     | `:swimming_woman:`                              | [TOC](#table-of-contents) |
| [TOC](#people--body) |   :bouncing_ball_person:   | `:bouncing_ball_person:`                            |     :basketball_man:     | `:basketball_man:` <br /> `:bouncing_ball_man:` | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :basketball_woman:     | `:basketball_woman:` <br /> `:bouncing_ball_woman:` |     :weight_lifting:     | `:weight_lifting:`                              | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :weight_lifting_man:    | `:weight_lifting_man:`                              |  :weight_lifting_woman:  | `:weight_lifting_woman:`                        | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :bicyclist:         | `:bicyclist:`                                       |       :biking_man:       | `:biking_man:`                                  | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :biking_woman:       | `:biking_woman:`                                    |   :mountain_bicyclist:   | `:mountain_bicyclist:`                          | [TOC](#table-of-contents) |
| [TOC](#people--body) |   :mountain_biking_man:    | `:mountain_biking_man:`                             | :mountain_biking_woman:  | `:mountain_biking_woman:`                       | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :cartwheeling:       | `:cartwheeling:`                                    |    :man_cartwheeling:    | `:man_cartwheeling:`                            | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :woman_cartwheeling:    | `:woman_cartwheeling:`                              |       :wrestling:        | `:wrestling:`                                   | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :men_wrestling:       | `:men_wrestling:`                                   |    :women_wrestling:     | `:women_wrestling:`                             | [TOC](#table-of-contents) |
| [TOC](#people--body) |        :water_polo:        | `:water_polo:`                                      | :man_playing_water_polo: | `:man_playing_water_polo:`                      | [TOC](#table-of-contents) |
| [TOC](#people--body) | :woman_playing_water_polo: | `:woman_playing_water_polo:`                        |    :handball_person:     | `:handball_person:`                             | [TOC](#table-of-contents) |
| [TOC](#people--body) |   :man_playing_handball:   | `:man_playing_handball:`                            | :woman_playing_handball: | `:woman_playing_handball:`                      | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :juggling_person:      | `:juggling_person:`                                 |      :man_juggling:      | `:man_juggling:`                                | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :woman_juggling:      | `:woman_juggling:`                                  |                          |                                                 | [TOC](#table-of-contents) |

#### Person Resting

|                      |          ico           | shortcode                |         ico          | shortcode              |                           |
| -------------------- | :--------------------: | ------------------------ | :------------------: | ---------------------- | ------------------------- |
| [TOC](#people--body) |    :lotus_position:    | `:lotus_position:`       | :lotus_position_man: | `:lotus_position_man:` | [TOC](#table-of-contents) |
| [TOC](#people--body) | :lotus_position_woman: | `:lotus_position_woman:` |        :bath:        | `:bath:`               | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :sleeping_bed:     | `:sleeping_bed:`         |                      |                        | [TOC](#table-of-contents) |

#### Family

|                      |              ico               | shortcode                        |               ico               | shortcode                         |                           |
| -------------------- | :----------------------------: | -------------------------------- | :-----------------------------: | --------------------------------- | ------------------------- |
| [TOC](#people--body) |     :people_holding_hands:     | `:people_holding_hands:`         |    :two_women_holding_hands:    | `:two_women_holding_hands:`       | [TOC](#table-of-contents) |
| [TOC](#people--body) |            :couple:            | `:couple:`                       |     :two_men_holding_hands:     | `:two_men_holding_hands:`         | [TOC](#table-of-contents) |
| [TOC](#people--body) |          :couplekiss:          | `:couplekiss:`                   |     :couplekiss_man_woman:      | `:couplekiss_man_woman:`          | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :couplekiss_man_man:      | `:couplekiss_man_man:`           |    :couplekiss_woman_woman:     | `:couplekiss_woman_woman:`        | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :couple_with_heart:       | `:couple_with_heart:`            |  :couple_with_heart_woman_man:  | `:couple_with_heart_woman_man:`   | [TOC](#table-of-contents) |
| [TOC](#people--body) |  :couple_with_heart_man_man:   | `:couple_with_heart_man_man:`    | :couple_with_heart_woman_woman: | `:couple_with_heart_woman_woman:` | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :family_man_woman_boy:     | `:family_man_woman_boy:`         |     :family_man_woman_girl:     | `:family_man_woman_girl:`         | [TOC](#table-of-contents) |
| [TOC](#people--body) |  :family_man_woman_girl_boy:   | `:family_man_woman_girl_boy:`    |   :family_man_woman_boy_boy:    | `:family_man_woman_boy_boy:`      | [TOC](#table-of-contents) |
| [TOC](#people--body) |  :family_man_woman_girl_girl:  | `:family_man_woman_girl_girl:`   |      :family_man_man_boy:       | `:family_man_man_boy:`            | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :family_man_man_girl:      | `:family_man_man_girl:`          |    :family_man_man_girl_boy:    | `:family_man_man_girl_boy:`       | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :family_man_man_boy_boy:    | `:family_man_man_boy_boy:`       |   :family_man_man_girl_girl:    | `:family_man_man_girl_girl:`      | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :family_woman_woman_boy:    | `:family_woman_woman_boy:`       |    :family_woman_woman_girl:    | `:family_woman_woman_girl:`       | [TOC](#table-of-contents) |
| [TOC](#people--body) | :family_woman_woman_girl_boy:  | `:family_woman_woman_girl_boy:`  |  :family_woman_woman_boy_boy:   | `:family_woman_woman_boy_boy:`    | [TOC](#table-of-contents) |
| [TOC](#people--body) | :family_woman_woman_girl_girl: | `:family_woman_woman_girl_girl:` |        :family_man_boy:         | `:family_man_boy:`                | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :family_man_boy_boy:      | `:family_man_boy_boy:`           |        :family_man_girl:        | `:family_man_girl:`               | [TOC](#table-of-contents) |
| [TOC](#people--body) |     :family_man_girl_boy:      | `:family_man_girl_boy:`          |     :family_man_girl_girl:      | `:family_man_girl_girl:`          | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :family_woman_boy:       | `:family_woman_boy:`             |     :family_woman_boy_boy:      | `:family_woman_boy_boy:`          | [TOC](#table-of-contents) |
| [TOC](#people--body) |      :family_woman_girl:       | `:family_woman_girl:`            |     :family_woman_girl_boy:     | `:family_woman_girl_boy:`         | [TOC](#table-of-contents) |
| [TOC](#people--body) |    :family_woman_girl_girl:    | `:family_woman_girl_girl:`       |                                 |                                   | [TOC](#table-of-contents) |

#### Person Symbol

|                      |          ico          | shortcode               |         ico          | shortcode              |                           |
| -------------------- | :-------------------: | ----------------------- | :------------------: | ---------------------- | ------------------------- |
| [TOC](#people--body) |    :speaking_head:    | `:speaking_head:`       | :bust_in_silhouette: | `:bust_in_silhouette:` | [TOC](#table-of-contents) |
| [TOC](#people--body) | :busts_in_silhouette: | `:busts_in_silhouette:` |   :people_hugging:   | `:people_hugging:`     | [TOC](#table-of-contents) |
| [TOC](#people--body) |       :family:        | `:family:`              |     :footprints:     | `:footprints:`         | [TOC](#table-of-contents) |

### Animals & Nature

- [Animal Mammal](#animal-mammal)
- [Animal Bird](#animal-bird)
- [Animal Amphibian](#animal-amphibian)
- [Animal Reptile](#animal-reptile)
- [Animal Marine](#animal-marine)
- [Animal Bug](#animal-bug)
- [Plant Flower](#plant-flower)
- [Plant Other](#plant-other)

#### Animal Mammal

|                         |        ico        | shortcode           |       ico       | shortcode                      |                           |
| ----------------------- | :---------------: | ------------------- | :-------------: | ------------------------------ | ------------------------- |
| [TOC](#animals--nature) |   :monkey_face:   | `:monkey_face:`     |    :monkey:     | `:monkey:`                     | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |     :gorilla:     | `:gorilla:`         |   :orangutan:   | `:orangutan:`                  | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |       :dog:       | `:dog:`             |     :dog2:      | `:dog2:`                       | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :guide_dog:    | `:guide_dog:`       |  :service_dog:  | `:service_dog:`                | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |     :poodle:      | `:poodle:`          |     :wolf:      | `:wolf:`                       | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :fox_face:     | `:fox_face:`        |    :raccoon:    | `:raccoon:`                    | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |       :cat:       | `:cat:`             |     :cat2:      | `:cat2:`                       | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :black_cat:    | `:black_cat:`       |     :lion:      | `:lion:`                       | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :tiger:      | `:tiger:`           |    :tiger2:     | `:tiger2:`                     | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |     :leopard:     | `:leopard:`         |     :horse:     | `:horse:`                      | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :racehorse:    | `:racehorse:`       |    :unicorn:    | `:unicorn:`                    | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :zebra:      | `:zebra:`           |     :deer:      | `:deer:`                       | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :bison:      | `:bison:`           |      :cow:      | `:cow:`                        | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |       :ox:        | `:ox:`              | :water_buffalo: | `:water_buffalo:`              | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :cow2:       | `:cow2:`            |      :pig:      | `:pig:`                        | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :pig2:       | `:pig2:`            |     :boar:      | `:boar:`                       | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :pig_nose:     | `:pig_nose:`        |      :ram:      | `:ram:`                        | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :sheep:      | `:sheep:`           |     :goat:      | `:goat:`                       | [TOC](#table-of-contents) |
| [TOC](#animals--nature) | :dromedary_camel: | `:dromedary_camel:` |     :camel:     | `:camel:`                      | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :llama:      | `:llama:`           |    :giraffe:    | `:giraffe:`                    | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :elephant:     | `:elephant:`        |    :mammoth:    | `:mammoth:`                    | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |   :rhinoceros:    | `:rhinoceros:`      | :hippopotamus:  | `:hippopotamus:`               | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :mouse:      | `:mouse:`           |    :mouse2:     | `:mouse2:`                     | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |       :rat:       | `:rat:`             |    :hamster:    | `:hamster:`                    | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |     :rabbit:      | `:rabbit:`          |    :rabbit2:    | `:rabbit2:`                    | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :chipmunk:     | `:chipmunk:`        |    :beaver:     | `:beaver:`                     | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :hedgehog:     | `:hedgehog:`        |      :bat:      | `:bat:`                        | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :bear:       | `:bear:`            |  :polar_bear:   | `:polar_bear:`                 | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :koala:      | `:koala:`           |  :panda_face:   | `:panda_face:`                 | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :sloth:      | `:sloth:`           |     :otter:     | `:otter:`                      | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |      :skunk:      | `:skunk:`           |   :kangaroo:    | `:kangaroo:`                   | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |     :badger:      | `:badger:`          |     :feet:      | `:feet:` <br /> `:paw_prints:` | [TOC](#table-of-contents) |

#### Animal Bird

|                         |     ico      | shortcode      |       ico        | shortcode          |                           |
| ----------------------- | :----------: | -------------- | :--------------: | ------------------ | ------------------------- |
| [TOC](#animals--nature) |   :turkey:   | `:turkey:`     |    :chicken:     | `:chicken:`        | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |  :rooster:   | `:rooster:`    | :hatching_chick: | `:hatching_chick:` | [TOC](#table-of-contents) |
| [TOC](#animals--nature) | :baby_chick: | `:baby_chick:` | :hatched_chick:  | `:hatched_chick:`  | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :bird:    | `:bird:`       |    :penguin:     | `:penguin:`        | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :dove:    | `:dove:`       |     :eagle:      | `:eagle:`          | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :duck:    | `:duck:`       |      :swan:      | `:swan:`           | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :owl:     | `:owl:`        |      :dodo:      | `:dodo:`           | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |  :feather:   | `:feather:`    |    :flamingo:    | `:flamingo:`       | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |  :peacock:   | `:peacock:`    |     :parrot:     | `:parrot:`         | [TOC](#table-of-contents) |

#### Animal Amphibian

|                         |  ico   | shortcode |                           |
| ----------------------- | :----: | --------- | ------------------------- |
| [TOC](#animals--nature) | :frog: | `:frog:`  | [TOC](#table-of-contents) |

#### Animal Reptile

|                         |      ico      | shortcode       |   ico    | shortcode  |                           |
| ----------------------- | :-----------: | --------------- | :------: | ---------- | ------------------------- |
| [TOC](#animals--nature) |  :crocodile:  | `:crocodile:`   | :turtle: | `:turtle:` | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |   :lizard:    | `:lizard:`      | :snake:  | `:snake:`  | [TOC](#table-of-contents) |
| [TOC](#animals--nature) | :dragon_face: | `:dragon_face:` | :dragon: | `:dragon:` | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |  :sauropod:   | `:sauropod:`    | :t-rex:  | `:t-rex:`  | [TOC](#table-of-contents) |

#### Animal Marine

|                         |    ico     | shortcode                      |       ico       | shortcode         |                           |
| ----------------------- | :--------: | ------------------------------ | :-------------: | ----------------- | ------------------------- |
| [TOC](#animals--nature) |  :whale:   | `:whale:`                      |    :whale2:     | `:whale2:`        | [TOC](#table-of-contents) |
| [TOC](#animals--nature) | :dolphin:  | `:dolphin:` <br /> `:flipper:` |     :seal:      | `:seal:`          | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |   :fish:   | `:fish:`                       | :tropical_fish: | `:tropical_fish:` | [TOC](#table-of-contents) |
| [TOC](#animals--nature) | :blowfish: | `:blowfish:`                   |     :shark:     | `:shark:`         | [TOC](#table-of-contents) |
| [TOC](#animals--nature) | :ocTOCus:  | `:ocTOCus:`                    |     :shell:     | `:shell:`         | [TOC](#table-of-contents) |

#### Animal Bug

|                         |      ico      | shortcode                   |     ico     | shortcode     |                           |
| ----------------------- | :-----------: | --------------------------- | :---------: | ------------- | ------------------------- |
| [TOC](#animals--nature) |    :snail:    | `:snail:`                   | :butterfly: | `:butterfly:` | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |     :bug:     | `:bug:`                     |    :ant:    | `:ant:`       | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |     :bee:     | `:bee:` <br /> `:honeybee:` |  :beetle:   | `:beetle:`    | [TOC](#table-of-contents) |
| [TOC](#animals--nature) | :lady_beetle: | `:lady_beetle:`             |  :cricket:  | `:cricket:`   | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |  :cockroach:  | `:cockroach:`               |  :spider:   | `:spider:`    | [TOC](#table-of-contents) |
| [TOC](#animals--nature) | :spider_web:  | `:spider_web:`              | :scorpion:  | `:scorpion:`  | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |  :mosquito:   | `:mosquito:`                |    :fly:    | `:fly:`       | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :worm:     | `:worm:`                    |  :microbe:  | `:microbe:`   | [TOC](#table-of-contents) |

#### Plant Flower

|                         |      ico       | shortcode        |       ico        | shortcode          |                           |
| ----------------------- | :------------: | ---------------- | :--------------: | ------------------ | ------------------------- |
| [TOC](#animals--nature) |   :bouquet:    | `:bouquet:`      | :cherry_blossom: | `:cherry_blossom:` | [TOC](#table-of-contents) |
| [TOC](#animals--nature) | :white_flower: | `:white_flower:` |    :rosette:     | `:rosette:`        | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |     :rose:     | `:rose:`         | :wilted_flower:  | `:wilted_flower:`  | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |   :hibiscus:   | `:hibiscus:`     |   :sunflower:    | `:sunflower:`      | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |   :blossom:    | `:blossom:`      |     :tulip:      | `:tulip:`          | [TOC](#table-of-contents) |

#### Plant Other

|                         |       ico        | shortcode          |        ico         | shortcode            |                           |
| ----------------------- | :--------------: | ------------------ | :----------------: | -------------------- | ------------------------- |
| [TOC](#animals--nature) |    :seedling:    | `:seedling:`       |   :potted_plant:   | `:potted_plant:`     | [TOC](#table-of-contents) |
| [TOC](#animals--nature) | :evergreen_tree: | `:evergreen_tree:` |  :deciduous_tree:  | `:deciduous_tree:`   | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |   :palm_tree:    | `:palm_tree:`      |      :cactus:      | `:cactus:`           | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |  :ear_of_rice:   | `:ear_of_rice:`    |       :herb:       | `:herb:`             | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |    :shamrock:    | `:shamrock:`       | :four_leaf_clover: | `:four_leaf_clover:` | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |   :maple_leaf:   | `:maple_leaf:`     |   :fallen_leaf:    | `:fallen_leaf:`      | [TOC](#table-of-contents) |
| [TOC](#animals--nature) |     :leaves:     | `:leaves:`         |     :mushroom:     | `:mushroom:`         | [TOC](#table-of-contents) |

### Food & Drink

- [Food Fruit](#food-fruit)
- [Food Vegetable](#food-vegetable)
- [Food Prepared](#food-prepared)
- [Food Asian](#food-asian)
- [Food Marine](#food-marine)
- [Food Sweet](#food-sweet)
- [Drink](#drink)
- [Dishware](#dishware)

#### Food Fruit

|                     |      ico      | shortcode       |      ico      | shortcode                                           |                           |
| ------------------- | :-----------: | --------------- | :-----------: | --------------------------------------------------- | ------------------------- |
| [TOC](#food--drink) |   :grapes:    | `:grapes:`      |    :melon:    | `:melon:`                                           | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :watermelon:  | `:watermelon:`  |  :mandarin:   | `:mandarin:` <br /> `:orange:` <br /> `:tangerine:` | [TOC](#table-of-contents) |
| [TOC](#food--drink) |    :lemon:    | `:lemon:`       |   :banana:    | `:banana:`                                          | [TOC](#table-of-contents) |
| [TOC](#food--drink) |  :pineapple:  | `:pineapple:`   |    :mango:    | `:mango:`                                           | [TOC](#table-of-contents) |
| [TOC](#food--drink) |    :apple:    | `:apple:`       | :green_apple: | `:green_apple:`                                     | [TOC](#table-of-contents) |
| [TOC](#food--drink) |    :pear:     | `:pear:`        |    :peach:    | `:peach:`                                           | [TOC](#table-of-contents) |
| [TOC](#food--drink) |  :cherries:   | `:cherries:`    | :strawberry:  | `:strawberry:`                                      | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :blueberries: | `:blueberries:` | :kiwi_fruit:  | `:kiwi_fruit:`                                      | [TOC](#table-of-contents) |
| [TOC](#food--drink) |   :tomato:    | `:tomato:`      |    :olive:    | `:olive:`                                           | [TOC](#table-of-contents) |
| [TOC](#food--drink) |   :coconut:   | `:coconut:`     |               |                                                     | [TOC](#table-of-contents) |

#### Food Vegetable

|                     |      ico      | shortcode       |     ico      | shortcode      |                           |
| ------------------- | :-----------: | --------------- | :----------: | -------------- | ------------------------- |
| [TOC](#food--drink) |   :avocado:   | `:avocado:`     |  :eggplant:  | `:eggplant:`   | [TOC](#table-of-contents) |
| [TOC](#food--drink) |   :potato:    | `:potato:`      |   :carrot:   | `:carrot:`     | [TOC](#table-of-contents) |
| [TOC](#food--drink) |    :corn:     | `:corn:`        | :hot_pepper: | `:hot_pepper:` | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :bell_pepper: | `:bell_pepper:` |  :cucumber:  | `:cucumber:`   | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :leafy_green: | `:leafy_green:` |  :broccoli:  | `:broccoli:`   | [TOC](#table-of-contents) |
| [TOC](#food--drink) |   :garlic:    | `:garlic:`      |   :onion:    | `:onion:`      | [TOC](#table-of-contents) |
| [TOC](#food--drink) |   :peanuts:   | `:peanuts:`     |  :chestnut:  | `:chestnut:`   | [TOC](#table-of-contents) |

#### Food Prepared

|                     |        ico        | shortcode           |          ico          | shortcode               |                           |
| ------------------- | :---------------: | ------------------- | :-------------------: | ----------------------- | ------------------------- |
| [TOC](#food--drink) |      :bread:      | `:bread:`           |      :croissant:      | `:croissant:`           | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :baguette_bread:  | `:baguette_bread:`  |      :flatbread:      | `:flatbread:`           | [TOC](#table-of-contents) |
| [TOC](#food--drink) |     :pretzel:     | `:pretzel:`         |        :bagel:        | `:bagel:`               | [TOC](#table-of-contents) |
| [TOC](#food--drink) |    :pancakes:     | `:pancakes:`        |       :waffle:        | `:waffle:`              | [TOC](#table-of-contents) |
| [TOC](#food--drink) |     :cheese:      | `:cheese:`          |    :meat_on_bone:     | `:meat_on_bone:`        | [TOC](#table-of-contents) |
| [TOC](#food--drink) |   :poultry_leg:   | `:poultry_leg:`     |     :cut_of_meat:     | `:cut_of_meat:`         | [TOC](#table-of-contents) |
| [TOC](#food--drink) |      :bacon:      | `:bacon:`           |      :hamburger:      | `:hamburger:`           | [TOC](#table-of-contents) |
| [TOC](#food--drink) |      :fries:      | `:fries:`           |        :pizza:        | `:pizza:`               | [TOC](#table-of-contents) |
| [TOC](#food--drink) |     :hotdog:      | `:hotdog:`          |      :sandwich:       | `:sandwich:`            | [TOC](#table-of-contents) |
| [TOC](#food--drink) |      :taco:       | `:taco:`            |       :burrito:       | `:burrito:`             | [TOC](#table-of-contents) |
| [TOC](#food--drink) |     :tamale:      | `:tamale:`          |  :stuffed_flatbread:  | `:stuffed_flatbread:`   | [TOC](#table-of-contents) |
| [TOC](#food--drink) |     :falafel:     | `:falafel:`         |         :egg:         | `:egg:`                 | [TOC](#table-of-contents) |
| [TOC](#food--drink) |    :fried_egg:    | `:fried_egg:`       | :shallow_pan_of_food: | `:shallow_pan_of_food:` | [TOC](#table-of-contents) |
| [TOC](#food--drink) |      :stew:       | `:stew:`            |       :fondue:        | `:fondue:`              | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :bowl_with_spoon: | `:bowl_with_spoon:` |     :green_salad:     | `:green_salad:`         | [TOC](#table-of-contents) |
| [TOC](#food--drink) |     :popcorn:     | `:popcorn:`         |       :butter:        | `:butter:`              | [TOC](#table-of-contents) |
| [TOC](#food--drink) |      :salt:       | `:salt:`            |     :canned_food:     | `:canned_food:`         | [TOC](#table-of-contents) |

#### Food Asian

|                     |      ico       | shortcode        |       ico        | shortcode          |                           |
| ------------------- | :------------: | ---------------- | :--------------: | ------------------ | ------------------------- |
| [TOC](#food--drink) |    :bento:     | `:bento:`        |  :rice_cracker:  | `:rice_cracker:`   | [TOC](#table-of-contents) |
| [TOC](#food--drink) |  :rice_ball:   | `:rice_ball:`    |      :rice:      | `:rice:`           | [TOC](#table-of-contents) |
| [TOC](#food--drink) |    :curry:     | `:curry:`        |     :ramen:      | `:ramen:`          | [TOC](#table-of-contents) |
| [TOC](#food--drink) |  :spaghetti:   | `:spaghetti:`    |  :sweet_potato:  | `:sweet_potato:`   | [TOC](#table-of-contents) |
| [TOC](#food--drink) |     :oden:     | `:oden:`         |     :sushi:      | `:sushi:`          | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :fried_shrimp: | `:fried_shrimp:` |   :fish_cake:    | `:fish_cake:`      | [TOC](#table-of-contents) |
| [TOC](#food--drink) |  :moon_cake:   | `:moon_cake:`    |     :dango:      | `:dango:`          | [TOC](#table-of-contents) |
| [TOC](#food--drink) |   :dumpling:   | `:dumpling:`     | :fortune_cookie: | `:fortune_cookie:` | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :takeout_box:  | `:takeout_box:`  |                  |                    | [TOC](#table-of-contents) |

#### Food Marine

|                     |   ico    | shortcode  |    ico    | shortcode   |                           |
| ------------------- | :------: | ---------- | :-------: | ----------- | ------------------------- |
| [TOC](#food--drink) |  :crab:  | `:crab:`   | :lobster: | `:lobster:` | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :shrimp: | `:shrimp:` |  :squid:  | `:squid:`   | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :oyster: | `:oyster:` |           |             | [TOC](#table-of-contents) |

#### Food Sweet

|                     |     ico     | shortcode     |       ico       | shortcode         |                           |
| ------------------- | :---------: | ------------- | :-------------: | ----------------- | ------------------------- |
| [TOC](#food--drink) | :icecream:  | `:icecream:`  |  :shaved_ice:   | `:shaved_ice:`    | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :ice_cream: | `:ice_cream:` |   :doughnut:    | `:doughnut:`      | [TOC](#table-of-contents) |
| [TOC](#food--drink) |  :cookie:   | `:cookie:`    |   :birthday:    | `:birthday:`      | [TOC](#table-of-contents) |
| [TOC](#food--drink) |   :cake:    | `:cake:`      |    :cupcake:    | `:cupcake:`       | [TOC](#table-of-contents) |
| [TOC](#food--drink) |    :pie:    | `:pie:`       | :chocolate_bar: | `:chocolate_bar:` | [TOC](#table-of-contents) |
| [TOC](#food--drink) |   :candy:   | `:candy:`     |   :lollipop:    | `:lollipop:`      | [TOC](#table-of-contents) |
| [TOC](#food--drink) |  :custard:  | `:custard:`   |   :honey_pot:   | `:honey_pot:`     | [TOC](#table-of-contents) |

#### Drink

|                     |        ico         | shortcode            |       ico        | shortcode          |                           |
| ------------------- | :----------------: | -------------------- | :--------------: | ------------------ | ------------------------- |
| [TOC](#food--drink) |   :baby_bottle:    | `:baby_bottle:`      |   :milk_glass:   | `:milk_glass:`     | [TOC](#table-of-contents) |
| [TOC](#food--drink) |      :coffee:      | `:coffee:`           |     :teapot:     | `:teapot:`         | [TOC](#table-of-contents) |
| [TOC](#food--drink) |       :tea:        | `:tea:`              |      :sake:      | `:sake:`           | [TOC](#table-of-contents) |
| [TOC](#food--drink) |    :champagne:     | `:champagne:`        |   :wine_glass:   | `:wine_glass:`     | [TOC](#table-of-contents) |
| [TOC](#food--drink) |     :cocktail:     | `:cocktail:`         | :tropical_drink: | `:tropical_drink:` | [TOC](#table-of-contents) |
| [TOC](#food--drink) |       :beer:       | `:beer:`             |     :beers:      | `:beers:`          | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :clinking_glasses: | `:clinking_glasses:` | :tumbler_glass:  | `:tumbler_glass:`  | [TOC](#table-of-contents) |
| [TOC](#food--drink) |  :cup_with_straw:  | `:cup_with_straw:`   |   :bubble_tea:   | `:bubble_tea:`     | [TOC](#table-of-contents) |
| [TOC](#food--drink) |   :beverage_box:   | `:beverage_box:`     |      :mate:      | `:mate:`           | [TOC](#table-of-contents) |
| [TOC](#food--drink) |     :ice_cube:     | `:ice_cube:`         |                  |                    | [TOC](#table-of-contents) |

#### Dishware

|                     |       ico        | shortcode                  |         ico          | shortcode              |                           |
| ------------------- | :--------------: | -------------------------- | :------------------: | ---------------------- | ------------------------- |
| [TOC](#food--drink) |   :chopsticks:   | `:chopsticks:`             | :plate_with_cutlery: | `:plate_with_cutlery:` | [TOC](#table-of-contents) |
| [TOC](#food--drink) | :fork_and_knife: | `:fork_and_knife:`         |       :spoon:        | `:spoon:`              | [TOC](#table-of-contents) |
| [TOC](#food--drink) |     :hocho:      | `:hocho:` <br /> `:knife:` |      :amphora:       | `:amphora:`            | [TOC](#table-of-contents) |

### Travel & Places

- [Place Map](#place-map)
- [Place Geographic](#place-geographic)
- [Place Building](#place-building)
- [Place Religious](#place-religious)
- [Place Other](#place-other)
- [Transport Ground](#transport-ground)
- [Transport Water](#transport-water)
- [Transport Air](#transport-air)
- [Hotel](#hotel)
- [Time](#time)
- [Sky & Weather](#sky--weather)

#### Place Map

|                        |      ico       | shortcode        |          ico           | shortcode                |                           |
| ---------------------- | :------------: | ---------------- | :--------------------: | ------------------------ | ------------------------- |
| [TOC](#travel--places) | :earth_africa: | `:earth_africa:` |    :earth_americas:    | `:earth_americas:`       | [TOC](#table-of-contents) |
| [TOC](#travel--places) |  :earth_asia:  | `:earth_asia:`   | :globe_with_meridians: | `:globe_with_meridians:` | [TOC](#table-of-contents) |
| [TOC](#travel--places) |  :world_map:   | `:world_map:`    |        :japan:         | `:japan:`                | [TOC](#table-of-contents) |
| [TOC](#travel--places) |   :compass:    | `:compass:`      |                        |                          | [TOC](#table-of-contents) |

#### Place Geographic

|                        |       ico       | shortcode         |       ico        | shortcode          |                           |
| ---------------------- | :-------------: | ----------------- | :--------------: | ------------------ | ------------------------- |
| [TOC](#travel--places) | :mountain_snow: | `:mountain_snow:` |    :mountain:    | `:mountain:`       | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :volcano:    | `:volcano:`       |   :mount_fuji:   | `:mount_fuji:`     | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :camping:    | `:camping:`       | :beach_umbrella: | `:beach_umbrella:` | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :desert:     | `:desert:`        | :desert_island:  | `:desert_island:`  | [TOC](#table-of-contents) |
| [TOC](#travel--places) | :national_park: | `:national_park:` |                  |                    | [TOC](#table-of-contents) |

#### Place Building

|                        |           ico           | shortcode                 |          ico           | shortcode                |                           |
| ---------------------- | :---------------------: | ------------------------- | :--------------------: | ------------------------ | ------------------------- |
| [TOC](#travel--places) |        :stadium:        | `:stadium:`               |  :classical_building:  | `:classical_building:`   | [TOC](#table-of-contents) |
| [TOC](#travel--places) | :building_construction: | `:building_construction:` |        :bricks:        | `:bricks:`               | [TOC](#table-of-contents) |
| [TOC](#travel--places) |         :rock:          | `:rock:`                  |         :wood:         | `:wood:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |          :hut:          | `:hut:`                   |        :houses:        | `:houses:`               | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :derelict_house:     | `:derelict_house:`        |        :house:         | `:house:`                | [TOC](#table-of-contents) |
| [TOC](#travel--places) |   :house_with_garden:   | `:house_with_garden:`     |        :office:        | `:office:`               | [TOC](#table-of-contents) |
| [TOC](#travel--places) |      :post_office:      | `:post_office:`           | :european_post_office: | `:european_post_office:` | [TOC](#table-of-contents) |
| [TOC](#travel--places) |       :hospital:        | `:hospital:`              |         :bank:         | `:bank:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |         :hotel:         | `:hotel:`                 |      :love_hotel:      | `:love_hotel:`           | [TOC](#table-of-contents) |
| [TOC](#travel--places) |   :convenience_store:   | `:convenience_store:`     |        :school:        | `:school:`               | [TOC](#table-of-contents) |
| [TOC](#travel--places) |   :department_store:    | `:department_store:`      |       :factory:        | `:factory:`              | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :japanese_castle:    | `:japanese_castle:`       |   :european_castle:    | `:european_castle:`      | [TOC](#table-of-contents) |
| [TOC](#travel--places) |        :wedding:        | `:wedding:`               |     :tokyo_tower:      | `:tokyo_tower:`          | [TOC](#table-of-contents) |
| [TOC](#travel--places) |   :statue_of_liberty:   | `:statue_of_liberty:`     |                        |                          | [TOC](#table-of-contents) |

#### Place Religious

|                        |       ico       | shortcode         |     ico     | shortcode     |                           |
| ---------------------- | :-------------: | ----------------- | :---------: | ------------- | ------------------------- |
| [TOC](#travel--places) |    :church:     | `:church:`        |  :mosque:   | `:mosque:`    | [TOC](#table-of-contents) |
| [TOC](#travel--places) | :hindu_temple:  | `:hindu_temple:`  | :synagogue: | `:synagogue:` | [TOC](#table-of-contents) |
| [TOC](#travel--places) | :shinto_shrine: | `:shinto_shrine:` |   :kaaba:   | `:kaaba:`     | [TOC](#table-of-contents) |

#### Place Other

|                        |      ico       | shortcode        |           ico            | shortcode                  |                           |
| ---------------------- | :------------: | ---------------- | :----------------------: | -------------------------- | ------------------------- |
| [TOC](#travel--places) |   :fountain:   | `:fountain:`     |          :tent:          | `:tent:`                   | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :foggy:     | `:foggy:`        |    :night_with_stars:    | `:night_with_stars:`       | [TOC](#table-of-contents) |
| [TOC](#travel--places) |  :cityscape:   | `:cityscape:`    | :sunrise_over_mountains: | `:sunrise_over_mountains:` | [TOC](#table-of-contents) |
| [TOC](#travel--places) |   :sunrise:    | `:sunrise:`      |      :city_sunset:       | `:city_sunset:`            | [TOC](#table-of-contents) |
| [TOC](#travel--places) | :city_sunrise: | `:city_sunrise:` |    :bridge_at_night:     | `:bridge_at_night:`        | [TOC](#table-of-contents) |
| [TOC](#travel--places) |  :hotsprings:  | `:hotsprings:`   |     :carousel_horse:     | `:carousel_horse:`         | [TOC](#table-of-contents) |
| [TOC](#travel--places) | :ferris_wheel: | `:ferris_wheel:` |     :roller_coaster:     | `:roller_coaster:`         | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :barber:    | `:barber:`       |      :circus_tent:       | `:circus_tent:`            | [TOC](#table-of-contents) |

#### Transport Ground

|                        |           ico            | shortcode                  |          ico           | shortcode                |                           |
| ---------------------- | :----------------------: | -------------------------- | :--------------------: | ------------------------ | ------------------------- |
| [TOC](#travel--places) |    :steam_locomotive:    | `:steam_locomotive:`       |     :railway_car:      | `:railway_car:`          | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :bullettrain_side:    | `:bullettrain_side:`       |  :bullettrain_front:   | `:bullettrain_front:`    | [TOC](#table-of-contents) |
| [TOC](#travel--places) |         :train2:         | `:train2:`                 |        :metro:         | `:metro:`                | [TOC](#table-of-contents) |
| [TOC](#travel--places) |       :light_rail:       | `:light_rail:`             |       :station:        | `:station:`              | [TOC](#table-of-contents) |
| [TOC](#travel--places) |          :tram:          | `:tram:`                   |       :monorail:       | `:monorail:`             | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :mountain_railway:    | `:mountain_railway:`       |        :train:         | `:train:`                | [TOC](#table-of-contents) |
| [TOC](#travel--places) |          :bus:           | `:bus:`                    |     :oncoming_bus:     | `:oncoming_bus:`         | [TOC](#table-of-contents) |
| [TOC](#travel--places) |       :trolleybus:       | `:trolleybus:`             |       :minibus:        | `:minibus:`              | [TOC](#table-of-contents) |
| [TOC](#travel--places) |       :ambulance:        | `:ambulance:`              |     :fire_engine:      | `:fire_engine:`          | [TOC](#table-of-contents) |
| [TOC](#travel--places) |       :police_car:       | `:police_car:`             | :oncoming_police_car:  | `:oncoming_police_car:`  | [TOC](#table-of-contents) |
| [TOC](#travel--places) |          :taxi:          | `:taxi:`                   |    :oncoming_taxi:     | `:oncoming_taxi:`        | [TOC](#table-of-contents) |
| [TOC](#travel--places) |          :car:           | `:car:` <br /> `:red_car:` | :oncoming_automobile:  | `:oncoming_automobile:`  | [TOC](#table-of-contents) |
| [TOC](#travel--places) |        :blue_car:        | `:blue_car:`               |     :pickup_truck:     | `:pickup_truck:`         | [TOC](#table-of-contents) |
| [TOC](#travel--places) |         :truck:          | `:truck:`                  |  :articulated_lorry:   | `:articulated_lorry:`    | [TOC](#table-of-contents) |
| [TOC](#travel--places) |        :tractor:         | `:tractor:`                |      :racing_car:      | `:racing_car:`           | [TOC](#table-of-contents) |
| [TOC](#travel--places) |       :motorcycle:       | `:motorcycle:`             |    :motor_scooter:     | `:motor_scooter:`        | [TOC](#table-of-contents) |
| [TOC](#travel--places) |   :manual_wheelchair:    | `:manual_wheelchair:`      | :motorized_wheelchair: | `:motorized_wheelchair:` | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :auto_rickshaw:      | `:auto_rickshaw:`          |         :bike:         | `:bike:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |      :kick_scooter:      | `:kick_scooter:`           |      :skateboard:      | `:skateboard:`           | [TOC](#table-of-contents) |
| [TOC](#travel--places) |      :roller_skate:      | `:roller_skate:`           |       :bussTOC:        | `:bussTOC:`              | [TOC](#table-of-contents) |
| [TOC](#travel--places) |        :motorway:        | `:motorway:`               |    :railway_track:     | `:railway_track:`        | [TOC](#table-of-contents) |
| [TOC](#travel--places) |        :oil_drum:        | `:oil_drum:`               |       :fuelpump:       | `:fuelpump:`             | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :rotating_light:     | `:rotating_light:`         |    :traffic_light:     | `:traffic_light:`        | [TOC](#table-of-contents) |
| [TOC](#travel--places) | :vertical_traffic_light: | `:vertical_traffic_light:` |      :sTOC_sign:       | `:sTOC_sign:`            | [TOC](#table-of-contents) |
| [TOC](#travel--places) |      :construction:      | `:construction:`           |                        |                          | [TOC](#table-of-contents) |

#### Transport Water

|                        |       ico        | shortcode          |     ico     | shortcode                    |                           |
| ---------------------- | :--------------: | ------------------ | :---------: | ---------------------------- | ------------------------- |
| [TOC](#travel--places) |     :anchor:     | `:anchor:`         |   :boat:    | `:boat:` <br /> `:sailboat:` | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :canoe:      | `:canoe:`          | :speedboat: | `:speedboat:`                | [TOC](#table-of-contents) |
| [TOC](#travel--places) | :passenger_ship: | `:passenger_ship:` |   :ferry:   | `:ferry:`                    | [TOC](#table-of-contents) |
| [TOC](#travel--places) |   :motor_boat:   | `:motor_boat:`     |   :ship:    | `:ship:`                     | [TOC](#table-of-contents) |

#### Transport Air

|                        |          ico           | shortcode                |         ico          | shortcode              |                           |
| ---------------------- | :--------------------: | ------------------------ | :------------------: | ---------------------- | ------------------------- |
| [TOC](#travel--places) |       :airplane:       | `:airplane:`             |   :small_airplane:   | `:small_airplane:`     | [TOC](#table-of-contents) |
| [TOC](#travel--places) |   :flight_departure:   | `:flight_departure:`     |   :flight_arrival:   | `:flight_arrival:`     | [TOC](#table-of-contents) |
| [TOC](#travel--places) |      :parachute:       | `:parachute:`            |        :seat:        | `:seat:`               | [TOC](#table-of-contents) |
| [TOC](#travel--places) |      :helicopter:      | `:helicopter:`           | :suspension_railway: | `:suspension_railway:` | [TOC](#table-of-contents) |
| [TOC](#travel--places) |  :mountain_cableway:   | `:mountain_cableway:`    |   :aerial_tramway:   | `:aerial_tramway:`     | [TOC](#table-of-contents) |
| [TOC](#travel--places) | :artificial_satellite: | `:artificial_satellite:` |       :rocket:       | `:rocket:`             | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :flying_saucer:     | `:flying_saucer:`        |                      |                        | [TOC](#table-of-contents) |

#### Hotel

|                        |      ico       | shortcode        |    ico    | shortcode   |                           |
| ---------------------- | :------------: | ---------------- | :-------: | ----------- | ------------------------- |
| [TOC](#travel--places) | :bellhop_bell: | `:bellhop_bell:` | :luggage: | `:luggage:` | [TOC](#table-of-contents) |

#### Time

|                        |         ico         | shortcode             |           ico            | shortcode                  |                           |
| ---------------------- | :-----------------: | --------------------- | :----------------------: | -------------------------- | ------------------------- |
| [TOC](#travel--places) |     :hourglass:     | `:hourglass:`         | :hourglass_flowing_sand: | `:hourglass_flowing_sand:` | [TOC](#table-of-contents) |
| [TOC](#travel--places) |       :watch:       | `:watch:`             |      :alarm_clock:       | `:alarm_clock:`            | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :sTOCwatch:     | `:sTOCwatch:`         |      :timer_clock:       | `:timer_clock:`            | [TOC](#table-of-contents) |
| [TOC](#travel--places) | :mantelpiece_clock: | `:mantelpiece_clock:` |        :clock12:         | `:clock12:`                | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock1230:     | `:clock1230:`         |         :clock1:         | `:clock1:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock130:      | `:clock130:`          |         :clock2:         | `:clock2:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock230:      | `:clock230:`          |         :clock3:         | `:clock3:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock330:      | `:clock330:`          |         :clock4:         | `:clock4:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock430:      | `:clock430:`          |         :clock5:         | `:clock5:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock530:      | `:clock530:`          |         :clock6:         | `:clock6:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock630:      | `:clock630:`          |         :clock7:         | `:clock7:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock730:      | `:clock730:`          |         :clock8:         | `:clock8:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock830:      | `:clock830:`          |         :clock9:         | `:clock9:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock930:      | `:clock930:`          |        :clock10:         | `:clock10:`                | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock1030:     | `:clock1030:`         |        :clock11:         | `:clock11:`                | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :clock1130:     | `:clock1130:`         |                          |                            | [TOC](#table-of-contents) |

#### Sky & Weather

|                        |              ico               | shortcode                        |               ico               | shortcode                               |                           |
| ---------------------- | :----------------------------: | -------------------------------- | :-----------------------------: | --------------------------------------- | ------------------------- |
| [TOC](#travel--places) |           :new_moon:           | `:new_moon:`                     |     :waxing_crescent_moon:      | `:waxing_crescent_moon:`                | [TOC](#table-of-contents) |
| [TOC](#travel--places) |      :first_quarter_moon:      | `:first_quarter_moon:`           |             :moon:              | `:moon:` <br /> `:waxing_gibbous_moon:` | [TOC](#table-of-contents) |
| [TOC](#travel--places) |          :full_moon:           | `:full_moon:`                    |      :waning_gibbous_moon:      | `:waning_gibbous_moon:`                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |      :last_quarter_moon:       | `:last_quarter_moon:`            |     :waning_crescent_moon:      | `:waning_crescent_moon:`                | [TOC](#table-of-contents) |
| [TOC](#travel--places) |        :crescent_moon:         | `:crescent_moon:`                |      :new_moon_with_face:       | `:new_moon_with_face:`                  | [TOC](#table-of-contents) |
| [TOC](#travel--places) | :first_quarter_moon_with_face: | `:first_quarter_moon_with_face:` |  :last_quarter_moon_with_face:  | `:last_quarter_moon_with_face:`         | [TOC](#table-of-contents) |
| [TOC](#travel--places) |         :thermometer:          | `:thermometer:`                  |             :sunny:             | `:sunny:`                               | [TOC](#table-of-contents) |
| [TOC](#travel--places) |     :full_moon_with_face:      | `:full_moon_with_face:`          |         :sun_with_face:         | `:sun_with_face:`                       | [TOC](#table-of-contents) |
| [TOC](#travel--places) |        :ringed_planet:         | `:ringed_planet:`                |             :star:              | `:star:`                                | [TOC](#table-of-contents) |
| [TOC](#travel--places) |            :star2:             | `:star2:`                        |             :stars:             | `:stars:`                               | [TOC](#table-of-contents) |
| [TOC](#travel--places) |          :milky_way:           | `:milky_way:`                    |             :cloud:             | `:cloud:`                               | [TOC](#table-of-contents) |
| [TOC](#travel--places) |         :partly_sunny:         | `:partly_sunny:`                 | :cloud_with_lightning_and_rain: | `:cloud_with_lightning_and_rain:`       | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :sun_behind_small_cloud:    | `:sun_behind_small_cloud:`       |    :sun_behind_large_cloud:     | `:sun_behind_large_cloud:`              | [TOC](#table-of-contents) |
| [TOC](#travel--places) |    :sun_behind_rain_cloud:     | `:sun_behind_rain_cloud:`        |        :cloud_with_rain:        | `:cloud_with_rain:`                     | [TOC](#table-of-contents) |
| [TOC](#travel--places) |       :cloud_with_snow:        | `:cloud_with_snow:`              |     :cloud_with_lightning:      | `:cloud_with_lightning:`                | [TOC](#table-of-contents) |
| [TOC](#travel--places) |           :tornado:            | `:tornado:`                      |              :fog:              | `:fog:`                                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |          :wind_face:           | `:wind_face:`                    |            :cyclone:            | `:cyclone:`                             | [TOC](#table-of-contents) |
| [TOC](#travel--places) |           :rainbow:            | `:rainbow:`                      |        :closed_umbrella:        | `:closed_umbrella:`                     | [TOC](#table-of-contents) |
| [TOC](#travel--places) |        :open_umbrella:         | `:open_umbrella:`                |           :umbrella:            | `:umbrella:`                            | [TOC](#table-of-contents) |
| [TOC](#travel--places) |      :parasol_on_ground:       | `:parasol_on_ground:`            |              :zap:              | `:zap:`                                 | [TOC](#table-of-contents) |
| [TOC](#travel--places) |          :snowflake:           | `:snowflake:`                    |       :snowman_with_snow:       | `:snowman_with_snow:`                   | [TOC](#table-of-contents) |
| [TOC](#travel--places) |           :snowman:            | `:snowman:`                      |             :comet:             | `:comet:`                               | [TOC](#table-of-contents) |
| [TOC](#travel--places) |             :fire:             | `:fire:`                         |            :droplet:            | `:droplet:`                             | [TOC](#table-of-contents) |
| [TOC](#travel--places) |            :ocean:             | `:ocean:`                        |                                 |                                         | [TOC](#table-of-contents) |

### Activities

- [Event](#event)
- [Award Medal](#award-medal)
- [Sport](#sport)
- [Game](#game)
- [Arts & Crafts](#arts--crafts)

#### Event

|                    |        ico        | shortcode           |       ico        | shortcode          |                           |
| ------------------ | :---------------: | ------------------- | :--------------: | ------------------ | ------------------------- |
| [TOC](#activities) | :jack_o_lantern:  | `:jack_o_lantern:`  | :christmas_tree: | `:christmas_tree:` | [TOC](#table-of-contents) |
| [TOC](#activities) |    :fireworks:    | `:fireworks:`       |    :sparkler:    | `:sparkler:`       | [TOC](#table-of-contents) |
| [TOC](#activities) |   :firecracker:   | `:firecracker:`     |    :sparkles:    | `:sparkles:`       | [TOC](#table-of-contents) |
| [TOC](#activities) |     :balloon:     | `:balloon:`         |      :tada:      | `:tada:`           | [TOC](#table-of-contents) |
| [TOC](#activities) |  :confetti_ball:  | `:confetti_ball:`   | :tanabata_tree:  | `:tanabata_tree:`  | [TOC](#table-of-contents) |
| [TOC](#activities) |     :bamboo:      | `:bamboo:`          |     :dolls:      | `:dolls:`          | [TOC](#table-of-contents) |
| [TOC](#activities) |      :flags:      | `:flags:`           |   :wind_chime:   | `:wind_chime:`     | [TOC](#table-of-contents) |
| [TOC](#activities) |   :rice_scene:    | `:rice_scene:`      |  :red_envelope:  | `:red_envelope:`   | [TOC](#table-of-contents) |
| [TOC](#activities) |     :ribbon:      | `:ribbon:`          |      :gift:      | `:gift:`           | [TOC](#table-of-contents) |
| [TOC](#activities) | :reminder_ribbon: | `:reminder_ribbon:` |    :tickets:     | `:tickets:`        | [TOC](#table-of-contents) |
| [TOC](#activities) |     :ticket:      | `:ticket:`          |                  |                    | [TOC](#table-of-contents) |

#### Award Medal

|                    |        ico        | shortcode           |        ico        | shortcode           |                           |
| ------------------ | :---------------: | ------------------- | :---------------: | ------------------- | ------------------------- |
| [TOC](#activities) | :medal_military:  | `:medal_military:`  |     :trophy:      | `:trophy:`          | [TOC](#table-of-contents) |
| [TOC](#activities) |  :medal_sports:   | `:medal_sports:`    | :1st_place_medal: | `:1st_place_medal:` | [TOC](#table-of-contents) |
| [TOC](#activities) | :2nd_place_medal: | `:2nd_place_medal:` | :3rd_place_medal: | `:3rd_place_medal:` | [TOC](#table-of-contents) |

#### Sport

|                    |       ico        | shortcode          |            ico            | shortcode                   |                           |
| ------------------ | :--------------: | ------------------ | :-----------------------: | --------------------------- | ------------------------- |
| [TOC](#activities) |     :soccer:     | `:soccer:`         |        :baseball:         | `:baseball:`                | [TOC](#table-of-contents) |
| [TOC](#activities) |    :softball:    | `:softball:`       |       :basketball:        | `:basketball:`              | [TOC](#table-of-contents) |
| [TOC](#activities) |   :volleyball:   | `:volleyball:`     |        :football:         | `:football:`                | [TOC](#table-of-contents) |
| [TOC](#activities) | :rugby_football: | `:rugby_football:` |         :tennis:          | `:tennis:`                  | [TOC](#table-of-contents) |
| [TOC](#activities) |  :flying_disc:   | `:flying_disc:`    |         :bowling:         | `:bowling:`                 | [TOC](#table-of-contents) |
| [TOC](#activities) |  :cricket_game:  | `:cricket_game:`   |      :field_hockey:       | `:field_hockey:`            | [TOC](#table-of-contents) |
| [TOC](#activities) |   :ice_hockey:   | `:ice_hockey:`     |        :lacrosse:         | `:lacrosse:`                | [TOC](#table-of-contents) |
| [TOC](#activities) |   :ping_pong:    | `:ping_pong:`      |        :badminton:        | `:badminton:`               | [TOC](#table-of-contents) |
| [TOC](#activities) |  :boxing_glove:  | `:boxing_glove:`   |  :martial_arts_uniform:   | `:martial_arts_uniform:`    | [TOC](#table-of-contents) |
| [TOC](#activities) |    :goal_net:    | `:goal_net:`       |          :golf:           | `:golf:`                    | [TOC](#table-of-contents) |
| [TOC](#activities) |   :ice_skate:    | `:ice_skate:`      |  :fishing_pole_and_fish:  | `:fishing_pole_and_fish:`   | [TOC](#table-of-contents) |
| [TOC](#activities) |  :diving_mask:   | `:diving_mask:`    | :running_shirt_with_sash: | `:running_shirt_with_sash:` | [TOC](#table-of-contents) |
| [TOC](#activities) |      :ski:       | `:ski:`            |          :sled:           | `:sled:`                    | [TOC](#table-of-contents) |
| [TOC](#activities) | :curling_stone:  | `:curling_stone:`  |                           |                             | [TOC](#table-of-contents) |

#### Game

|                    |          ico           | shortcode                |      ico       | shortcode        |                           |
| ------------------ | :--------------------: | ------------------------ | :------------: | ---------------- | ------------------------- |
| [TOC](#activities) |         :dart:         | `:dart:`                 |    :yo_yo:     | `:yo_yo:`        | [TOC](#table-of-contents) |
| [TOC](#activities) |         :kite:         | `:kite:`                 |     :gun:      | `:gun:`          | [TOC](#table-of-contents) |
| [TOC](#activities) |        :8ball:         | `:8ball:`                | :crystal_ball: | `:crystal_ball:` | [TOC](#table-of-contents) |
| [TOC](#activities) |      :magic_wand:      | `:magic_wand:`           |  :video_game:  | `:video_game:`   | [TOC](#table-of-contents) |
| [TOC](#activities) |       :joystick:       | `:joystick:`             | :slot_machine: | `:slot_machine:` | [TOC](#table-of-contents) |
| [TOC](#activities) |       :game_die:       | `:game_die:`             |    :jigsaw:    | `:jigsaw:`       | [TOC](#table-of-contents) |
| [TOC](#activities) |      :teddy_bear:      | `:teddy_bear:`           |    :pinata:    | `:pinata:`       | [TOC](#table-of-contents) |
| [TOC](#activities) |    :nesting_dolls:     | `:nesting_dolls:`        |    :spades:    | `:spades:`       | [TOC](#table-of-contents) |
| [TOC](#activities) |        :hearts:        | `:hearts:`               |   :diamonds:   | `:diamonds:`     | [TOC](#table-of-contents) |
| [TOC](#activities) |        :clubs:         | `:clubs:`                |  :chess_pawn:  | `:chess_pawn:`   | [TOC](#table-of-contents) |
| [TOC](#activities) |     :black_joker:      | `:black_joker:`          |   :mahjong:    | `:mahjong:`      | [TOC](#table-of-contents) |
| [TOC](#activities) | :flower_playing_cards: | `:flower_playing_cards:` |                |                  | [TOC](#table-of-contents) |

#### Arts & Crafts

|                    |        ico        | shortcode           |       ico        | shortcode          |                           |
| ------------------ | :---------------: | ------------------- | :--------------: | ------------------ | ------------------------- |
| [TOC](#activities) | :performing_arts: | `:performing_arts:` | :framed_picture: | `:framed_picture:` | [TOC](#table-of-contents) |
| [TOC](#activities) |       :art:       | `:art:`             |     :thread:     | `:thread:`         | [TOC](#table-of-contents) |
| [TOC](#activities) |  :sewing_needle:  | `:sewing_needle:`   |      :yarn:      | `:yarn:`           | [TOC](#table-of-contents) |
| [TOC](#activities) |      :knot:       | `:knot:`            |                  |                    | [TOC](#table-of-contents) |

### Objects

- [Clothing](#clothing)
- [Sound](#sound)
- [Music](#music)
- [Musical Instrument](#musical-instrument)
- [Phone](#phone)
- [Computer](#computer)
- [Light & Video](#light--video)
- [Book Paper](#book-paper)
- [Money](#money)
- [Mail](#mail)
- [Writing](#writing)
- [Office](#office)
- [Lock](#lock)
- [Tool](#tool)
- [Science](#science)
- [Medical](#medical)
- [Household](#household)
- [Other Object](#other-object)

#### Clothing

|                 |          ico           | shortcode                     |         ico          | shortcode              |                           |
| --------------- | :--------------------: | ----------------------------- | :------------------: | ---------------------- | ------------------------- |
| [TOC](#objects) |      :eyeglasses:      | `:eyeglasses:`                |  :dark_sunglasses:   | `:dark_sunglasses:`    | [TOC](#table-of-contents) |
| [TOC](#objects) |       :goggles:        | `:goggles:`                   |      :lab_coat:      | `:lab_coat:`           | [TOC](#table-of-contents) |
| [TOC](#objects) |     :safety_vest:      | `:safety_vest:`               |      :necktie:       | `:necktie:`            | [TOC](#table-of-contents) |
| [TOC](#objects) |        :shirt:         | `:shirt:` <br /> `:tshirt:`   |       :jeans:        | `:jeans:`              | [TOC](#table-of-contents) |
| [TOC](#objects) |        :scarf:         | `:scarf:`                     |       :gloves:       | `:gloves:`             | [TOC](#table-of-contents) |
| [TOC](#objects) |         :coat:         | `:coat:`                      |       :socks:        | `:socks:`              | [TOC](#table-of-contents) |
| [TOC](#objects) |        :dress:         | `:dress:`                     |       :kimono:       | `:kimono:`             | [TOC](#table-of-contents) |
| [TOC](#objects) |         :sari:         | `:sari:`                      | :one_piece_swimsuit: | `:one_piece_swimsuit:` | [TOC](#table-of-contents) |
| [TOC](#objects) |      :swim_brief:      | `:swim_brief:`                |       :shorts:       | `:shorts:`             | [TOC](#table-of-contents) |
| [TOC](#objects) |        :bikini:        | `:bikini:`                    |   :womans_clothes:   | `:womans_clothes:`     | [TOC](#table-of-contents) |
| [TOC](#objects) |        :purse:         | `:purse:`                     |      :handbag:       | `:handbag:`            | [TOC](#table-of-contents) |
| [TOC](#objects) |        :pouch:         | `:pouch:`                     |      :shopping:      | `:shopping:`           | [TOC](#table-of-contents) |
| [TOC](#objects) |    :school_satchel:    | `:school_satchel:`            |    :thong_sandal:    | `:thong_sandal:`       | [TOC](#table-of-contents) |
| [TOC](#objects) |      :mans_shoe:       | `:mans_shoe:` <br /> `:shoe:` |   :athletic_shoe:    | `:athletic_shoe:`      | [TOC](#table-of-contents) |
| [TOC](#objects) |     :hiking_boot:      | `:hiking_boot:`               |     :flat_shoe:      | `:flat_shoe:`          | [TOC](#table-of-contents) |
| [TOC](#objects) |      :high_heel:       | `:high_heel:`                 |       :sandal:       | `:sandal:`             | [TOC](#table-of-contents) |
| [TOC](#objects) |     :ballet_shoes:     | `:ballet_shoes:`              |        :boot:        | `:boot:`               | [TOC](#table-of-contents) |
| [TOC](#objects) |        :crown:         | `:crown:`                     |     :womans_hat:     | `:womans_hat:`         | [TOC](#table-of-contents) |
| [TOC](#objects) |        :TOChat:        | `:TOChat:`                    |    :mortar_board:    | `:mortar_board:`       | [TOC](#table-of-contents) |
| [TOC](#objects) |      :billed_cap:      | `:billed_cap:`                |  :military_helmet:   | `:military_helmet:`    | [TOC](#table-of-contents) |
| [TOC](#objects) | :rescue_worker_helmet: | `:rescue_worker_helmet:`      |    :prayer_beads:    | `:prayer_beads:`       | [TOC](#table-of-contents) |
| [TOC](#objects) |       :lipstick:       | `:lipstick:`                  |        :ring:        | `:ring:`               | [TOC](#table-of-contents) |
| [TOC](#objects) |         :gem:          | `:gem:`                       |                      |                        | [TOC](#table-of-contents) |

#### Sound

|                 |      ico      | shortcode       |     ico      | shortcode      |                           |
| --------------- | :-----------: | --------------- | :----------: | -------------- | ------------------------- |
| [TOC](#objects) |    :mute:     | `:mute:`        |  :speaker:   | `:speaker:`    | [TOC](#table-of-contents) |
| [TOC](#objects) |    :sound:    | `:sound:`       | :loud_sound: | `:loud_sound:` | [TOC](#table-of-contents) |
| [TOC](#objects) | :loudspeaker: | `:loudspeaker:` |    :mega:    | `:mega:`       | [TOC](#table-of-contents) |
| [TOC](#objects) | :postal_horn: | `:postal_horn:` |    :bell:    | `:bell:`       | [TOC](#table-of-contents) |
| [TOC](#objects) |   :no_bell:   | `:no_bell:`     |              |                | [TOC](#table-of-contents) |

#### Music

|                 |       ico       | shortcode         |         ico         | shortcode             |                           |
| --------------- | :-------------: | ----------------- | :-----------------: | --------------------- | ------------------------- |
| [TOC](#objects) | :musical_score: | `:musical_score:` |   :musical_note:    | `:musical_note:`      | [TOC](#table-of-contents) |
| [TOC](#objects) |     :notes:     | `:notes:`         | :studio_microphone: | `:studio_microphone:` | [TOC](#table-of-contents) |
| [TOC](#objects) | :level_slider:  | `:level_slider:`  |   :control_knobs:   | `:control_knobs:`     | [TOC](#table-of-contents) |
| [TOC](#objects) |  :microphone:   | `:microphone:`    |    :headphones:     | `:headphones:`        | [TOC](#table-of-contents) |
| [TOC](#objects) |     :radio:     | `:radio:`         |                     |                       | [TOC](#table-of-contents) |

#### Musical Instrument

|                 |     ico     | shortcode     |        ico         | shortcode            |                           |
| --------------- | :---------: | ------------- | :----------------: | -------------------- | ------------------------- |
| [TOC](#objects) | :saxophone: | `:saxophone:` |    :accordion:     | `:accordion:`        | [TOC](#table-of-contents) |
| [TOC](#objects) |  :guitar:   | `:guitar:`    | :musical_keyboard: | `:musical_keyboard:` | [TOC](#table-of-contents) |
| [TOC](#objects) |  :trumpet:  | `:trumpet:`   |      :violin:      | `:violin:`           | [TOC](#table-of-contents) |
| [TOC](#objects) |   :banjo:   | `:banjo:`     |       :drum:       | `:drum:`             | [TOC](#table-of-contents) |
| [TOC](#objects) | :long_drum: | `:long_drum:` |                    |                      | [TOC](#table-of-contents) |

#### Phone

|                 |   ico    | shortcode                      |         ico          | shortcode              |                           |
| --------------- | :------: | ------------------------------ | :------------------: | ---------------------- | ------------------------- |
| [TOC](#objects) | :iphone: | `:iphone:`                     |      :calling:       | `:calling:`            | [TOC](#table-of-contents) |
| [TOC](#objects) | :phone:  | `:phone:` <br /> `:telephone:` | :telephone_receiver: | `:telephone_receiver:` | [TOC](#table-of-contents) |
| [TOC](#objects) | :pager:  | `:pager:`                      |        :fax:         | `:fax:`                | [TOC](#table-of-contents) |

#### Computer

|                 |       ico        | shortcode          |        ico         | shortcode            |                           |
| --------------- | :--------------: | ------------------ | :----------------: | -------------------- | ------------------------- |
| [TOC](#objects) |    :battery:     | `:battery:`        |  :electric_plug:   | `:electric_plug:`    | [TOC](#table-of-contents) |
| [TOC](#objects) |    :computer:    | `:computer:`       | :deskTOC_computer: | `:deskTOC_computer:` | [TOC](#table-of-contents) |
| [TOC](#objects) |    :printer:     | `:printer:`        |     :keyboard:     | `:keyboard:`         | [TOC](#table-of-contents) |
| [TOC](#objects) | :computer_mouse: | `:computer_mouse:` |    :trackball:     | `:trackball:`        | [TOC](#table-of-contents) |
| [TOC](#objects) |    :minidisc:    | `:minidisc:`       |   :floppy_disk:    | `:floppy_disk:`      | [TOC](#table-of-contents) |
| [TOC](#objects) |       :cd:       | `:cd:`             |       :dvd:        | `:dvd:`              | [TOC](#table-of-contents) |
| [TOC](#objects) |     :abacus:     | `:abacus:`         |                    |                      | [TOC](#table-of-contents) |

#### Light & Video

|                 |        ico        | shortcode                              |      ico       | shortcode        |                           |
| --------------- | :---------------: | -------------------------------------- | :------------: | ---------------- | ------------------------- |
| [TOC](#objects) |  :movie_camera:   | `:movie_camera:`                       |  :film_strip:  | `:film_strip:`   | [TOC](#table-of-contents) |
| [TOC](#objects) | :film_projector:  | `:film_projector:`                     |   :clapper:    | `:clapper:`      | [TOC](#table-of-contents) |
| [TOC](#objects) |       :tv:        | `:tv:`                                 |    :camera:    | `:camera:`       | [TOC](#table-of-contents) |
| [TOC](#objects) |  :camera_flash:   | `:camera_flash:`                       | :video_camera: | `:video_camera:` | [TOC](#table-of-contents) |
| [TOC](#objects) |       :vhs:       | `:vhs:`                                |     :mag:      | `:mag:`          | [TOC](#table-of-contents) |
| [TOC](#objects) |    :mag_right:    | `:mag_right:`                          |    :candle:    | `:candle:`       | [TOC](#table-of-contents) |
| [TOC](#objects) |      :bulb:       | `:bulb:`                               |  :flashlight:  | `:flashlight:`   | [TOC](#table-of-contents) |
| [TOC](#objects) | :izakaya_lantern: | `:izakaya_lantern:` <br /> `:lantern:` |  :diya_lamp:   | `:diya_lamp:`    | [TOC](#table-of-contents) |

#### Book Paper

|                 |               ico                | shortcode                          |       ico        | shortcode          |                           |
| --------------- | :------------------------------: | ---------------------------------- | :--------------: | ------------------ | ------------------------- |
| [TOC](#objects) | :notebook_with_decorative_cover: | `:notebook_with_decorative_cover:` |  :closed_book:   | `:closed_book:`    | [TOC](#table-of-contents) |
| [TOC](#objects) |              :book:              | `:book:` <br /> `:open_book:`      |   :green_book:   | `:green_book:`     | [TOC](#table-of-contents) |
| [TOC](#objects) |           :blue_book:            | `:blue_book:`                      |  :orange_book:   | `:orange_book:`    | [TOC](#table-of-contents) |
| [TOC](#objects) |             :books:              | `:books:`                          |    :notebook:    | `:notebook:`       | [TOC](#table-of-contents) |
| [TOC](#objects) |             :ledger:             | `:ledger:`                         | :page_with_curl: | `:page_with_curl:` | [TOC](#table-of-contents) |
| [TOC](#objects) |             :scroll:             | `:scroll:`                         | :page_facing_up: | `:page_facing_up:` | [TOC](#table-of-contents) |
| [TOC](#objects) |           :newspaper:            | `:newspaper:`                      | :newspaper_roll: | `:newspaper_roll:` | [TOC](#table-of-contents) |
| [TOC](#objects) |         :bookmark_tabs:          | `:bookmark_tabs:`                  |    :bookmark:    | `:bookmark:`       | [TOC](#table-of-contents) |
| [TOC](#objects) |             :label:              | `:label:`                          |                  |                    | [TOC](#table-of-contents) |

#### Money

|                 |        ico         | shortcode            |      ico      | shortcode       |                           |
| --------------- | :----------------: | -------------------- | :-----------: | --------------- | ------------------------- |
| [TOC](#objects) |     :moneybag:     | `:moneybag:`         |    :coin:     | `:coin:`        | [TOC](#table-of-contents) |
| [TOC](#objects) |       :yen:        | `:yen:`              |   :dollar:    | `:dollar:`      | [TOC](#table-of-contents) |
| [TOC](#objects) |       :euro:       | `:euro:`             |    :pound:    | `:pound:`       | [TOC](#table-of-contents) |
| [TOC](#objects) | :money_with_wings: | `:money_with_wings:` | :credit_card: | `:credit_card:` | [TOC](#table-of-contents) |
| [TOC](#objects) |     :receipt:      | `:receipt:`          |    :chart:    | `:chart:`       | [TOC](#table-of-contents) |

#### Mail

|                 |          ico           | shortcode                |          ico          | shortcode                   |                           |
| --------------- | :--------------------: | ------------------------ | :-------------------: | --------------------------- | ------------------------- |
| [TOC](#objects) |       :envelope:       | `:envelope:`             |       :e-mail:        | `:e-mail:` <br /> `:email:` | [TOC](#table-of-contents) |
| [TOC](#objects) |  :incoming_envelope:   | `:incoming_envelope:`    | :envelope_with_arrow: | `:envelope_with_arrow:`     | [TOC](#table-of-contents) |
| [TOC](#objects) |     :outbox_tray:      | `:outbox_tray:`          |     :inbox_tray:      | `:inbox_tray:`              | [TOC](#table-of-contents) |
| [TOC](#objects) |       :package:        | `:package:`              |       :mailbox:       | `:mailbox:`                 | [TOC](#table-of-contents) |
| [TOC](#objects) |    :mailbox_closed:    | `:mailbox_closed:`       |  :mailbox_with_mail:  | `:mailbox_with_mail:`       | [TOC](#table-of-contents) |
| [TOC](#objects) | :mailbox_with_no_mail: | `:mailbox_with_no_mail:` |       :postbox:       | `:postbox:`                 | [TOC](#table-of-contents) |
| [TOC](#objects) |      :ballot_box:      | `:ballot_box:`           |                       |                             | [TOC](#table-of-contents) |

#### Writing

|                 |      ico       | shortcode                  |     ico     | shortcode     |                           |
| --------------- | :------------: | -------------------------- | :---------: | ------------- | ------------------------- |
| [TOC](#objects) |   :pencil2:    | `:pencil2:`                | :black_nib: | `:black_nib:` | [TOC](#table-of-contents) |
| [TOC](#objects) | :fountain_pen: | `:fountain_pen:`           |    :pen:    | `:pen:`       | [TOC](#table-of-contents) |
| [TOC](#objects) |  :paintbrush:  | `:paintbrush:`             |  :crayon:   | `:crayon:`    | [TOC](#table-of-contents) |
| [TOC](#objects) |     :memo:     | `:memo:` <br /> `:pencil:` |             |               | [TOC](#table-of-contents) |

#### Office

|                 |             ico              | shortcode                      |            ico             | shortcode                    |                           |
| --------------- | :--------------------------: | ------------------------------ | :------------------------: | ---------------------------- | ------------------------- |
| [TOC](#objects) |         :briefcase:          | `:briefcase:`                  |       :file_folder:        | `:file_folder:`              | [TOC](#table-of-contents) |
| [TOC](#objects) |      :open_file_folder:      | `:open_file_folder:`           |   :card_index_dividers:    | `:card_index_dividers:`      | [TOC](#table-of-contents) |
| [TOC](#objects) |            :date:            | `:date:`                       |         :calendar:         | `:calendar:`                 | [TOC](#table-of-contents) |
| [TOC](#objects) |       :spiral_notepad:       | `:spiral_notepad:`             |     :spiral_calendar:      | `:spiral_calendar:`          | [TOC](#table-of-contents) |
| [TOC](#objects) |         :card_index:         | `:card_index:`                 | :chart_with_upwards_trend: | `:chart_with_upwards_trend:` | [TOC](#table-of-contents) |
| [TOC](#objects) | :chart_with_downwards_trend: | `:chart_with_downwards_trend:` |        :bar_chart:         | `:bar_chart:`                | [TOC](#table-of-contents) |
| [TOC](#objects) |         :clipboard:          | `:clipboard:`                  |         :pushpin:          | `:pushpin:`                  | [TOC](#table-of-contents) |
| [TOC](#objects) |       :round_pushpin:        | `:round_pushpin:`              |        :paperclip:         | `:paperclip:`                | [TOC](#table-of-contents) |
| [TOC](#objects) |         :paperclips:         | `:paperclips:`                 |      :straight_ruler:      | `:straight_ruler:`           | [TOC](#table-of-contents) |
| [TOC](#objects) |      :triangular_ruler:      | `:triangular_ruler:`           |         :scissors:         | `:scissors:`                 | [TOC](#table-of-contents) |
| [TOC](#objects) |       :card_file_box:        | `:card_file_box:`              |       :file_cabinet:       | `:file_cabinet:`             | [TOC](#table-of-contents) |
| [TOC](#objects) |        :wastebasket:         | `:wastebasket:`                |                            |                              | [TOC](#table-of-contents) |

#### Lock

|                 |         ico         | shortcode             |          ico           | shortcode                |                           |
| --------------- | :-----------------: | --------------------- | :--------------------: | ------------------------ | ------------------------- |
| [TOC](#objects) |       :lock:        | `:lock:`              |        :unlock:        | `:unlock:`               | [TOC](#table-of-contents) |
| [TOC](#objects) | :lock_with_ink_pen: | `:lock_with_ink_pen:` | :closed_lock_with_key: | `:closed_lock_with_key:` | [TOC](#table-of-contents) |
| [TOC](#objects) |        :key:        | `:key:`               |       :old_key:        | `:old_key:`              | [TOC](#table-of-contents) |

#### Tool

|                 |         ico         | shortcode             |        ico        | shortcode           |                           |
| --------------- | :-----------------: | --------------------- | :---------------: | ------------------- | ------------------------- |
| [TOC](#objects) |      :hammer:       | `:hammer:`            |       :axe:       | `:axe:`             | [TOC](#table-of-contents) |
| [TOC](#objects) |       :pick:        | `:pick:`              | :hammer_and_pick: | `:hammer_and_pick:` | [TOC](#table-of-contents) |
| [TOC](#objects) | :hammer_and_wrench: | `:hammer_and_wrench:` |     :dagger:      | `:dagger:`          | [TOC](#table-of-contents) |
| [TOC](#objects) |  :crossed_swords:   | `:crossed_swords:`    |      :bomb:       | `:bomb:`            | [TOC](#table-of-contents) |
| [TOC](#objects) |     :boomerang:     | `:boomerang:`         |  :bow_and_arrow:  | `:bow_and_arrow:`   | [TOC](#table-of-contents) |
| [TOC](#objects) |      :shield:       | `:shield:`            |  :carpentry_saw:  | `:carpentry_saw:`   | [TOC](#table-of-contents) |
| [TOC](#objects) |      :wrench:       | `:wrench:`            |   :screwdriver:   | `:screwdriver:`     | [TOC](#table-of-contents) |
| [TOC](#objects) |   :nut_and_bolt:    | `:nut_and_bolt:`      |      :gear:       | `:gear:`            | [TOC](#table-of-contents) |
| [TOC](#objects) |       :clamp:       | `:clamp:`             |  :balance_scale:  | `:balance_scale:`   | [TOC](#table-of-contents) |
| [TOC](#objects) |   :probing_cane:    | `:probing_cane:`      |      :link:       | `:link:`            | [TOC](#table-of-contents) |
| [TOC](#objects) |      :chains:       | `:chains:`            |      :hook:       | `:hook:`            | [TOC](#table-of-contents) |
| [TOC](#objects) |      :toolbox:      | `:toolbox:`           |     :magnet:      | `:magnet:`          | [TOC](#table-of-contents) |
| [TOC](#objects) |      :ladder:       | `:ladder:`            |                   |                     | [TOC](#table-of-contents) |

#### Science

|                 |     ico      | shortcode      |     ico     | shortcode     |                           |
| --------------- | :----------: | -------------- | :---------: | ------------- | ------------------------- |
| [TOC](#objects) |  :alembic:   | `:alembic:`    | :test_tube: | `:test_tube:` | [TOC](#table-of-contents) |
| [TOC](#objects) | :petri_dish: | `:petri_dish:` |    :dna:    | `:dna:`       | [TOC](#table-of-contents) |
| [TOC](#objects) | :microscope: | `:microscope:` | :telescope: | `:telescope:` | [TOC](#table-of-contents) |
| [TOC](#objects) | :satellite:  | `:satellite:`  |             |               | [TOC](#table-of-contents) |

#### Medical

|                 |      ico      | shortcode       |        ico         | shortcode            |                           |
| --------------- | :-----------: | --------------- | :----------------: | -------------------- | ------------------------- |
| [TOC](#objects) |   :syringe:   | `:syringe:`     |  :drop_of_blood:   | `:drop_of_blood:`    | [TOC](#table-of-contents) |
| [TOC](#objects) |    :pill:     | `:pill:`        | :adhesive_bandage: | `:adhesive_bandage:` | [TOC](#table-of-contents) |
| [TOC](#objects) | :stethoscope: | `:stethoscope:` |                    |                      | [TOC](#table-of-contents) |

#### Household

|                 |         ico         | shortcode             |       ico        | shortcode          |                           |
| --------------- | :-----------------: | --------------------- | :--------------: | ------------------ | ------------------------- |
| [TOC](#objects) |       :door:        | `:door:`              |    :elevator:    | `:elevator:`       | [TOC](#table-of-contents) |
| [TOC](#objects) |      :mirror:       | `:mirror:`            |     :window:     | `:window:`         | [TOC](#table-of-contents) |
| [TOC](#objects) |        :bed:        | `:bed:`               | :couch_and_lamp: | `:couch_and_lamp:` | [TOC](#table-of-contents) |
| [TOC](#objects) |       :chair:       | `:chair:`             |     :toilet:     | `:toilet:`         | [TOC](#table-of-contents) |
| [TOC](#objects) |      :plunger:      | `:plunger:`           |     :shower:     | `:shower:`         | [TOC](#table-of-contents) |
| [TOC](#objects) |      :bathtub:      | `:bathtub:`           |   :mouse_trap:   | `:mouse_trap:`     | [TOC](#table-of-contents) |
| [TOC](#objects) |       :razor:       | `:razor:`             | :lotion_bottle:  | `:lotion_bottle:`  | [TOC](#table-of-contents) |
| [TOC](#objects) |    :safety_pin:     | `:safety_pin:`        |     :broom:      | `:broom:`          | [TOC](#table-of-contents) |
| [TOC](#objects) |      :basket:       | `:basket:`            | :roll_of_paper:  | `:roll_of_paper:`  | [TOC](#table-of-contents) |
| [TOC](#objects) |      :bucket:       | `:bucket:`            |      :soap:      | `:soap:`           | [TOC](#table-of-contents) |
| [TOC](#objects) |    :toothbrush:     | `:toothbrush:`        |     :sponge:     | `:sponge:`         | [TOC](#table-of-contents) |
| [TOC](#objects) | :fire_extinguisher: | `:fire_extinguisher:` | :shopping_cart:  | `:shopping_cart:`  | [TOC](#table-of-contents) |

#### Other Object

|                 |      ico       | shortcode        |      ico      | shortcode       |                           |
| --------------- | :------------: | ---------------- | :-----------: | --------------- | ------------------------- |
| [TOC](#objects) |   :smoking:    | `:smoking:`      |   :coffin:    | `:coffin:`      | [TOC](#table-of-contents) |
| [TOC](#objects) |  :headstone:   | `:headstone:`    | :funeral_urn: | `:funeral_urn:` | [TOC](#table-of-contents) |
| [TOC](#objects) | :nazar_amulet: | `:nazar_amulet:` |    :moyai:    | `:moyai:`       | [TOC](#table-of-contents) |
| [TOC](#objects) |   :placard:    | `:placard:`      |               |                 | [TOC](#table-of-contents) |

### Symbols

- [Transport Sign](#transport-sign)
- [Warning](#warning)
- [Arrow](#arrow)
- [Religion](#religion)
- [Zodiac](#zodiac)
- [Av Symbol](#av-symbol)
- [Gender](#gender)
- [Math](#math)
- [Punctuation](#punctuation)
- [Currency](#currency)
- [Other Symbol](#other-symbol)
- [Keycap](#keycap)
- [Alphanum](#alphanum)
- [Geometric](#geometric)

#### Transport Sign

|                 |       ico       | shortcode         |            ico            | shortcode                   |                           |
| --------------- | :-------------: | ----------------- | :-----------------------: | --------------------------- | ------------------------- |
| [TOC](#symbols) |      :atm:      | `:atm:`           | :put_litter_in_its_place: | `:put_litter_in_its_place:` | [TOC](#table-of-contents) |
| [TOC](#symbols) | :potable_water: | `:potable_water:` |       :wheelchair:        | `:wheelchair:`              | [TOC](#table-of-contents) |
| [TOC](#symbols) |     :mens:      | `:mens:`          |         :womens:          | `:womens:`                  | [TOC](#table-of-contents) |
| [TOC](#symbols) |   :restroom:    | `:restroom:`      |       :baby_symbol:       | `:baby_symbol:`             | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :wc:       | `:wc:`            |    :passport_control:     | `:passport_control:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :customs:    | `:customs:`       |      :baggage_claim:      | `:baggage_claim:`           | [TOC](#table-of-contents) |
| [TOC](#symbols) | :left_luggage:  | `:left_luggage:`  |                           |                             | [TOC](#table-of-contents) |

#### Warning

|                 |       ico        | shortcode          |         ico         | shortcode             |                           |
| --------------- | :--------------: | ------------------ | :-----------------: | --------------------- | ------------------------- |
| [TOC](#symbols) |    :warning:     | `:warning:`        | :children_crossing: | `:children_crossing:` | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :no_entry:    | `:no_entry:`       |   :no_entry_sign:   | `:no_entry_sign:`     | [TOC](#table-of-contents) |
| [TOC](#symbols) |  :no_bicycles:   | `:no_bicycles:`    |    :no_smoking:     | `:no_smoking:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) | :do_not_litter:  | `:do_not_litter:`  | :non-potable_water: | `:non-potable_water:` | [TOC](#table-of-contents) |
| [TOC](#symbols) | :no_pedestrians: | `:no_pedestrians:` | :no_mobile_phones:  | `:no_mobile_phones:`  | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :underage:    | `:underage:`       |    :radioactive:    | `:radioactive:`       | [TOC](#table-of-contents) |
| [TOC](#symbols) |   :biohazard:    | `:biohazard:`      |                     |                       | [TOC](#table-of-contents) |

#### Arrow

|                 |             ico             | shortcode                     |            ico            | shortcode                   |                           |
| --------------- | :-------------------------: | ----------------------------- | :-----------------------: | --------------------------- | ------------------------- |
| [TOC](#symbols) |         :arrow_up:          | `:arrow_up:`                  |    :arrow_upper_right:    | `:arrow_upper_right:`       | [TOC](#table-of-contents) |
| [TOC](#symbols) |        :arrow_right:        | `:arrow_right:`               |    :arrow_lower_right:    | `:arrow_lower_right:`       | [TOC](#table-of-contents) |
| [TOC](#symbols) |        :arrow_down:         | `:arrow_down:`                |    :arrow_lower_left:     | `:arrow_lower_left:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) |        :arrow_left:         | `:arrow_left:`                |    :arrow_upper_left:     | `:arrow_upper_left:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) |       :arrow_up_down:       | `:arrow_up_down:`             |    :left_right_arrow:     | `:left_right_arrow:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) | :leftwards_arrow_with_hook: | `:leftwards_arrow_with_hook:` |    :arrow_right_hook:     | `:arrow_right_hook:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) |     :arrow_heading_up:      | `:arrow_heading_up:`          |   :arrow_heading_down:    | `:arrow_heading_down:`      | [TOC](#table-of-contents) |
| [TOC](#symbols) |     :arrows_clockwise:      | `:arrows_clockwise:`          | :arrows_counterclockwise: | `:arrows_counterclockwise:` | [TOC](#table-of-contents) |
| [TOC](#symbols) |           :back:            | `:back:`                      |           :end:           | `:end:`                     | [TOC](#table-of-contents) |
| [TOC](#symbols) |            :on:             | `:on:`                        |          :soon:           | `:soon:`                    | [TOC](#table-of-contents) |
| [TOC](#symbols) |            :TOC:            | `:TOC:`                       |                           |                             | [TOC](#table-of-contents) |

#### Religion

|                 |         ico         | shortcode             |        ico         | shortcode            |                           |
| --------------- | :-----------------: | --------------------- | :----------------: | -------------------- | ------------------------- |
| [TOC](#symbols) | :place_of_worship:  | `:place_of_worship:`  |   :atom_symbol:    | `:atom_symbol:`      | [TOC](#table-of-contents) |
| [TOC](#symbols) |        :om:         | `:om:`                |  :star_of_david:   | `:star_of_david:`    | [TOC](#table-of-contents) |
| [TOC](#symbols) |  :wheel_of_dharma:  | `:wheel_of_dharma:`   |     :yin_yang:     | `:yin_yang:`         | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :latin_cross:    | `:latin_cross:`       |  :orthodox_cross:  | `:orthodox_cross:`   | [TOC](#table-of-contents) |
| [TOC](#symbols) | :star_and_crescent: | `:star_and_crescent:` |   :peace_symbol:   | `:peace_symbol:`     | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :menorah:      | `:menorah:`           | :six_pointed_star: | `:six_pointed_star:` | [TOC](#table-of-contents) |

#### Zodiac

|                 |      ico      | shortcode       |     ico     | shortcode     |                           |
| --------------- | :-----------: | --------------- | :---------: | ------------- | ------------------------- |
| [TOC](#symbols) |    :aries:    | `:aries:`       |  :taurus:   | `:taurus:`    | [TOC](#table-of-contents) |
| [TOC](#symbols) |   :gemini:    | `:gemini:`      |  :cancer:   | `:cancer:`    | [TOC](#table-of-contents) |
| [TOC](#symbols) |     :leo:     | `:leo:`         |   :virgo:   | `:virgo:`     | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :libra:    | `:libra:`       | :scorpius:  | `:scorpius:`  | [TOC](#table-of-contents) |
| [TOC](#symbols) | :sagittarius: | `:sagittarius:` | :capricorn: | `:capricorn:` | [TOC](#table-of-contents) |
| [TOC](#symbols) |  :aquarius:   | `:aquarius:`    |  :pisces:   | `:pisces:`    | [TOC](#table-of-contents) |
| [TOC](#symbols) |  :ophiuchus:  | `:ophiuchus:`   |             |               | [TOC](#table-of-contents) |

#### Av Symbol

|                 |             ico             | shortcode                     |           ico           | shortcode                 |                           |
| --------------- | :-------------------------: | ----------------------------- | :---------------------: | ------------------------- | ------------------------- |
| [TOC](#symbols) | :twisted_rightwards_arrows: | `:twisted_rightwards_arrows:` |        :repeat:         | `:repeat:`                | [TOC](#table-of-contents) |
| [TOC](#symbols) |        :repeat_one:         | `:repeat_one:`                |     :arrow_forward:     | `:arrow_forward:`         | [TOC](#table-of-contents) |
| [TOC](#symbols) |       :fast_forward:        | `:fast_forward:`              |   :next_track_button:   | `:next_track_button:`     | [TOC](#table-of-contents) |
| [TOC](#symbols) |   :play_or_pause_button:    | `:play_or_pause_button:`      |    :arrow_backward:     | `:arrow_backward:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) |          :rewind:           | `:rewind:`                    | :previous_track_button: | `:previous_track_button:` | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :arrow_up_small:       | `:arrow_up_small:`            |    :arrow_double_up:    | `:arrow_double_up:`       | [TOC](#table-of-contents) |
| [TOC](#symbols) |     :arrow_down_small:      | `:arrow_down_small:`          |   :arrow_double_down:   | `:arrow_double_down:`     | [TOC](#table-of-contents) |
| [TOC](#symbols) |       :pause_button:        | `:pause_button:`              |      :sTOC_button:      | `:sTOC_button:`           | [TOC](#table-of-contents) |
| [TOC](#symbols) |       :record_button:       | `:record_button:`             |     :eject_button:      | `:eject_button:`          | [TOC](#table-of-contents) |
| [TOC](#symbols) |          :cinema:           | `:cinema:`                    |    :low_brightness:     | `:low_brightness:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :high_brightness:      | `:high_brightness:`           |    :signal_strength:    | `:signal_strength:`       | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :vibration_mode:       | `:vibration_mode:`            |   :mobile_phone_off:    | `:mobile_phone_off:`      | [TOC](#table-of-contents) |

#### Gender

|                 |         ico          | shortcode              |     ico     | shortcode     |                           |
| --------------- | :------------------: | ---------------------- | :---------: | ------------- | ------------------------- |
| [TOC](#symbols) |    :female_sign:     | `:female_sign:`        | :male_sign: | `:male_sign:` | [TOC](#table-of-contents) |
| [TOC](#symbols) | :transgender_symbol: | `:transgender_symbol:` |             |               | [TOC](#table-of-contents) |

#### Math

|                 |           ico            | shortcode                  |          ico          | shortcode               |                           |
| --------------- | :----------------------: | -------------------------- | :-------------------: | ----------------------- | ------------------------- |
| [TOC](#symbols) | :heavy_multiplication_x: | `:heavy_multiplication_x:` |   :heavy_plus_sign:   | `:heavy_plus_sign:`     | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :heavy_minus_sign:    | `:heavy_minus_sign:`       | :heavy_division_sign: | `:heavy_division_sign:` | [TOC](#table-of-contents) |
| [TOC](#symbols) |        :infinity:        | `:infinity:`               |                       |                         | [TOC](#table-of-contents) |

#### Punctuation

|                 |        ico         | shortcode            |       ico       | shortcode                                         |                           |
| --------------- | :----------------: | -------------------- | :-------------: | ------------------------------------------------- | ------------------------- |
| [TOC](#symbols) |     :bangbang:     | `:bangbang:`         |  :interrobang:  | `:interrobang:`                                   | [TOC](#table-of-contents) |
| [TOC](#symbols) |     :question:     | `:question:`         | :grey_question: | `:grey_question:`                                 | [TOC](#table-of-contents) |
| [TOC](#symbols) | :grey_exclamation: | `:grey_exclamation:` |  :exclamation:  | `:exclamation:` <br /> `:heavy_exclamation_mark:` | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :wavy_dash:     | `:wavy_dash:`        |                 |                                                   | [TOC](#table-of-contents) |

#### Currency

|                 |         ico         | shortcode             |         ico         | shortcode             |                           |
| --------------- | :-----------------: | --------------------- | :-----------------: | --------------------- | ------------------------- |
| [TOC](#symbols) | :currency_exchange: | `:currency_exchange:` | :heavy_dollar_sign: | `:heavy_dollar_sign:` | [TOC](#table-of-contents) |

#### Other Symbol

|                 |            ico             | shortcode                    |              ico              | shortcode                       |                           |
| --------------- | :------------------------: | ---------------------------- | :---------------------------: | ------------------------------- | ------------------------- |
| [TOC](#symbols) |      :medical_symbol:      | `:medical_symbol:`           |           :recycle:           | `:recycle:`                     | [TOC](#table-of-contents) |
| [TOC](#symbols) |       :fleur_de_lis:       | `:fleur_de_lis:`             |           :trident:           | `:trident:`                     | [TOC](#table-of-contents) |
| [TOC](#symbols) |        :name_badge:        | `:name_badge:`               |          :beginner:           | `:beginner:`                    | [TOC](#table-of-contents) |
| [TOC](#symbols) |            :o:             | `:o:`                        |      :white_check_mark:       | `:white_check_mark:`            | [TOC](#table-of-contents) |
| [TOC](#symbols) |  :ballot_box_with_check:   | `:ballot_box_with_check:`    |      :heavy_check_mark:       | `:heavy_check_mark:`            | [TOC](#table-of-contents) |
| [TOC](#symbols) |            :x:             | `:x:`                        | :negative_squared_cross_mark: | `:negative_squared_cross_mark:` | [TOC](#table-of-contents) |
| [TOC](#symbols) |        :curly_loop:        | `:curly_loop:`               |            :loop:             | `:loop:`                        | [TOC](#table-of-contents) |
| [TOC](#symbols) |  :part_alternation_mark:   | `:part_alternation_mark:`    |    :eight_spoked_asterisk:    | `:eight_spoked_asterisk:`       | [TOC](#table-of-contents) |
| [TOC](#symbols) | :eight_pointed_black_star: | `:eight_pointed_black_star:` |           :sparkle:           | `:sparkle:`                     | [TOC](#table-of-contents) |
| [TOC](#symbols) |        :copyright:         | `:copyright:`                |         :registered:          | `:registered:`                  | [TOC](#table-of-contents) |
| [TOC](#symbols) |            :tm:            | `:tm:`                       |                               |                                 | [TOC](#table-of-contents) |

#### Keycap

|                 |     ico      | shortcode      |    ico     | shortcode    |                           |
| --------------- | :----------: | -------------- | :--------: | ------------ | ------------------------- |
| [TOC](#symbols) |    :hash:    | `:hash:`       | :asterisk: | `:asterisk:` | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :zero:    | `:zero:`       |   :one:    | `:one:`      | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :two:     | `:two:`        |  :three:   | `:three:`    | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :four:    | `:four:`       |   :five:   | `:five:`     | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :six:     | `:six:`        |  :seven:   | `:seven:`    | [TOC](#table-of-contents) |
| [TOC](#symbols) |   :eight:    | `:eight:`      |   :nine:   | `:nine:`     | [TOC](#table-of-contents) |
| [TOC](#symbols) | :keycap_ten: | `:keycap_ten:` |            |              | [TOC](#table-of-contents) |

#### Alphanum

|                 |      ico       | shortcode        |          ico          | shortcode               |                           |
| --------------- | :------------: | ---------------- | :-------------------: | ----------------------- | ------------------------- |
| [TOC](#symbols) | :capital_abcd: | `:capital_abcd:` |        :abcd:         | `:abcd:`                | [TOC](#table-of-contents) |
| [TOC](#symbols) |     :1234:     | `:1234:`         |       :symbols:       | `:symbols:`             | [TOC](#table-of-contents) |
| [TOC](#symbols) |     :abc:      | `:abc:`          |          :a:          | `:a:`                   | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :ab:      | `:ab:`           |          :b:          | `:b:`                   | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :cl:      | `:cl:`           |        :cool:         | `:cool:`                | [TOC](#table-of-contents) |
| [TOC](#symbols) |     :free:     | `:free:`         | :information_source:  | `:information_source:`  | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :id:      | `:id:`           |          :m:          | `:m:`                   | [TOC](#table-of-contents) |
| [TOC](#symbols) |     :new:      | `:new:`          |         :ng:          | `:ng:`                  | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :o2:      | `:o2:`           |         :ok:          | `:ok:`                  | [TOC](#table-of-contents) |
| [TOC](#symbols) |   :parking:    | `:parking:`      |         :sos:         | `:sos:`                 | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :up:      | `:up:`           |         :vs:          | `:vs:`                  | [TOC](#table-of-contents) |
| [TOC](#symbols) |     :koko:     | `:koko:`         |         :sa:          | `:sa:`                  | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :u6708:     | `:u6708:`        |        :u6709:        | `:u6709:`               | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :u6307:     | `:u6307:`        | :ideograph_advantage: | `:ideograph_advantage:` | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :u5272:     | `:u5272:`        |        :u7121:        | `:u7121:`               | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :u7981:     | `:u7981:`        |       :accept:        | `:accept:`              | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :u7533:     | `:u7533:`        |        :u5408:        | `:u5408:`               | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :u7a7a:     | `:u7a7a:`        |   :congratulations:   | `:congratulations:`     | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :secret:    | `:secret:`       |        :u55b6:        | `:u55b6:`               | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :u6e80:     | `:u6e80:`        |                       |                         | [TOC](#table-of-contents) |

#### Geometric

|                 |                ico                | shortcode                           |             ico             | shortcode                     |                           |
| --------------- | :-------------------------------: | ----------------------------------- | :-------------------------: | ----------------------------- | ------------------------- |
| [TOC](#symbols) |           :red_circle:            | `:red_circle:`                      |       :orange_circle:       | `:orange_circle:`             | [TOC](#table-of-contents) |
| [TOC](#symbols) |          :yellow_circle:          | `:yellow_circle:`                   |       :green_circle:        | `:green_circle:`              | [TOC](#table-of-contents) |
| [TOC](#symbols) |        :large_blue_circle:        | `:large_blue_circle:`               |       :purple_circle:       | `:purple_circle:`             | [TOC](#table-of-contents) |
| [TOC](#symbols) |          :brown_circle:           | `:brown_circle:`                    |       :black_circle:        | `:black_circle:`              | [TOC](#table-of-contents) |
| [TOC](#symbols) |          :white_circle:           | `:white_circle:`                    |        :red_square:         | `:red_square:`                | [TOC](#table-of-contents) |
| [TOC](#symbols) |          :orange_square:          | `:orange_square:`                   |       :yellow_square:       | `:yellow_square:`             | [TOC](#table-of-contents) |
| [TOC](#symbols) |          :green_square:           | `:green_square:`                    |        :blue_square:        | `:blue_square:`               | [TOC](#table-of-contents) |
| [TOC](#symbols) |          :purple_square:          | `:purple_square:`                   |       :brown_square:        | `:brown_square:`              | [TOC](#table-of-contents) |
| [TOC](#symbols) |       :black_large_square:        | `:black_large_square:`              |    :white_large_square:     | `:white_large_square:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) |       :black_medium_square:       | `:black_medium_square:`             |    :white_medium_square:    | `:white_medium_square:`       | [TOC](#table-of-contents) |
| [TOC](#symbols) |    :black_medium_small_square:    | `:black_medium_small_square:`       | :white_medium_small_square: | `:white_medium_small_square:` | [TOC](#table-of-contents) |
| [TOC](#symbols) |       :black_small_square:        | `:black_small_square:`              |    :white_small_square:     | `:white_small_square:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :large_orange_diamond:       | `:large_orange_diamond:`            |    :large_blue_diamond:     | `:large_blue_diamond:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) |      :small_orange_diamond:       | `:small_orange_diamond:`            |    :small_blue_diamond:     | `:small_blue_diamond:`        | [TOC](#table-of-contents) |
| [TOC](#symbols) |       :small_red_triangle:        | `:small_red_triangle:`              |  :small_red_triangle_down:  | `:small_red_triangle_down:`   | [TOC](#table-of-contents) |
| [TOC](#symbols) | :diamond_shape_with_a_dot_inside: | `:diamond_shape_with_a_dot_inside:` |       :radio_button:        | `:radio_button:`              | [TOC](#table-of-contents) |
| [TOC](#symbols) |       :white_square_button:       | `:white_square_button:`             |    :black_square_button:    | `:black_square_button:`       | [TOC](#table-of-contents) |

### Flags

- [Flag](#flag)
- [Country Flag](#country-flag)
- [Subdivision Flag](#subdivision-flag)

#### Flag

|               |        ico         | shortcode            |            ico            | shortcode                   |                           |
| ------------- | :----------------: | -------------------- | :-----------------------: | --------------------------- | ------------------------- |
| [TOC](#flags) |  :checkered_flag:  | `:checkered_flag:`   | :triangular_flag_on_post: | `:triangular_flag_on_post:` | [TOC](#table-of-contents) |
| [TOC](#flags) |  :crossed_flags:   | `:crossed_flags:`    |       :black_flag:        | `:black_flag:`              | [TOC](#table-of-contents) |
| [TOC](#flags) |    :white_flag:    | `:white_flag:`       |      :rainbow_flag:       | `:rainbow_flag:`            | [TOC](#table-of-contents) |
| [TOC](#flags) | :transgender_flag: | `:transgender_flag:` |       :pirate_flag:       | `:pirate_flag:`             | [TOC](#table-of-contents) |

#### Country Flag

|               |                  ico                   | shortcode                                |               ico                | shortcode                          |                           |
| ------------- | :------------------------------------: | ---------------------------------------- | :------------------------------: | ---------------------------------- | ------------------------- |
| [TOC](#flags) |           :ascension_island:           | `:ascension_island:`                     |            :andorra:             | `:andorra:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |         :united_arab_emirates:         | `:united_arab_emirates:`                 |          :afghanistan:           | `:afghanistan:`                    | [TOC](#table-of-contents) |
| [TOC](#flags) |           :antigua_barbuda:            | `:antigua_barbuda:`                      |            :anguilla:            | `:anguilla:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |               :albania:                | `:albania:`                              |            :armenia:             | `:armenia:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |                :angola:                | `:angola:`                               |           :antarctica:           | `:antarctica:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |              :argentina:               | `:argentina:`                            |         :american_samoa:         | `:american_samoa:`                 | [TOC](#table-of-contents) |
| [TOC](#flags) |               :austria:                | `:austria:`                              |           :australia:            | `:australia:`                      | [TOC](#table-of-contents) |
| [TOC](#flags) |                :aruba:                 | `:aruba:`                                |         :aland_islands:          | `:aland_islands:`                  | [TOC](#table-of-contents) |
| [TOC](#flags) |              :azerbaijan:              | `:azerbaijan:`                           |       :bosnia_herzegovina:       | `:bosnia_herzegovina:`             | [TOC](#table-of-contents) |
| [TOC](#flags) |               :barbados:               | `:barbados:`                             |           :bangladesh:           | `:bangladesh:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |               :belgium:                | `:belgium:`                              |          :burkina_faso:          | `:burkina_faso:`                   | [TOC](#table-of-contents) |
| [TOC](#flags) |               :bulgaria:               | `:bulgaria:`                             |            :bahrain:             | `:bahrain:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |               :burundi:                | `:burundi:`                              |             :benin:              | `:benin:`                          | [TOC](#table-of-contents) |
| [TOC](#flags) |            :st_barthelemy:             | `:st_barthelemy:`                        |            :bermuda:             | `:bermuda:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |                :brunei:                | `:brunei:`                               |            :bolivia:             | `:bolivia:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |        :caribbean_netherlands:         | `:caribbean_netherlands:`                |             :brazil:             | `:brazil:`                         | [TOC](#table-of-contents) |
| [TOC](#flags) |               :bahamas:                | `:bahamas:`                              |             :bhutan:             | `:bhutan:`                         | [TOC](#table-of-contents) |
| [TOC](#flags) |            :bouvet_island:             | `:bouvet_island:`                        |            :botswana:            | `:botswana:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |               :belarus:                | `:belarus:`                              |             :belize:             | `:belize:`                         | [TOC](#table-of-contents) |
| [TOC](#flags) |                :canada:                | `:canada:`                               |         :cocos_islands:          | `:cocos_islands:`                  | [TOC](#table-of-contents) |
| [TOC](#flags) |            :congo_kinshasa:            | `:congo_kinshasa:`                       |    :central_african_republic:    | `:central_african_republic:`       | [TOC](#table-of-contents) |
| [TOC](#flags) |          :congo_brazzaville:           | `:congo_brazzaville:`                    |          :switzerland:           | `:switzerland:`                    | [TOC](#table-of-contents) |
| [TOC](#flags) |             :cote_divoire:             | `:cote_divoire:`                         |          :cook_islands:          | `:cook_islands:`                   | [TOC](#table-of-contents) |
| [TOC](#flags) |                :chile:                 | `:chile:`                                |            :cameroon:            | `:cameroon:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |                  :cn:                  | `:cn:`                                   |            :colombia:            | `:colombia:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |          :clipperton_island:           | `:clipperton_island:`                    |           :costa_rica:           | `:costa_rica:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |                 :cuba:                 | `:cuba:`                                 |           :cape_verde:           | `:cape_verde:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |               :curacao:                | `:curacao:`                              |        :christmas_island:        | `:christmas_island:`               | [TOC](#table-of-contents) |
| [TOC](#flags) |                :cyprus:                | `:cyprus:`                               |         :czech_republic:         | `:czech_republic:`                 | [TOC](#table-of-contents) |
| [TOC](#flags) |                  :de:                  | `:de:`                                   |          :diego_garcia:          | `:diego_garcia:`                   | [TOC](#table-of-contents) |
| [TOC](#flags) |               :djibouti:               | `:djibouti:`                             |            :denmark:             | `:denmark:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |               :dominica:               | `:dominica:`                             |       :dominican_republic:       | `:dominican_republic:`             | [TOC](#table-of-contents) |
| [TOC](#flags) |               :algeria:                | `:algeria:`                              |         :ceuta_melilla:          | `:ceuta_melilla:`                  | [TOC](#table-of-contents) |
| [TOC](#flags) |               :ecuador:                | `:ecuador:`                              |            :estonia:             | `:estonia:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |                :egypt:                 | `:egypt:`                                |         :western_sahara:         | `:western_sahara:`                 | [TOC](#table-of-contents) |
| [TOC](#flags) |               :eritrea:                | `:eritrea:`                              |               :es:               | `:es:`                             | [TOC](#table-of-contents) |
| [TOC](#flags) |               :ethiopia:               | `:ethiopia:`                             |               :eu:               | `:eu:` <br /> `:european_union:`   | [TOC](#table-of-contents) |
| [TOC](#flags) |               :finland:                | `:finland:`                              |              :fiji:              | `:fiji:`                           | [TOC](#table-of-contents) |
| [TOC](#flags) |           :falkland_islands:           | `:falkland_islands:`                     |           :micronesia:           | `:micronesia:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |            :faroe_islands:             | `:faroe_islands:`                        |               :fr:               | `:fr:`                             | [TOC](#table-of-contents) |
| [TOC](#flags) |                :gabon:                 | `:gabon:`                                |               :gb:               | `:gb:` <br /> `:uk:`               | [TOC](#table-of-contents) |
| [TOC](#flags) |               :grenada:                | `:grenada:`                              |            :georgia:             | `:georgia:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |            :french_guiana:             | `:french_guiana:`                        |            :guernsey:            | `:guernsey:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |                :ghana:                 | `:ghana:`                                |           :gibraltar:            | `:gibraltar:`                      | [TOC](#table-of-contents) |
| [TOC](#flags) |              :greenland:               | `:greenland:`                            |             :gambia:             | `:gambia:`                         | [TOC](#table-of-contents) |
| [TOC](#flags) |                :guinea:                | `:guinea:`                               |           :guadeloupe:           | `:guadeloupe:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |          :equatorial_guinea:           | `:equatorial_guinea:`                    |             :greece:             | `:greece:`                         | [TOC](#table-of-contents) |
| [TOC](#flags) | :south_georgia_south_sandwich_islands: | `:south_georgia_south_sandwich_islands:` |           :guatemala:            | `:guatemala:`                      | [TOC](#table-of-contents) |
| [TOC](#flags) |                 :guam:                 | `:guam:`                                 |         :guinea_bissau:          | `:guinea_bissau:`                  | [TOC](#table-of-contents) |
| [TOC](#flags) |                :guyana:                | `:guyana:`                               |           :hong_kong:            | `:hong_kong:`                      | [TOC](#table-of-contents) |
| [TOC](#flags) |        :heard_mcdonald_islands:        | `:heard_mcdonald_islands:`               |            :honduras:            | `:honduras:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |               :croatia:                | `:croatia:`                              |             :haiti:              | `:haiti:`                          | [TOC](#table-of-contents) |
| [TOC](#flags) |               :hungary:                | `:hungary:`                              |         :canary_islands:         | `:canary_islands:`                 | [TOC](#table-of-contents) |
| [TOC](#flags) |              :indonesia:               | `:indonesia:`                            |            :ireland:             | `:ireland:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |                :israel:                | `:israel:`                               |          :isle_of_man:           | `:isle_of_man:`                    | [TOC](#table-of-contents) |
| [TOC](#flags) |                :india:                 | `:india:`                                | :british_indian_ocean_territory: | `:british_indian_ocean_territory:` | [TOC](#table-of-contents) |
| [TOC](#flags) |                 :iraq:                 | `:iraq:`                                 |              :iran:              | `:iran:`                           | [TOC](#table-of-contents) |
| [TOC](#flags) |               :iceland:                | `:iceland:`                              |               :it:               | `:it:`                             | [TOC](#table-of-contents) |
| [TOC](#flags) |                :jersey:                | `:jersey:`                               |            :jamaica:             | `:jamaica:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |                :jordan:                | `:jordan:`                               |               :jp:               | `:jp:`                             | [TOC](#table-of-contents) |
| [TOC](#flags) |                :kenya:                 | `:kenya:`                                |           :kyrgyzstan:           | `:kyrgyzstan:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |               :cambodia:               | `:cambodia:`                             |            :kiribati:            | `:kiribati:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |               :comoros:                | `:comoros:`                              |         :st_kitts_nevis:         | `:st_kitts_nevis:`                 | [TOC](#table-of-contents) |
| [TOC](#flags) |             :north_korea:              | `:north_korea:`                          |               :kr:               | `:kr:`                             | [TOC](#table-of-contents) |
| [TOC](#flags) |                :kuwait:                | `:kuwait:`                               |         :cayman_islands:         | `:cayman_islands:`                 | [TOC](#table-of-contents) |
| [TOC](#flags) |              :kazakhstan:              | `:kazakhstan:`                           |              :laos:              | `:laos:`                           | [TOC](#table-of-contents) |
| [TOC](#flags) |               :lebanon:                | `:lebanon:`                              |            :st_lucia:            | `:st_lucia:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |            :liechtenstein:             | `:liechtenstein:`                        |           :sri_lanka:            | `:sri_lanka:`                      | [TOC](#table-of-contents) |
| [TOC](#flags) |               :liberia:                | `:liberia:`                              |            :lesotho:             | `:lesotho:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |              :lithuania:               | `:lithuania:`                            |           :luxembourg:           | `:luxembourg:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |                :latvia:                | `:latvia:`                               |             :libya:              | `:libya:`                          | [TOC](#table-of-contents) |
| [TOC](#flags) |               :morocco:                | `:morocco:`                              |             :monaco:             | `:monaco:`                         | [TOC](#table-of-contents) |
| [TOC](#flags) |               :moldova:                | `:moldova:`                              |           :montenegro:           | `:montenegro:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |              :st_martin:               | `:st_martin:`                            |           :madagascar:           | `:madagascar:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |           :marshall_islands:           | `:marshall_islands:`                     |           :macedonia:            | `:macedonia:`                      | [TOC](#table-of-contents) |
| [TOC](#flags) |                 :mali:                 | `:mali:`                                 |            :myanmar:             | `:myanmar:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |               :mongolia:               | `:mongolia:`                             |             :macau:              | `:macau:`                          | [TOC](#table-of-contents) |
| [TOC](#flags) |       :northern_mariana_islands:       | `:northern_mariana_islands:`             |           :martinique:           | `:martinique:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |              :mauritania:              | `:mauritania:`                           |           :montserrat:           | `:montserrat:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |                :malta:                 | `:malta:`                                |           :mauritius:            | `:mauritius:`                      | [TOC](#table-of-contents) |
| [TOC](#flags) |               :maldives:               | `:maldives:`                             |             :malawi:             | `:malawi:`                         | [TOC](#table-of-contents) |
| [TOC](#flags) |                :mexico:                | `:mexico:`                               |            :malaysia:            | `:malaysia:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |              :mozambique:              | `:mozambique:`                           |            :namibia:             | `:namibia:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |            :new_caledonia:             | `:new_caledonia:`                        |             :niger:              | `:niger:`                          | [TOC](#table-of-contents) |
| [TOC](#flags) |            :norfolk_island:            | `:norfolk_island:`                       |            :nigeria:             | `:nigeria:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |              :nicaragua:               | `:nicaragua:`                            |          :netherlands:           | `:netherlands:`                    | [TOC](#table-of-contents) |
| [TOC](#flags) |                :norway:                | `:norway:`                               |             :nepal:              | `:nepal:`                          | [TOC](#table-of-contents) |
| [TOC](#flags) |                :nauru:                 | `:nauru:`                                |              :niue:              | `:niue:`                           | [TOC](#table-of-contents) |
| [TOC](#flags) |             :new_zealand:              | `:new_zealand:`                          |              :oman:              | `:oman:`                           | [TOC](#table-of-contents) |
| [TOC](#flags) |                :panama:                | `:panama:`                               |              :peru:              | `:peru:`                           | [TOC](#table-of-contents) |
| [TOC](#flags) |           :french_polynesia:           | `:french_polynesia:`                     |        :papua_new_guinea:        | `:papua_new_guinea:`               | [TOC](#table-of-contents) |
| [TOC](#flags) |             :philippines:              | `:philippines:`                          |            :pakistan:            | `:pakistan:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |                :poland:                | `:poland:`                               |       :st_pierre_miquelon:       | `:st_pierre_miquelon:`             | [TOC](#table-of-contents) |
| [TOC](#flags) |           :pitcairn_islands:           | `:pitcairn_islands:`                     |          :puerto_rico:           | `:puerto_rico:`                    | [TOC](#table-of-contents) |
| [TOC](#flags) |       :palestinian_territories:        | `:palestinian_territories:`              |            :portugal:            | `:portugal:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |                :palau:                 | `:palau:`                                |            :paraguay:            | `:paraguay:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |                :qatar:                 | `:qatar:`                                |            :reunion:             | `:reunion:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |               :romania:                | `:romania:`                              |             :serbia:             | `:serbia:`                         | [TOC](#table-of-contents) |
| [TOC](#flags) |                  :ru:                  | `:ru:`                                   |             :rwanda:             | `:rwanda:`                         | [TOC](#table-of-contents) |
| [TOC](#flags) |             :saudi_arabia:             | `:saudi_arabia:`                         |        :solomon_islands:         | `:solomon_islands:`                | [TOC](#table-of-contents) |
| [TOC](#flags) |              :seychelles:              | `:seychelles:`                           |             :sudan:              | `:sudan:`                          | [TOC](#table-of-contents) |
| [TOC](#flags) |                :sweden:                | `:sweden:`                               |           :singapore:            | `:singapore:`                      | [TOC](#table-of-contents) |
| [TOC](#flags) |              :st_helena:               | `:st_helena:`                            |            :slovenia:            | `:slovenia:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |          :svalbard_jan_mayen:          | `:svalbard_jan_mayen:`                   |            :slovakia:            | `:slovakia:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |             :sierra_leone:             | `:sierra_leone:`                         |           :san_marino:           | `:san_marino:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |               :senegal:                | `:senegal:`                              |            :somalia:             | `:somalia:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |               :suriname:               | `:suriname:`                             |          :south_sudan:           | `:south_sudan:`                    | [TOC](#table-of-contents) |
| [TOC](#flags) |          :sao_tome_principe:           | `:sao_tome_principe:`                    |          :el_salvador:           | `:el_salvador:`                    | [TOC](#table-of-contents) |
| [TOC](#flags) |             :sint_maarten:             | `:sint_maarten:`                         |             :syria:              | `:syria:`                          | [TOC](#table-of-contents) |
| [TOC](#flags) |              :swaziland:               | `:swaziland:`                            |        :tristan_da_cunha:        | `:tristan_da_cunha:`               | [TOC](#table-of-contents) |
| [TOC](#flags) |         :turks_caicos_islands:         | `:turks_caicos_islands:`                 |              :chad:              | `:chad:`                           | [TOC](#table-of-contents) |
| [TOC](#flags) |     :french_southern_territories:      | `:french_southern_territories:`          |              :togo:              | `:togo:`                           | [TOC](#table-of-contents) |
| [TOC](#flags) |               :thailand:               | `:thailand:`                             |           :tajikistan:           | `:tajikistan:`                     | [TOC](#table-of-contents) |
| [TOC](#flags) |               :tokelau:                | `:tokelau:`                              |          :timor_leste:           | `:timor_leste:`                    | [TOC](#table-of-contents) |
| [TOC](#flags) |             :turkmenistan:             | `:turkmenistan:`                         |            :tunisia:             | `:tunisia:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |                :tonga:                 | `:tonga:`                                |               :tr:               | `:tr:`                             | [TOC](#table-of-contents) |
| [TOC](#flags) |           :trinidad_tobago:            | `:trinidad_tobago:`                      |             :tuvalu:             | `:tuvalu:`                         | [TOC](#table-of-contents) |
| [TOC](#flags) |                :taiwan:                | `:taiwan:`                               |            :tanzania:            | `:tanzania:`                       | [TOC](#table-of-contents) |
| [TOC](#flags) |               :ukraine:                | `:ukraine:`                              |             :uganda:             | `:uganda:`                         | [TOC](#table-of-contents) |
| [TOC](#flags) |         :us_outlying_islands:          | `:us_outlying_islands:`                  |         :united_nations:         | `:united_nations:`                 | [TOC](#table-of-contents) |
| [TOC](#flags) |                  :us:                  | `:us:`                                   |            :uruguay:             | `:uruguay:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |              :uzbekistan:              | `:uzbekistan:`                           |          :vatican_city:          | `:vatican_city:`                   | [TOC](#table-of-contents) |
| [TOC](#flags) |        :st_vincent_grenadines:         | `:st_vincent_grenadines:`                |           :venezuela:            | `:venezuela:`                      | [TOC](#table-of-contents) |
| [TOC](#flags) |        :british_virgin_islands:        | `:british_virgin_islands:`               |       :us_virgin_islands:        | `:us_virgin_islands:`              | [TOC](#table-of-contents) |
| [TOC](#flags) |               :vietnam:                | `:vietnam:`                              |            :vanuatu:             | `:vanuatu:`                        | [TOC](#table-of-contents) |
| [TOC](#flags) |            :wallis_futuna:             | `:wallis_futuna:`                        |             :samoa:              | `:samoa:`                          | [TOC](#table-of-contents) |
| [TOC](#flags) |                :kosovo:                | `:kosovo:`                               |             :yemen:              | `:yemen:`                          | [TOC](#table-of-contents) |
| [TOC](#flags) |               :mayotte:                | `:mayotte:`                              |          :south_africa:          | `:south_africa:`                   | [TOC](#table-of-contents) |
| [TOC](#flags) |                :zambia:                | `:zambia:`                               |            :zimbabwe:            | `:zimbabwe:`                       | [TOC](#table-of-contents) |

#### Subdivision Flag

|               |    ico    | shortcode   |    ico     | shortcode    |                           |
| ------------- | :-------: | ----------- | :--------: | ------------ | ------------------------- |
| [TOC](#flags) | :england: | `:england:` | :scotland: | `:scotland:` | [TOC](#table-of-contents) |
| [TOC](#flags) |  :wales:  | `:wales:`   |            |              | [TOC](#table-of-contents) |
