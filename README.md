# Repo Sync

A project to store all scripts used to sync repositories.

## Tools

Tools used to sync repositories:

- [microplane](https://github.com/Clever/microplane)
- [turbolift](https://github.com/Skyscanner/turbolift)

## How to use turbolift

1. `turbolift init --name <name>`
   1. Update repos.txt with the list of repositories to update.
   2. Add pull request title/description to README.md.
2. `turbolift clone`
   1. Update the cloned repositories.
3. `turbolift foreach -- git add -A`
4. `turbolift commit --message "update"`
5. `turbolift create-prs`
6. `turbolift pr-status --list`
