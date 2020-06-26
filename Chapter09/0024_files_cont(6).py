"""
Python os and os.path Modules
    os module provides a portable way of using operating system
    dependent functionality.
    For accessing the filesystems, use the os module
    If you want to manipulate paths, use the os.path module
    sys.modules is a dict in which modules are cached

Methods of os module
chdir()     os.chdir(path)          changes the current working directory to path
getcwd()    os.getcwd()             returns a string representing the current working directory
mkdir()     os.mkdir(path)          creates the directory named path. If the directoy already
                                    exists, FileExistsError is raised
remove()    os.remove(path)         removes the file path. If the path is a directory OSError
                                    is raised. Use rmdir() to remove directories.
rmdir()     os.rmdir(path)          removes the directory path. Only works when the directory
                                    is empty, otherwise, OSError is raised
walk()      os.walk(top,            generates the file names in a directory tree by walking the
                topdown=True)       tree either top-down or bottom-up. For each directory in the
                                    tree rooted at directory top, it yields a 3-tuple (dirpath,
                                    dirnames, filenames). The dirpath is a string, the path to
                                    the directory. The dirnames is a list of the names of the
                                    subdirectories in dirpath. filenames is a list of the names
                                    of non-directory files in dirpath. Names in lists contain no
                                    path components. To get a full path, os.path.join(dirpath, name)
rename()    os.rename(old_name,     rename the file from old_name to new_name
                new_name)
listdir()   os.listdir(path=".")    returns a list containing the names of the entries in the
                                    directory given by path. THe list is in arbitrary order and
                                    doe not include "." or ".." even if they are present in the
                                    directory

Methods of os.path module
join()      os.path.join(path,      used to join one or more path components intelligently. Return
                *paths)             value is the concatenation of path and any members of *paths
                                    with exactly one directory
exists()    os.path.exists(path)    returns True if path refers to an existing path else returns
                                    False for broken links
isfile()    os.path.isfile(path)    returns True if path is an existing regular file
isdir()     os.path.isdir(path)     returns True if path is an existing directory
getmtime()  os.path.getmtime(path)  returns time of last modification of path
abspath()   os.path.abspath(path)   returns a normalized absolutized version of the pathname path
path.isabs()os.path.isabs(path)     returns True if path is an absolute path name
relpath()   os.path.relpath(path,   returns a relative filepath to path either from the current
                start=os.curdir)    directory of from an optional start directory
dirname()   os.path.dirname(path)   returns the directory name of the pathname path
basename()  os.path.basename(path)  returns the base name of pathname path
split()     os.path.split(path)     splits the pathname path into a pair, (head, tail) where the
                                    tail is the last pathname component and the head is everything
                                    leading up to that. The tail part will never contain a slash; if
                                    path ends in a slash, the tail will be empty. If there is no slash
                                    in the path name, head will be empty. If path is empty, bot head
                                    and tail are empty
splitext()  os.path.splitext(path)  splits the pathname path into a pair (root,ext) such that
                                    root + ext == path where ext begins with a period and contains at
                                    most one period and root is everything leading up to that
getsize()   os.path.getsize(path)   returns the size in bytes of path
"""
import os
os.getcwd()
os.mkdir("Chapter09/Python_OS_Demo")
os.chdir("Chapter09/Python_OS_Demo")
os.getcwd()

with open("Data_Mining", "w") as f:
    f.write("abc")

os.remove("Data_Mining")
os.mkdir("Data_Science")
os.chdir("Data_Science")
os.getcwd()
os.mkdir("Machine_Learning")
os.rmdir("Machine_Learning")
os.chdir("..")
os.getcwd()
os.rmdir("Data_Science")
os.chdir("..")
os.getcwd()
os.rmdir("Python_OS_Demo")
os.chdir("..")
os.getcwd()

os.path.join("Python_OS_Demon", "Data_Science")
os.path.abspath("Chapter09")
os.path.getsize("Chapter09/0001_files.py")
os.listdir(".")
os.path.split(os.getcwd())
os.path.splitext("Chapter09/0001_files.py")
os.path.basename("Chapter09/0001_files.py")
os.path.dirname("Chapter09/0001_files.py")
os.path.relpath("Chapter09/0001_files.py")
os.chdir("Thisdirectorydoesnoteexist")  #FileNotFoundError
