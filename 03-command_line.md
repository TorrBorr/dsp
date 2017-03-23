# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

|   Command    |    Function   |  
| :------------| ------------- |   
|  **pwd**     |  show current working directory path |  
|   **mkdir**  |    create a new folder/directory |  
|    cd         |  change directory  |  
|   cd ..  |  go up one directory  |  
|    **rmdir**  |  delete directory |  
|   **rm**  |  delete file  |  
|   rm -rf *  |  delete folder and all files  |  
|   **touch**  |  creates a new empty file or changes the timestamp on an existing file |  
|   ls  |  list files/folders in the directory  |  
|   **ls -a**  | lists hidden files/folders|  
|   **cp** (-r)  | copy file (folder+contents) from one place to another (used to remane a file) |   
|    **mv** (-r)  |  move a file (folder+contents) from one directory to another directory (also renames)  |  
|  -r  |  modifies command to be recursive (act on contents of folder) |  



---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

|   Command    |    Function   |  
| :------------| ------------- |  
| ls          | lists files and directories in current directory |  
| ls -a     | lists hidden files and folders |  
| ls -l      | lists files and directories along with the details size, modification date and time, file or folder name, owner and permissions |  
| ls -lh    | lists file sizes in human readable format |  
| ls -lah  | lists files and directories (including hidden files and directories) along with the details size, modification date and time, file or folder name, owner and permissions |  
| ls -t     |sorts files and directories by time and date |  
| ls -Glp  | lists files and folders (without owner information) and adds a "/" to mark directories |  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

-R (displays subdirectories)  
-p (displays a “/“ on directories)  
-t (newest first)  
-m (comma separated list)  
-1 (each entry on a line)  

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs takes a string from stdin and tokenizes it into its constituent pieces based on delimiters to pass in as arguments.
One use is to take an output that is on multiple lines and convert it into one line. 
  

 

