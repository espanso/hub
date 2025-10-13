import glob
import os
import re

from . import ValidationRule
VERSION_PATTERN = r"^\d+\.\d+\.\d+$"

class InvalidVersionPath(ValidationRule):
    def name(self):
        return "invalid_version_path"

    def validate(self, path: str):
        all_entries: list[str] = glob.glob(os.path.join(path, "*"))

        for entry_path in all_entries:
            entry_name = os.path.basename(entry_path)
            
            # re.fullmatch() ensures the ENTIRE string matches the pattern
            if not re.fullmatch(VERSION_PATTERN, entry_name):
                
                is_dir = "directory" if os.path.isdir(entry_path) else "file"

                # Use the custom exception for better error handling upstream
                raise Exception(
                    f"Unexpected entry: '{entry_name}' (a {is_dir}) was found in '{path}'. "
                    f"This directory must only contain entries matching the version pattern (e.g., 2.1.15)."
                )
        
        return 
