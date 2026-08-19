# Git + GitHub Notes — Next Page

## Connect Local Repository to GitHub

### Clone / SSH Notes

```bash
git clone <repo-url>
```

- Clone the repository from GitHub to the local computer.
- SSH key can be used for authentication.

### SSH Key

- Generate an SSH key.
- Copy the public key (`.pub`).
- Add the SSH key to GitHub.

The notes appear to refer to adding the SSH key under GitHub account settings.

## Initial Local Repository Setup

```bash
touch index.md
git add .
git commit -m "..."
git push origin main
```

- The `git add` + `git commit` + `git push` sequence is used to commit local changes and push them to GitHub.

## Configure Git

```bash
git remote -v
git config --global init.defaultBranch main
git branch -M main
```

- `git remote -v` — check the remote repository URL.
- `git config --global init.defaultBranch main` — set the default initial branch name to `main`.
- `git branch -M main` — rename the current branch to `main`.

## Steps to Push Local Repo to a Remote GitHub Repo

1. Create a repository on GitHub.
2. Copy the repository URL.
3. Add the GitHub repository as the remote:

```bash
git remote add origin <URL>
```

4. Check the remote:

```bash
git remote -v
```

5. Change/rename the branch to `main` if required:

```bash
git branch -M main
```

6. Push the local `main` branch to GitHub:

```bash
git push -u origin main
```

7. Pull changes from the remote repository:

```bash
git pull
```

- `git pull` will bring the changes made by others into the local repository.

## GitHub Desktop

- Download GitHub Desktop.
- Create repository.
- Open with VS Code.
- Click the **+** button to stage changes.
- Publish repository.
- Pull requests.
- Create pull request.
- Merge someone else's branch into your branch.

> The handwritten note also mentions that publishing may require connecting/authenticating with GitHub.

## Fork

### What is a Fork?

A **fork** means creating a copy of another person's repository in your own GitHub account so that you can make changes without directly affecting the original repository.

```text
Original Repository
        |
        ↓
      Fork
        |
        ↓
Your own copy
        |
        ↓
Make changes
        |
        ↓
Create Pull Request
```

- A fork is useful when you do not have direct write access to the original repository.
- You can make changes in your fork and then create a pull request to contribute those changes back to the original repository.

> Some words and command details in the handwritten SSH section are unclear, so they have been represented generically rather than guessed.
