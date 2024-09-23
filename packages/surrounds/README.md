# Surrounds for text strings

# An Espanso file to quickly surround text in various punctuation.
### Important note on trigger syntax:
This package uses a leading semicolon `;` instead of Espanso's more standard `:`(colon). I find that this is slightly faster to type, but if you would like to change it, feel free to do so.

## :Usage examples:

Say you have a long string of text that you want to search in google using quotes.
1. copy the text
2. click on the google search bar so your cursor is blinking there. 
3. use the trigger combination `;p"` and the text string will be placed with quotation marks around it.

This can also be useful for surrounding text with matching brackets, braces, etc.

For most surrounds, you simply choose the character you want to surround the text witth. 

For characters with a different closing character (like `{}` or `[]`), only the open character will trigger the surround.

> For example `;p(` will surround the text with opening and closing parentheses, but `;p)` will not.

You may want to selectively disable this package depending on the apps you use and the contexts in which you type.
