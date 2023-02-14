# Espanso GIT

Improve your git experience using this snippets triggers.
A package of the most common and important Git commands.
Become faster with the Git CLI.

## Triggers

### Configurations

| Trigger         | Command                                  |
| --------------- | ---------------------------------------- |
| giti.           | `git init`                               |
| gitcl.          | `git clone`                              |
| gitconfigline1. | `git config --global core.autocrlf true` |
| gitconfigline2. | `git config --global core.safecrlf warn` |
| gitemailg.      | `git config --global user.email ""`      |
| gitemaill.      | `git config --local user.email ""`       |
| gituserg.       | `git config --global user.name ""`       |
| gituserl.       | `git config --local user.name ""`        |

<br>

### Commits

| Trigger | Command                                                     |
| ------- | ----------------------------------------------------------- |
| gits.   | `git status`                                                |
| gita.   | `git add .`                                                 |
| gitc.   | `git commit -m ""`                                          |
| gitamc. | `git commit --amend -m ""`                                  |
| gitcam. | `git commit --amend -m ""`                                  |
| gitama. | `git commit --amend --author="User Name <email@email.com>"` |
| gitamd. | `git commit --amend --date="2023-02-14T15:55:00"`           |
| gitru.  | `git remote update`                                         |
| gitfa.  | `git fetch --all`                                           |

<br>

### Push

| Trigger | Command                        |
| ------- | ------------------------------ |
| gitpf.  | `git push origin --force `     |
| gitp.   | `git push origin`              |
| gitpd.  | `git push origin develop`      |
| gitpd1. | `git push origin dev`          |
| gitpd2. | `git push origin develop`      |
| gitpd3. | `git push origin development`  |
| gitph.  | `git push origin homolog`      |
| gitph1. | `git push origin hml`          |
| gitph2. | `git push origin homolog`      |
| gitph3. | `git push origin homologation` |

<br>

### Pull

| Trigger | Command                        |
| ------- | ------------------------------ |
| gitu.   | `git pull origin `             |
| gitud.  | `git pull origin develop`      |
| gitud1. | `git pull origin dev`          |
| gitud2. | `git pull origin develop`      |
| gitud3. | `git pull origin development`  |
| gituh.  | `git pull origin homolog`      |
| gituh1. | `git pull origin hml`          |
| gituh2. | `git pull origin homolog`      |
| gituh3. | `git pull origin homologation` |

<br>

### Stash

| Trigger  | Command                         |
| -------- | ------------------------------- |
| gitst.   | `git stash`                     |
| gitstl.  | `git stash list`                |
| gitsts.  | `git stash show`                |
| gitstp.  | `git stash pop`                 |
| gitstd.  | `git stash drop`                |
| gitstiu. | `git stash --include-untracked` |

<br>

### Branch

| Trigger   | Command                     |
| --------- | --------------------------- |
| gitm.     | `git merge`                 |
| gitbm.    | `git branch -m main`        |
| gitmb.    | `git merge`                 |
| gitmd.    | `git merge develop`         |
| gitmd1.   | `git merge dev`             |
| gitmd2.   | `git merge develop`         |
| gitmd3.   | `git merge development`     |
| gitmh.    | `git merge homolog`         |
| gitmh1.   | `git merge hml`             |
| gitmh2.   | `git merge homolog`         |
| gitmh3.   | `git merge homologation`    |
| gitchk.   | `git checkout`              |
| gitchkd.  | `git checkout develop`      |
| gitchkd1. | `git checkout dev`          |
| gitchkd2. | `git checkout develop`      |
| gitchkd3. | `git checkout development`  |
| gitchkh.  | `git checkout homolog`      |
| gitchkh1. | `git checkout hml`          |
| gitchkh2. | `git checkout homolog`      |
| gitchkh3. | `git checkout homologation` |
| gitchkb.  | `git checkout -b`           |
| gitnb.    | `git checkout -b`           |
| gitb.     | `git branch`                |
| gitba.    | `git branch -a`             |
| gitbd.    | `git branch -d `            |
| gitbdf.   | `git branch -D `            |
| gitbdr.   | `git push origin --delete`  |

<br>

### Log

| Trigger | Command                                                             |
| ------- | ------------------------------------------------------------------- |
| gitl.   | `git log`                                                           |
| gitlp.  | `git log --pretty=oneline`                                          |
| gitlo.  | `git log --oneline`                                                 |
| gitlgo. | `git log --graph --oneline`                                         |
| gitlpf. | `git log --pretty=format:"%h %ad  %s%d [%an]" --graph --date=short` |

<br>

### Revert | Rebase | Reset

| Trigger   | Command                     |
| --------- | --------------------------- |
| gitrb.    | `git rebase master`         |
| gitrs.    | `git reset`                 |
| gitrsh.   | `git reset --hard`          |
| gitrshh.  | `git reset --hard HEAD`     |
| gitrshh1. | `git reset --hard HEAD~1`   |
| gitrss.   | `git reset --soft `         |
| gitrssh.  | `git reset --soft HEAD`     |
| gitrssh1. | `git reset --soft HEAD~1`   |
| gitrv.    | `git revert HEAD`           |
| gitrvne.  | `git revert HEAD --no-edit` |

<br>

### Tags

| Trigger | Command      |
| ------- | ------------ |
| gittg.  | `git tag`    |
| gittgd. | `git tag -d` |

### Tags

| Trigger  | Command         |
| -------- | --------------- |
| gitrt.   | `git restore .` |
| gitcln.  | `git clean`     |
| gitclnf. | `git clean -f`  |

### Others

| Trigger | Command                    |
| ------- | -------------------------- |
| gitmv.  | `git mv file.ext dir_name` |
| gitcyp. | `git cherry-pick `         |
