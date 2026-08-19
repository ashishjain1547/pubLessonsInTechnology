# Git + GitHub Notes — Next Page

## Notes

(10) Again, I’ll make commit to check how some new
  [??] to [??] changes to Git history.

    git add .
    git commit -m "updated [??]"

(11) git restore [filename]
     → to discard changes.
     Again: git add, or choose how to [??]

(12) git restore --staged filename
     git restore filename → then change back [??]

(13) git branch
• Instead of doing some work on main branch we can do it on independent branch.

(14) git branch
     → It will show [???]
       [new/available branches]

(15) git switch <branch>

(16) git ls-files
     → files to be tracked by Git.

• If you want to merge the changes you have done in your branch [to the main branch]:

    git switch master

(17) git merge [branch]

     It will make [changes] to
     new branch → [??]

(18) git branch -d [branch]
     (delete branch)

(19) If you have some file on one branch, you pushed to main branch & again if you try to push the same file from another branch into main branch, then that is
     [merge conflict].


## Main Commands Visible on This Page

git add .
git commit -m "..."

git restore <filename>
git restore --staged <filename>

git branch
git switch <branch>
git ls-files

git merge <branch>
git branch -d <branch>

## Branching Workflow

main branch
    |
    +---- new branch
             |
        make changes
             |
        commit changes
             |
       merge into main
             |
          main branch

## Key Concept

**merge conflict**: when changes from different branches affect the same file or the same part of a file, Git may require the conflicts to be resolved before the branches can be merged.
