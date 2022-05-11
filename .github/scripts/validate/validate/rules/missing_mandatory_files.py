import os
from . import ValidationRule

REQUIRED_FILES = ["package.yml", "README.md", "_manifest.yml"]

class MissingMandatoryFiles(ValidationRule):  
  def name(self):
    return "missing_mandatory_files"
  
  def validate(self, path: str):
    for version_path in self.get_version_paths(path):
      for required in REQUIRED_FILES:
        target_file = os.path.join(version_path, required)
        if not os.path.isfile(target_file):
          raise Exception(f"expected file '{required}' to be present inside package: {self.get_package_name(path)}, but found none. File should be present in path: {target_file}")