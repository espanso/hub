# 𝑭𝘰𝔫𝘁𝓼 Galore
This package allows you to replace any old text with a fancified version using fonts!

## Installation
Install this package using
```sh
espanso install fonts
```

## Usage
This package replaces text found, up to a final colon, with the same text, but fancified using the specified font.

In order for this font to work, you may need to install Python 3 in order to allow the script to run. You can view a tutorial to do that [here](https://www.reddit.com/r/learnpython/comments/8lkmjf/python_3_installation_guide/).

This package also may not be as useful given the Espanso regex limit, which is set to 30 by default. To change this (**highly recommended**), navigate to the Espanso config file and adjust `max_regex_buffer_size:` to a higher value, I recommend anywhere from 500 - 2000 (*note that this will increase Espanso's memory usage*).

| Shortcut     | Name | Example |
|--------------| - | - |
| :b 𝘵𝘦𝘹𝘵: | Bold | 𝗟𝗼𝗿𝗲𝗺 𝗜𝗽𝘀𝘂𝗺 |
| :i 𝘵𝘦𝘹𝘵: | Italics | 𝘓𝘰𝘳𝘦𝘮 𝘐𝘱𝘴𝘶𝘮 |
| :s 𝘵𝘦𝘹𝘵: | Script | 𝓛𝓸𝓻𝓮𝓶 𝓘𝓹𝓼𝓾𝓶 |
| :g 𝘵𝘦𝘹𝘵: | Gothic | 𝔏𝔬𝔯𝔢𝔪 ℑ𝔭𝔰𝔲𝔪 |
| :f 𝘵𝘦𝘹𝘵: | Fancy | 𝑳𝒐𝒓𝒆𝒎 𝑰𝒑𝒔𝒖𝒎 |
