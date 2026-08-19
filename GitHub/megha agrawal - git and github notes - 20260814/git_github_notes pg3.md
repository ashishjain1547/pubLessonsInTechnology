# Git + GitHub Notes — Next Page

## Resolve Merge Conflict (Manually)

- Just open the file.
- Keep or delete the unwanted/conflicting changes.
- Save the file.
- Then run:

```bash
git add .
git commit -m "..."
```

## Git Stashing

**Stashing:** If you have made some changes but you need to do some emergency/other work, you can temporarily save your current changes using `git stash`.

```bash
git stash
git stash list
git status
```

- `git stash` — temporarily saves your current changes.
- `git stash list` — shows the saved stashes.
- `git status` — should show a clean working tree after stashing.
- When you want the changes back:

```bash
git stash pop
```

- `git stash pop` — brings back the stashed changes.

## Best Practices

1. Create an isolated branch for each feature.
2. Never develop directly on the `main` branch.
3. Delete merged branches.
4. Use meaningful branch names.
5. Keep branches short-lived and merge them as soon as possible.

## Git Tags

Git tags can be used to mark specific points/versions in the repository.

### Types of Tags

1. **Annotated tag**
   - Contains additional information/metadata.
   - Example:

```bash
git tag -a v1.0 -m "my release"
```

2. **Lightweight tag**
   - A simple tag pointing to a specific commit.
   - Example:

```bash
git tag v1.1
```

### Other Tag Command

```bash
git tag
```

- Lists the tags in the repository.

## Git Rebase

```bash
git rebase master
```

- Rebase can be used to replay the changes from one branch on top of another branch.
- This can help avoid unnecessary merge commits.
