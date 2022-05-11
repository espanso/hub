import re
from . import ValidationRule

REQUIRED_PROPERTIES = ["name", "title", "description", "version", "author"]

class MissingManifestFields(ValidationRule):  
  def name(self):
    return "missing_manifest_fields"

  def validate(self, path: str):
    for version_path in self.get_version_paths(path):
      manifest = self.read_manifest(version_path)

      for property in REQUIRED_PROPERTIES:
        if not property in manifest:
          raise Exception(f"manifest is missing field: {property} in package: {version_path}. These fields are case-sensitive, so make sure you write them all lowercase.")
