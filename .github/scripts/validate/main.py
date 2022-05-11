import glob
import os
import sys
from validate import validate_package

report_errors = []

for package in glob.glob("packages/*"):
  package_name = os.path.basename(package)

  print(f"Validating package: {package_name}... ", end='', flush=True)

  errors = validate_package(package)
  if len(errors) == 0:
    print("OK")
    continue

  print(f"Found {len(errors)} errors:")

  for error in errors:
    print(f"Check: {error.name}")
    print(f" ->: {error.error}")
  
  report_errors.append({
    "package": package_name,
    "errors": errors,
  })

print("Generating CI report...")

with open("validation_report.md", "w", encoding="utf-8") as f:
  f.write("## CI Quality Check 🤖🚨 \n\n")

  if len(report_errors) == 0:
    f.write("All checks passed ✅ Great job!\n\n")
    f.write("![Great Job](https://raw.githubusercontent.com/espanso/hub/main/.github/scripts/validate/great-job-image.jpg)")
  else:
    f.write("Oh snap! Our robots detected some errors 🤖 We need to solve them before merging the package:\n\n")
    for package in report_errors:
      package_name = package["package"]
      package_errors = package["errors"]
      f.write(f"### Package: {package_name}\n\n")
      for error in package_errors:
        error_name = error.name
        error_message = error.error
        f.write(f"#### Check: **{error_name}** ❌\n\n")
        f.write(f"```\n{error_message}\n```\n\n")
    f.write("After you fixed the problems, please create another commit and push it to re-run the checks 🚀")

if len(report_errors) == 0:
  print("All ok!")
else:
  print("Errors detected, please see attached report.")
  sys.exit(1) 