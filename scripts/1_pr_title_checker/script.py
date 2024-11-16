# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ruamel-yaml==0.18.6",
# ]
# ///

import sys
from ruamel.yaml import YAML
import os

def update_pr_title_checker(file_path: str) -> bool:
    try:
        # Load the file
        yaml = YAML(typ='safe', pure=True)
        with open(file_path, 'r') as file:
            content = yaml.load(file)
        
        # Transform the content
        transformed_content = transform_yaml(content)
        
        # Save the transformed content back to the file
        with open(file_path, 'w') as file:
            yaml.dump(transformed_content, file)
        
        print(f"File {file_path} updated successfully")
        return True
    except Exception as e:
        print(f"Error updating the file {file_path}: {e}")
        return False

def transform_yaml(content: dict) -> dict:
    # Transform the yaml content
    content_str = str(content)
    content_str = content_str.replace("check-pr-title", "check-pull-request-title")
    content_str = content_str.replace("Check PR title", "Check Pull Request title")
    content_str = content_str.replace(
        "\"feat: ,fix: ,bug: ,ci: ,refactor: ,docs: ,build: ,chore(,deps(,chore: ,feat!: ,fix!: ,refactor!: ,test: \"",
        "\"feat: ,fix: ,bug: ,ci: ,refactor: ,docs: ,build: ,chore(,deps(,chore: ,feat!: ,fix!: ,refactor!: ,test: ,build(deps): \""
    )
    return eval(content_str)

files_paths_to_update = [
    ".github/workflows/pull-request-tasks.yml",
    ".github/workflows/pull-request-checks.yml",
]
print(f"CWD: {os.getcwd()}")
for file_path in files_paths_to_update:
    if update_pr_title_checker(file_path):
        break
