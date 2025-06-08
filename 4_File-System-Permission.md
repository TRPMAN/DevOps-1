## File System
- file : check file type
- ln -s : link
- ---------- : regular file
- d--------- : directory file
- l--------- : link file
- c--------- : special file
- s--------- : socket file
- p--------- : pipe file

## File Permissions
- r => read w => write x => execute
- --- --- --- => filetype user group other
- chmod -<option> <username>:<group> <path> : change permission
  - -R : Recursive
- chmod -<option> <(U,G,O)(-,+)(r,w,x)> <path> : change permission
- chmod -<option> 640 <path> : change permission
- 4 => Read 2 => Write 1 => execute
- 1st => User, Permission 6 = 4 + 2 (R + w)
- 2nd => Group, Permission 4 = 4 + 0 (R)
- 3rd => Other, Permission 0 = 0 (No RWX)

## Archiving
- tar -czvf <name>.tar.gz : Archive
- tar -xzvf <name>.tar.gz : Extract
  - -C <path> : Extract to
- can use zip unzip if install
