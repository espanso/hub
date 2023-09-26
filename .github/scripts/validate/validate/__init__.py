from collections import namedtuple
import os
from typing import List
from .rules.missing_mandatory_files import MissingMandatoryFiles
from .rules.invalid_version_path import InvalidVersionPath
from .rules.invalid_package_name import InvalidPackageName
from .rules.incoherent_path import IncoherentPath 
from .rules.missing_manifest_fields import MissingManifestFields 
from .rules.invalid_yaml import InvalidYAML
from .rules.no_yaml_extension import NoYAMLExtension

RULES = [
    MissingMandatoryFiles(),
    InvalidVersionPath(),
    InvalidPackageName(),
    IncoherentPath(),
    MissingManifestFields(),
    InvalidYAML(),
    NoYAMLExtension(),
]

ValidationError = namedtuple('ValidationError', 'name error')

def validate_package(path: str) -> List[ValidationError]:
    if not os.path.isdir(path):
        raise Exception(f"the given path is not a directory: {path}")

    errors = []

    for rule in RULES:
        try:
            rule.validate(path)
        except Exception as e:
            errors.append(ValidationError(rule.name(), e))
          
    return errors
