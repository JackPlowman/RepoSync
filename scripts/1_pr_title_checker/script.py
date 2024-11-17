# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from pathlib import Path

def check_file_exists(file_path: str) -> bool:
    try:
        file = Path(file_path)
        return file.exists()
    except Exception:
        return False


def update_pr_title_checker(file_path: str) -> bool:
    try:
        # Open the file in write mode
        with open(file_path, "r") as file:
            # Read the content of the file
            content = file.read()

        # Transform the content
        transformed_content = transform_file(content)
    
        with open(file_path, "w") as file:
            # Save the transformed content back to the file
            file.write(transformed_content)
            return True
    except Exception:
        return False


def transform_file(content: str) -> str:
    content = content.replace("check-pr-title", "check-pull-request-title")
    content = content.replace("Check PR title", "Check Pull Request title")
    content = content.replace(
        '"feat: ,fix: ,bug: ,ci: ,refactor: ,docs: ,build: ,chore(,deps(,chore: ,feat!: ,fix!: ,refactor!: ,test: "',
        '"feat: ,fix: ,bug: ,ci: ,refactor: ,docs: ,build: ,chore(,deps(,chore: ,feat!: ,fix!: ,refactor!: ,test: ,build(deps): "',
    )
    return content


files_paths_to_update = [
    ".github/workflows/pull-request-tasks.yml",
    ".github/workflows/pull-request-checks.yml",
    ".github/workflows/pull-request-check.yml",
]
file_to_update = [file for file in files_paths_to_update if check_file_exists(file)][0]
update_pr_title_checker(file_to_update)
