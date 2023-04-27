# dirDelete
Python script that can be used to securely delete files and directories on a filesystem, making the data contained within them unrecoverable.


The script takes one argument, which is the directory that you want to securely delete. To use the script, open a terminal or command prompt and navigate to the directory where the script is saved. Then run the following command:
python3 secure_delete.py <directory>

Replace <directory> with the path to the directory that you want to securely delete.

How it works
The script imports several modules from the Python standard library, including os, sys, and uuid. It defines three functions: main(), destroy(directory), rename_file(root, name=None), and delete_file_or_dir(file_or_dir).

The main() function checks the command line arguments passed to the script and either calls the destroy() function on the provided directory or prints a usage message.

The destroy(directory) function walks through the specified directory and its subdirectories, renaming each file and directory to a randomly generated name using the rename_file() function. It then deletes each renamed file and directory using the delete_file_or_dir() function.

The rename_file(root, name=None) function renames a file or directory by generating a new random name using the uuid4() function from the uuid module and renaming the file or directory with the new name using the rename() function from the os module.

The delete_file_or_dir(file_or_dir) function deletes a file or directory using the remove() or rmdir() function from the os module.

Note
This script is intended to permanently delete files and directories, and as such, it should be used with caution. Once files and directories have been deleted using this script, they cannot be recovered. Please make sure you have a backup of any important data before using this script.
