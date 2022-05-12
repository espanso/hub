import unittest
from validate import validate_package
import os

TEST_PACKAGES_DIR = os.path.join(os.path.dirname(__file__), "test_packages")

VALID_PACKAGES = ["valid-package", "valid-package2"]

class TestValidation(unittest.TestCase):
  def test_valid_packages(self):
    for package in VALID_PACKAGES:
      self.assertEqual(len(validate_package(os.path.join(TEST_PACKAGES_DIR, package))), 0)

  def assertValidationError(self, errors, name: str):
    error_names = []
    for error in errors:
      if error.name == name:
        return
      error_names.append(error.name)
    self.assertTrue(False, f"expected validation error: {name}, but it's not included in errors: {error_names}") 

  def test_missing_files(self):
    errors = validate_package(os.path.join(TEST_PACKAGES_DIR, "missing-files"))
    self.assertValidationError(errors, "missing_mandatory_files")

  def test_missing_version_path(self):
    errors = validate_package(os.path.join(TEST_PACKAGES_DIR, "missing-version-path"))
    self.assertValidationError(errors, "invalid_version_path")

  def test_invalid_extra_file_in_versions(self):
    errors = validate_package(os.path.join(TEST_PACKAGES_DIR, "invalid-extra-file-in-versions"))
    self.assertValidationError(errors, "invalid_version_path")

  def test_invalid_package_name(self):
    errors = validate_package(os.path.join(TEST_PACKAGES_DIR, "invalid_package_name"))
    self.assertValidationError(errors, "invalid_package_name")

  def test_path_coherence_name(self):
    errors = validate_package(os.path.join(TEST_PACKAGES_DIR, "mismatch-package-name"))
    self.assertValidationError(errors, "incoherent_path")

  def test_path_coherence_version(self):
    errors = validate_package(os.path.join(TEST_PACKAGES_DIR, "mismatch-version"))
    self.assertValidationError(errors, "incoherent_path")

  def test_manifest_missing_fields(self):
    errors = validate_package(os.path.join(TEST_PACKAGES_DIR, "manifest-missing-fields"))
    self.assertValidationError(errors, "missing_manifest_fields")

  def test_invalid_yaml_manifest(self):
    errors = validate_package(os.path.join(TEST_PACKAGES_DIR, "invalid-manifest-yaml"))
    self.assertValidationError(errors, "invalid_yaml")

  def test_invalid_yaml_package(self):
    errors = validate_package(os.path.join(TEST_PACKAGES_DIR, "invalid-yaml-files"))
    self.assertValidationError(errors, "invalid_yaml")

  def test_no_yaml_extension(self):
    errors = validate_package(os.path.join(TEST_PACKAGES_DIR, "no-yaml-extension"))
    self.assertValidationError(errors, "no_yaml_extension")

if __name__ == "__main__":
  unittest.main()
