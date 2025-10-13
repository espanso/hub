import glob
import os
from abc import ABC
from abc import abstractmethod
from typing import List

import yaml


class ValidationRule(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def validate(self, path: str):
        pass

    def get_package_name(self, path: str) -> str:
        return os.path.basename(path)

    def get_version_paths(self, path: str) -> List[str]:
        entries = glob.glob(os.path.join(path, "*.*.*"))
        return filter(lambda entry: os.path.isdir(entry), entries)

    def read_manifest(self, version_path: str):
        with open(os.path.join(version_path, "_manifest.yml"), encoding="utf-8") as f:
            return yaml.safe_load(f)
