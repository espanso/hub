import re
from . import ValidationRule

VALIDATE_REGEX = re.compile(r"^[a-z0-9\-]+$")

class InvalidPackageName(ValidationRule):  
  def name(self):
    return "invalid_package_name"

  def validate(self, path: str):
    name = self.get_package_name(path)
    if not VALIDATE_REGEX.match(name):
      raise Exception(f"invalid package name: '{name}'. A package name can only be composed of lowercase letters, numbers and hyphen -")
