# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

def update_pr_title_checker(file_path: str) -> bool:
    try:
        # Load the file
        with open(file_path, 'r') as file:
            content = file.read()
        # Transform the content
        transformed_content = transform_file(content)
        # Save the transformed content back to the file
        with open(file_path, 'w') as file:
            file.write(transformed_content)
        return True
    except Exception:
        return False

def transform_file(content: str) -> str:
    content_str = str(content)
    content_str = content_str.replace("check-pr-title", "check-pull-request-title")
    content_str = content_str.replace("Check PR title", "Check Pull Request title")
    content_str = content_str.replace(
        "\"feat: ,fix: ,bug: ,ci: ,refactor: ,docs: ,build: ,chore(,deps(,chore: ,feat!: ,fix!: ,refactor!: ,test: \"",
        "\"feat: ,fix: ,bug: ,ci: ,refactor: ,docs: ,build: ,chore(,deps(,chore: ,feat!: ,fix!: ,refactor!: ,test: ,build(deps): \""
    )


files_paths_to_update = [
    ".github/workflows/pull-request-tasks.yml",
    ".github/workflows/pull-request-checks.yml",
]
for file_path in files_paths_to_update:
    if update_pr_title_checker(file_path):
        break
