# Espanso GIT

Improve your git experience using this snippets triggers, become a faster developer at cli.

## Triggers

### Configurations

Trigger  | Command
---------|----------
giti. | `git init`
gitcl. | `git clone`
gitconfigline1. | `git config --global core.autocrlf true`
gitconfigline2. | `git config --global core.safecrlf warn`
gitemailg. | `git config --global user.email ""`
gitemaill. | `git config --local user.email ""`
gituserg. | `git config --global user.name ""`
gituserl. | `git config --local user.name ""`

<br>

### Push | Pull 

Trigger  | Command
---------|----------
gits. | `git status`
gita. | `git add .`
gitc. | `git commit -m ""`
gitamc. | `git commit --amend -m ""`
gitama. | `git commit --amend --author="User Name <email@email.com>"`
gitp. | `git push origin`
gitpf. | `git push origin --force `
gitu. | `git pull origin`
gitru. | `git remote update`
gitfa. | `git fetch --all`

<br>

### Stash

Trigger  | Command
---------|----------
gitst. | `git stash`
gitstl. | `git stash list`
gitsts. | `git stash show`
gitstp. | `git stash pop`
gitstd. | `git stash drop`

<br>

### Branch

Trigger  | Command
---------|----------
gitm. | `git merge`
gitmb. | `git merge`
gitchk. | `git checkout`
gitchkb. | `git checkout -b` 
gitnb. | `git checkout -b` 
gitb. | `git branch`
gitba. | `git branch -a`
gitbd. | `git branch -d `
gitbdr. | `git push origin --delete` 

<br>

### Log

Trigger  | Command
---------|----------
gitl. | `git log`
gitlp. | `git log --pretty=oneline`
gitlo. | `git log --oneline`
gitlgo. | `git log --graph --oneline`
gitlpf. | `git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short`

<br>

### Revert | Rebase | Reset

Trigger  | Command
---------|----------
gitrb. | `git rebase master`
gitrs. | `git reset`
gitrsh. | `git reset --hard`
gitrv. | `git revert HEAD`
gitrvne. | `git revert HEAD --no-edit`

<br>

### Tags

Trigger  | Command
---------|----------
gittg. | `git tag`
gittgd. | `git tag -d`
gitmv. | `git mv file.ext dir_name`
