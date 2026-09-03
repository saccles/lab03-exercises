# Lab 03: Git and GitHub

This repository documents my practice with 
local Git, GitHub, branches, and pull requests.

## README Responses

### 1.1 After initialization

```text
ls -la
total 12
drwxrwxr-x 3 kali kali 4096 Sep  3 10:45 .
drwxrwxr-x 8 kali kali 4096 Sep  3 10:45 ..
drwxrwxr-x 6 kali kali 4096 Sep  3 10:45 .git
```

### 1.2 First git status

git status      
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)

### 1.3 After the first commit

git status   
On branch main
nothing to commit, working tree clean

### 1.4 git log

git log --oneline
84cbf78 (HEAD -> main) Create lab README

### 1.5 git diff

git status       
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

git diff  
diff --git a/README.md b/README.md
index 090962f..30d5415 100644
--- a/README.md
+++ b/README.md
@@ -1,5 +1,8 @@
 # Lab 03: Git and GitHub
 
+This repository documents my practice with 
+local Git, GitHub, branches, and pull requests.
+
 ## README Responses
 
 ### 1.1 After initialization
@@ -27,8 +30,15 @@ nothing added to commit but untracked files present (use "git add" to track)
 
 ### 1.3 After the first commit
 
+git status   
+On branch main
+nothing to commit, working tree clean
+
 ### 1.4 git log
 
+git log --oneline
+84cbf78 (HEAD -> main) Create lab README
+
 ### 1.5 git diff
 
 Paste the `git status` and `git diff` commands and their output.

How does this `git status` differ from the one in **1.2**?
In the git status from 1.2, the command displays that no commits have yet
been made. Also a list of untracked files is displayed with README.md being
one of them.  However, in the git status from 1.5, the command displays that
changes have been made but not staged for the commit. Also README.md is now
listed as modified and not as untracked.

### 1.6 Git command reflections

In one or two sentences each, what does each command do?

- `git init`
- `git status`
- `git add`
- `git commit`
- `git log`
- `git diff`

### 1.7 Repository link

### 1.8 Comparing approaches

In your own words:

- How does the nested-loop approach check for a duplicate?
- How does the set-based approach check for a duplicate?
- What is the runtime and memory trade-off of each?

### 1.9 Pull request merge options

In your own words, what does each GitHub merge option do?

- Create a merge commit
- Squash and merge
- Rebase and merge
