"""
Files
    A file is the common storage unit in a computer, and
    all programs and data are "written" into a file and
    "read" from a file

Creating and Opening Text Files
    All files must be opened first before they can be
    read from or written
    open() returns an object called a file handler
        file_handler = open(filename, mode)
    mode is optional, "r" used by default

    Access Modes of Files
    "r"     Opens the file in read only mode
    "w"     Opens the file for writing. If a file already exists, then
            it will get overwritten. If the file does not exist, then
            it creates a new file
    "a"     Opens the file for appending data at the end of the file
            automatically. If the file does not exist it creates a
            new file.
    "r+"    Opens the file for both reading and writing
    "w+"    Opens the file for reading and writing. If the file does
            not exist, it creates a new file. If a file alread exists
            then it will be overwritten
    "a+"    Opens the file for reading and appending. If the file already
            exists, the data is appended. If the file does not exist
            it creates a new file
    "x"     Creates a new file. If the file already exists, the operation
            fails
    "rb"    Opens the binary file in read-only mode
    "wb"    Opens the file for writing the data in binary format
    "rb+"   Opens the file for both reading and writing in binary format
"""
file_handler = open("moon.txt", "x")
file_handler = open("moon.txt", "r")
file_handler = open("titanic.txt", "r")   #FileNotFoundError

"""
close() Method
    file_handler.close()
"""
file_handler = open("moon.txt", "w")
file_handler.close()

"""
If an exception occurs while performing some operation on
the file, then the code exits without closing the file.
Use try-except-finally to overcome the problem
"""
try:
    f = open("file", "w")
    try:
        f.write("Hello World!")
    finally:
        f.close()
except IOError:
    print("oops!")

"""
You should not be writing to the file in the finally block, as
any exceptions raised there will not be caught by the except block.
The finally block always executes regardless of what happens. The use
of return in the except block will not skip the finally block. finally
cannot be skipped no matter what; that is where clean up code goes.
"""
