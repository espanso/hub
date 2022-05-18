import os
from . import ValidationRule

class IncoherentPath(ValidationRule):  
  def name(self):
    return "incoherent_path"
  
  def validate(self, path: str):
    package_name = self.get_package_name(path)
    for version_path in self.get_version_paths(path):
      version = os.path.basename(version_path)
      manifest = self.read_manifest(version_path)

      manifest_name = manifest["name"]
      manifest_version = manifest["version"]

      if manifest_name != package_name:
        raise Exception(f"package name mismatch in package {package_name}: the path indicates that the name is {package_name}, but the manifest calls it {manifest_name}")

      if manifest_version != version:
        raise Exception(f"package version mismatch in package {package_name}: the path indicates that the version is {version}, but the manifest indicates version {manifest_version}")