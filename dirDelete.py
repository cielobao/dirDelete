from os import path, walk, rename, urandom, remove, rmdir
from sys import argv
from uuid import uuid4

def main():
    "Test arguments and either destroy path or print help."
    if len(argv) == 2 and path.isdir(argv[1]):
        destroy(argv[1])
    else:
        print('Usage: {} <directory>'.format(path.basename(argv[0])))

def destroy(directory):
    "Render the directory with its contents unrecoverable."
    for root, dirs, files in walk(directory, False):
        for name in files:
            rename_file(root, name)
        rename_file(root)
    delete_file_or_dir(root)

def rename_file(root, name=None):
    "Try to rename a file or directory."
    if name is None:
        old, new = root, path.join(path.dirname(root), uuid4().hex)
    else:
        old, new = path.join(root, name), path.join(root, uuid4().hex)
    try:
        rename(old, new)
    except EnvironmentError:
        return old
    return new

def delete_file_or_dir(file_or_dir):
    "Try to delete a file or directory."
    try:
        if path.isfile(file_or_dir):
            remove(file_or_dir)
        elif path.isdir(file_or_dir):
            rmdir(file_or_dir)
    except EnvironmentError:
        pass


if __name__ == '__main__':
    main()
