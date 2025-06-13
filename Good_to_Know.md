# Good to Know

## Directory/files
- .git/config : config file
- .gitignore : do not track specific file

## Command
- git init : initialized empty Git repository
- git status : current state of repository
- git add <file> : adding files to staging area(tracking files for any change)
- git rm,mv <file> : remove,move file
- git commit -m "<message>" : commit with message
- git log --oneline : show commit history
- git show <commit-id> : show full details in that commi
- git remote add <origin-name> <url> : add a remote repository with a specific name pointing to a URL
- git branch <-M,-m> <old-branch> <new-branch> : change branch name 
  - -M : force rename, overwriting <new-branch> with <old-branch> if it already exists
  - -m : rename the branch only if <new-branch> doesn't already exist
- git push <origin-name> <branch-name> : push all committed changes from <branch-name> to the remote named <origin-name>
- git branch : branch command
  - -c <branch-name> : create branch
  - -a : show all branch
- git checkout <branch-name> : switch branch
- git switch <branch-name> : switch branch(newer)
- gii merge <branch-name> : merge to target branch
- git diff : show differences between working directory and staging area
  - --cached : show differences between staging area and last commit
- git restore --staged <file-name> : unstage the file (remove from staging area)
- git revert <commit-id or HEAD> : create a new commit that undoes the changes of a specific commit (safe way)
- git reset --hard <commit-id or HEAD> : reset current branch to specific commit and discard all changes (dangerous)
- git tag <tagname> <commit> : create a lightweight tag on a specific commit (optional commit, default is HEAD)
- git tag -a <tagname> -m "<message>" : create an annotated tag with a message (recommended for releases)
- git push --tags : push all local tags to remote