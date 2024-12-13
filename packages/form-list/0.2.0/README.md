# Form list
## A package for getting a list of expansions from one form via a CSV list.

# Setup
The `package.yml` does not need to be edited.

You will need to edit the entries in the `form_urls.csv`. The sample lines are a good starting point. The basic syntax is:

| Name/description (without quotes) | URL |
| --- | --- |
| gmail | https://gmail.com/ |

**Separate the two fields with a comma.** Remember to save the file! Ensure you retain its UTF-8 encoding - spreadsheet programs may switch to UTF-8-BOM.

## Reuse

You can of course also copy the contents of this package and create multiple form lists with other text. 👍 If you do so, you will need to edit the global variable for the location of the csv file.

Requires Python, but if present should work in all operating systems.