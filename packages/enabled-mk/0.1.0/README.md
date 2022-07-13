### `enabled-mk`, an espanso plugin

If Espanso has become as ingrained in your every day life as it has for mine, then `enabled-mk` is for you.
Simply type `:mk` or `;mk` to trigger the associated form menu.

Under the hood, a Python one-liner takes Stdin arguments and uses them to interact with the espanso config files. Namely, it does this to deserialize, update, then re-serialize the data back into `espanso/match/base.yml`.

Additionally, this plugin supports Vim users who accidentally encounter <kbd>:</kbd>-prefixed patterns and want a suitable
alternative. To other authors -- please consider enabling <kbd>(;|:)</kbd> regex syntax instead of a static <kbd>:</kbd>
option, since it enables a magical compatibility between the command mode and espanso.

```sh
- regex: (;|:)mk
  replace: '{{empty}}'
  vars:
  - name: nix
    type: form
    params:
      layout: New keybinding [[key]] -> [[value]]
  - name: empty
    type: shell
    params:
      cmd: 'KEY=''{{nix.key}}'' VALUE=''{{nix.value}}'' python3 -c ''import os; import
        yaml; HOME=os.environ.get("HOME"); FOUT=f"{HOME}/.config/espanso/match/base.yml";
        FIN=FOUT; KEY,VALUE=(os.environ.get("KEY"),os.environ.get("VALUE")); assert
        KEY and VALUE, "Both KEY and VALUE must be supplied from stdin"; handle=open(FIN,
        "r+"); raw=handle.read(); handle.close(); espanso=yaml.load(raw, Loader=yaml.loader.SafeLoader);
        espanso["matches"].append({"trigger": KEY, "replace": VALUE}) ; handle=open(FOUT,
        "w+"); yaml.dump(espanso, stream=handle, sort_keys=False) ; handle.close();'';
        printf '''''
```

### Installation

Install [espanso](https://espanso.org/install/), then run

```
espanso install enabled-mk
```

### Example

(See above) 

