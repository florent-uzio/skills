---
name: post-merge-cleanup
description: Post-merge cleanup — switch to the default branch, pull, and delete the local branch that was worked on. Use when the user says a PR is merged, "merged", or asks to clean up after a merge.
---

# Post-merge cleanup

Land the repo back on a fresh default branch and delete the merged local branch.

## Steps

1. **Identify the target.** `branch` is the current branch (`git branch --show-current`), or the one the user names. The default branch is `git symbolic-ref --short refs/remotes/origin/HEAD` minus `origin/`. If `branch` is already the default branch, there is nothing to delete: say so and stop. Done when both names are known.

2. **Check the tree is clean.** `git status --porcelain` is empty. Uncommitted work: report it and stop, leaving the branch untouched.

3. **Switch and pull.** `git checkout <default>` then `git pull`. Done when the pull succeeds and the default branch matches `origin`.

4. **Delete the branch.** `git branch -d <branch>`. A squash or rebase merge leaves the branch looking unmerged, so on refusal confirm the merge with `gh pr list --head <branch> --state merged`: a hit → `git branch -D <branch>`; no hit → report and keep the branch.

5. **Report** the default branch's new HEAD (`git log -1 --oneline`) and the deleted branch name.

The remote branch is left to the merge's auto-delete.
