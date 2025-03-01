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
    content = (
        content
        + """
  run-code-limit:
      name: Code Limit Analysis
      runs-on: ubuntu-latest
      permissions:
        statuses: write
      steps:
        - name: Checkout
          uses: actions/checkout@v4.2.2
          with:
            fetch-depth: 0
        - name: "Run Code Limit"
          uses: getcodelimit/codelimit-action@8ee70f8d3d5b984130e46fb8ccbe229f5e1d68d0
          with:
            token: ${{ secrets.GITHUB_TOKEN }}
            upload: true
"""
    )
    return content


files_paths_to_update = [".github/workflows/code-checks.yml"]
file_to_update = [file for file in files_paths_to_update if check_file_exists(file)][0]
update_pr_title_checker(file_to_update)
