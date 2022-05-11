import glob 
import os
import yaml
from . import ValidationRule

class NoYAMLExtension(ValidationRule):  
  def name(self):
    return "no_yaml_extension"
  
  def validate(self, path: str):
    for version_path in self.get_version_paths(path):
      for yaml_path in glob.glob(os.path.join(version_path, "*.yaml")):
        raise Exception(f"Please use '.yml' as extension for your files and not .yaml")