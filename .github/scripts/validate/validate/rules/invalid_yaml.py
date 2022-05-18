import glob 
import os
import yaml
from . import ValidationRule

class InvalidYAML(ValidationRule):  
  def name(self):
    return "invalid_yaml"
  
  def validate(self, path: str):
    for version_path in self.get_version_paths(path):
      for yaml_path in glob.glob(os.path.join(version_path, "*.yml")):
        try:
          with open(yaml_path, encoding="utf-8") as f:
            yaml.safe_load(f)
        except Exception as e:
          raise Exception(f"invalid YAML detected in file: {yaml_path}, please make sure the file is formatted correctly. If you're unsure of the error, you can use http://www.yamllint.com/ to validate it.\nError: {e}")