# Timezone Date

A single trigger that uses two Python scripts to offer a choice from the full set of worldwide timezones, returning the current date and time there.

(Espanso's inbuilt `date` extension is handy, but very limited, especially because it can't accept a `{{variable}}` for its `offset:` value. I'll publish another small package `date-offset` to illustrate other ways in which this can be done.)

Two versions of the match file are included:

1. `package.yml` uses the `pytz` library and should work with any version of Python
2. `_package.yml` uses `zoneinfo`, which is part of modern editions (v3.9+) of Python, and should be a few milliseconds faster

To try the latter, rename the first file to anything you like, with an underscore `_` as its first character so that Espanso ignores it, then *remove* the underscore prefixing the second file's name.

In the middle of each file is a `default:` line, currently:

```yml
              default: Europe/London
```

Once you've tried the trigger, change this timezone value to take you quickly to a part of the list that suits you most - it's a long list!

There is scope to modify the code to:

- in the last line, change the text, and date format output
- hard-code a timezone into the third variable (if you only need one, for example),  dispensing with the first two variables providing the choice
- include some sort of time offset (do so in the final section but *prior* to the conversion of UTC time to the specified timezone) - see also the `date-offset` package

Stephen Meech
(@smeech)
