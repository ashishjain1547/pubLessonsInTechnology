# Git + GitHub Notes

### Git
- Distributed version control system.
- Works offline as well.

### Version Control Systems

**Centralized**
- All data is in one server.

**Distributed**
- Every developer has a copy.
- Changes can be made in the local repository and then pushed/shared.
- GitHub is an online platform where repositories are hosted.

### Steps — Install Git

1. Go to the folder location you want to track.
2. Open CMD:
   ```bash
   git --version
   ```
3. Check Git status:
   ```bash
   git status
   ```
4. Configure username:
   ```bash
   git config --global user.name "mayank"
   ```
5. Configure email:
   ```bash
   git config --global user.email "mayank.com"
   ```
   *(The exact email address is unclear in the handwriting.)*

### Git Workflow

**Working Directory → Staging Area → Local Repository → Remote Repository**

- Add:
  ```bash
  git add <file>
  ```

- Commit:
  ```bash
  git commit -m "..."
  ```

6. Example:
   ```bash
   git add index.css
   ```

7. Commit:
   ```bash
   git commit -m "my first website ready"
   ```

8. View commit history:
   ```bash
   git log
   ```
   or
   ```bash
   git log --oneline
   ```

9. `.gitignore`
   - Used to tell Git which files/folders should not be tracked.
   - Example: ignore files/folders that should not be pushed to the repository.
   - *(The exact example in the note is unclear.)*

10. Git does **not track empty folders**.
   - To keep an otherwise empty folder in Git, create a placeholder such as:
   ```text
   .gitkeep
   ```
   - Then Git will track the folder through that file.

### GitHub

- GitHub is an online platform where repositories are hosted.
- A developer can push a local repository to GitHub.
- GitHub allows repositories/code to be shared and collaborated on.

### Important Flow

```text
Working Directory
       ↓
   git add
       ↓
Staging Area
       ↓
 git commit
       ↓
Local Repository
       ↓
   git push
       ↓
Remote Repository / GitHub
```

A couple of lines in the upper-right and the exact `user.email` value are too unclear to transcribe reliably from the image.
