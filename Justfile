# ------------------------------------------------------------------------------
# General commands
# ------------------------------------------------------------------------------

# Remove all generated files
clean:
    find . -type d -name "work" -exec rm -rf {} \; 2>/dev/null || true
    git clean -Xdf


# ------------------------------------------------------------------------------
# Prettier
# ------------------------------------------------------------------------------

prettier-check:
    prettier . --check

prettier-format:
    prettier . --check --write

# ------------------------------------------------------------------------------
# Justfile
# ------------------------------------------------------------------------------

format:
    just --fmt --unstable

format-check:
    just --fmt --check --unstable

# ------------------------------------------------------------------------------
# gitleaks
# ------------------------------------------------------------------------------

gitleaks-detect:
    gitleaks detect --source . > /dev/null

# ------------------------------------------------------------------------------
# Git Hooks
# ------------------------------------------------------------------------------

# Install pre commit hook to run on all commits
install-git-hooks:
    cp -f githooks/pre-commit .git/hooks/pre-commit
    cp -f githooks/post-commit .git/hooks/post-commit
    chmod ug+x .git/hooks/*
