# Emoji Picker

This is a package created for [Espanso](https://espanso.org/) called `emoji-picker` that provides a picker to select an emoji based on your input.

This is heavily inspired by the work done in [jobiewong/espanso-emojis](https://github.com/jobiewong/espanso-emojis) and was started by a fork, but heavily modified to use search capabilities instead.

The method behind the package is very simple: Emoji unicode values and names are fetched from https://github.com/muan/unicode-emoji-json. They're then formatted and exported as a yml file for use by Espanso.

This project uses the search keywords provided by [muan/emojilib: Emoji keyword library.](https://github.com/muan/emojilib)

## Why?

_Why use this instead of your OS's or application's built-in emoji picker?_  
1. **Consistency across devices.** Use multiple computers? Multiple operating systems? Multiple applications? This works the same way across _all_ devices and applications. Not all devices _have_ a built-in emoji picker.
2. **Customization.** See notes in the `Customization` section below. You can change the trigger or shortcuts to your liking!
3. **Modernity.** This project was inspired by some operating systems having outdated lists of emojis. _(Looking at you, Windows 10.)_

_Why use this over other Espanso emoji packages?_  
The other Espanso emoji packages just dump 1,000+ emojis in your Espanso folder, thus clogging up your search results if you ever use the Espanso search to find expansion options. This clogs your search results with emojis, which makes finding *non*-emojis harder. With this package you can use Espanso's built-in picker to choose the emoji that most closely matches what you search for, without clogging search results!

## Usage:

1. Install the package.
2. In any text field on your computer, type the trigger to open the search bar. For a fresh installation, this defaults to `:em`.
3. Type your search query and select your desired result to insert it into your writing.

## Customization:

Being a simple text file on your PC, you are able to tweak the suggestions however you choose. Just know that any of the following suggestions may be overwritten if you update the extension! So maybe make a copy of the `package.yml` file and make your changes there instead.

To make changes to the default settings,

1. Open up the Espanso config folder. (On Windows this is located in `%appdata%` by default)
2. Navigate to `match` --> `packages` --> `emoji-picker` and open `package.yml`.

### Changing the default trigger:

By default, the trigger is set to `:em`. You could change this to any value you'd like.

To change the trigger:

1. Open the `package.yml` file.
2. Change the value in the `triggers` array, or add more.

You could even change the trigger to a key-combo! See the [Espanso docs](https://espanso.org/docs/matches/basics/#keyboard-triggers) for more details.

**Note:** If you want to emulate standard "colon-emoji" support, similar to the syntax of Discord, Slack, Google Chat, Git, (etc), then you can change the trigger to `" :"` and change the value of `replace` to `" {{output}}"`.
This means that _every_ time you type a colon after a space the picker will appear. If you do that, you may want to disable this package for certain applications that natively support colon-emojis, like Discord, Slack, etc. See the [Espanso docs](https://espanso.org/docs/configuration/include-and-exclude/) for more details.

### Customizing the shortcuts:

* Do you _never_ use certain emojis?
* Do you dislike certain triggers for being too similar to others?
* Do you want to add custom triggers for different emojis?

**You can!**

1. Open the `package.yml` file in the editor of your choice. Notepad works just fine.
2. Add, delete, or edit any of the label/id pairs you see. The `label` is what shows when you are using the picker, and the `id` is the emoji that gets inserted by the `label` on the preceding line.

## Known Issues:

### Why do the emojis look weird on Windows?
On Windows 10/11 devices, the emojis render in the dropdown like this:
![Emoji Picker Screenshot running Windows 10](/images/screenshot_windows_10.png)

Obviously this is not ideal. This is a Windows-specific issue that likely can be fixed in the Espanso program itself. See this open issue for more details: [emoji representation in search bar · Issue #1972 · espanso/espanso](https://github.com/espanso/espanso/issues/1972)

### If I type an exact match for an emoji, why do I have to dig for it?
For example, if you type `car` in the search bar you'll get hundreds of matching emojis. You'd think that 🚗 would be close to the top, right?  
This is apparently a quirk of how Espanso renders options when showing search results. This is likely something that could be fixed within Espanso itself.

As a workaround, you can type `:car` or `:car:` into the search dropdown to get exact matches.
