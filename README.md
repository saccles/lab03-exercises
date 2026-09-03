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
    This command initializes a new git repository in the current directory.
- `git status`
    This command shows you the current status of your git repository. It
    also shows you the branch your on as well as untracked and tracked files
    and file changes.
- `git add`
    This command adds the specified files (or . to add all) to the staging
    area.
- `git commit`
    This command commits your changes to git (now shown as commit with hash
    in git log and git history).
- `git log`
    This command shows you your git history (essentially a list of commits
    with respective commit hashes).
- `git diff`
    This command shows changes to files (in green) that have not yet been
    committed to the git history. For instance, if you accidentally deleted
    a file but did not yet commit the change, you can usually easily undo it
    by reverting to the previous commit.

### 1.7 Repository link

https://github.com/saccles/lab03-exercises

### 1.8 Comparing approaches

In your own words:

- How does the nested-loop approach check for a duplicate?
    The nested approach uses an outer loop to change the index
    (index that matches up with the current item being checked for a match)
    and inner loop to compare all other items (except items
    at index <= outer loop index) at different indices in the array 
    starting at the outer loop index + 1 to the current item to see if
    there is another match. If there is a match, the function immediately
    returns true. Otherwise, this process is repeated until a match is found
    or until the outer and inner loops have finished checking the array,
    then returning false if no duplicate value was found.
- How does the set-based approach check for a duplicate?
    Since sets cannot store duplicate values, the program monitors the
    return code of the method that adds an item to a set for failure. If
    the return code indicates failure, then that means the item that the
    program intended to add to the set was already present in the set,
    indicating that this is a duplicate value, stopping the program 
    and returning true.
- What is the runtime and memory trade-off of each?
    The nested-loop aproach has worse runtime (O(n^2)) and the set-based 
    approach has better runtime (O(n)).
    The set-based approach uses more space though (sets are generally implemented 
    using hash tables, which take up more memory compared to arrays).
    The nested-loop approach uses less space since it is operating only on
    one array and arrays are more space-efficient than sets. 

### 1.9 Pull request merge options

In your own words, what does each GitHub merge option do?

- Create a merge commit
- Squash and merge
- Rebase and merge
