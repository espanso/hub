import json
import yaml
from pathlib import Path
import requests
import io

# Note that this points to a specific commit. To update the mappings point to a newer commit.
lean_mappings_url = "https://raw.githubusercontent.com/leanprover/vscode-lean4/c7efb256743d3a5e35ffda21f09f6c32900ba69c/vscode-lean4/src/abbreviation/abbreviations.json"

custom_non_overriding_mapping = Path("custom_non_overriding_map.yml")
output_file = Path('package.yml')


def make_espanso_mappings(mappings : dict):
    espanso_mapping = {"matches": []}
    for key, value in mappings.items():
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
    return espanso_mapping


def main():
    # Fetch the Lean mappings
    response = requests.get(lean_mappings_url)
    with io.StringIO(response.text) as tmp_lean_mapping_file:
        lean_mappings = json.load(tmp_lean_mapping_file)

    # Add the custom mapppings
    custom_mappings = yaml.load(custom_non_overriding_mapping.open('r'), yaml.SafeLoader)
    for k, v in custom_mappings.items():
        if k in lean_mappings:
            raise Exception(f"The mappingping `{k}: {v}` would overwrite the default lean mapping of `{k}: {lean_mappings[k]}`. Aborting!")
        lean_mappings[k] = v

    # Create the espanso mappings
    espanso_mappings = make_espanso_mappings(lean_mappings)
    with output_file.open('w', encoding='utf-8') as out_file:
        yaml.dump(espanso_mappings, out_file, sort_keys=False, allow_unicode=True)


if __name__ == "__main__":
    main()
