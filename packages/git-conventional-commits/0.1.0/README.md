# Espanso Snippets for Conventional Commits in Git

## How it works:

You can specify the commit message as follows:

```
:{{type}}{{scope}}#{{closed_issue_number}}
```

The scope and closed_issue_number are optional.
You can also append `!` at the end to make it a breaking change commit or ``!!`` to add a BREAKING CHANGE footer.

Supported types are: ``feat``,`` fix``,`` build``,`` chore``,`` ci``,`` docs``,`` style``,`` refactor``,`` perf``,`` test``,`` and revert``