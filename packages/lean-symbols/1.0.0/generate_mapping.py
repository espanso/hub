import json
import yaml
from pathlib import Path

# Orignial mapping can be found here https://raw.githubusercontent.com/leanprover/vscode-lean4/c7efb256743d3a5e35ffda21f09f6c32900ba69c/vscode-lean4/src/abbreviation/abbreviations.json

custom_non_overriding_mapping = Path("custom_non_overriding_map.yml")
lean_mapping_file = Path("abbreviations.json")
output_file = Path('package.yml')


def append_mapping(espanso_mapping : dict, new : dict):
    for key, value in new.items():
        espanso_mapping["matches"].append(
            {
                "triggers": [f"\\{key}\\", f"\\{key}\t"],
                "replace": value
            }
        )
        espanso_mapping["matches"].append(
            {
                "triggers": [f"\\{key} "],
                "replace": value + " "
            }
        )


def json_to_espanso(json_file):
    espanso_mapping = {"matches": []}

    with json_file.open('r') as f:
        mapping = json.load(f)

    append_mapping(espanso_mapping, mapping)

    return espanso_mapping


def inject_custom_non_overwriding_mapping(mapping):
    mapping_to_inject = yaml.load(custom_non_overriding_mapping.open('r'), yaml.SafeLoader)
    for k, v in mapping_to_inject.items():
        if k in mapping:
            raise Exception(f"The mappingping `{k}: {v}` would overwrite the default lean mapping of `{k}: {map[k]}`. Aborting")
        append_mapping(mapping, {k: v})


# Example usage:
def main():
    mapping = json_to_espanso(lean_mapping_file)

    inject_custom_non_overwriding_mapping(mapping)

    with output_file.open('w', encoding='utf-8') as out_file:
        yaml.dump(mapping, out_file, sort_keys=False, allow_unicode=True)


if __name__ == "__main__":
    main()
