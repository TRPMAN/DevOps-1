## File System
check file type         : file
link                    : ln -s
regular file            : ----------
directory file          : d---------
link file               : l---------
special file            : c---------
socket file             : s---------
pipe file               : p---------

## File Permissions
r => read w => write x => execute
- --- --- --- => filetype user group other
change permission       : chmod -(option) (username):(group) (path)
  --> Recursive         : -R       
change permission       : chmod -(option) ((U,G,O)(-,+)(r,w,x)) ( path)
change permission       : chmod -(option) 640 (path)
4 => Read 2 => Write 1 => execute
1st => User, Permission 6 = 4 + 2 (R + w)
2nd => Group, Permission 4 = 4 + 0 (R)
3rd => Other, Permission 0 = 0 (No RWX)

## Archiving
Archive                 : tar -czvf (name).tar.gz
Extract                 : tar -xzvf (name).tar.gz
  --> Extract to        : -C (path)     
can use zip unzip if install  
