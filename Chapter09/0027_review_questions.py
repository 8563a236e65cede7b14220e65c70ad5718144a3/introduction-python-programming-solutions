"""
1)  A file is the common storage unit in a computer, and all programs
    and data are "written" into a file and "read" from a file
    There are two types of files
        text files
        binary files
    They encode data differently
    Bits in text files represent characters
    Bits in binary files represent custom data

2)
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
            not exist, it creates a new file. If a file already exists
            then it will be overwritten
    "a+"    Opens the file for reading and appending. If the file already
            exists, the data is appended. If the file does not exist
            it creates a new file
    "x"     Creates a new file. If the file already exists, the operation
            fails
    "rb"    Opens the binary file in read-only mode
    "wb"    Opens the file for writing the data in binary format
    "rb+"   Opens the file for both reading and writing in binary format

    file_handler = open("moon.txt", "x")
    file_handler = open("moon.txt", "r")
    file_handler = open("moon.txt", "w")
    file_handler = open("moon.txt", "a")
    file_handler = open("moon", "rb")
    file_handler = open("moon", "wb")
    file_handler = open("moon", "rb+")

3)  To read and write to a text file you need to create a file
    handler
        try:
            fh = open(filename, "w")
    Write some data to the file
            try:
                fh.write("abc")
    Then close the file handle so data persists
            finally:
                fh.close()
    And handle any exceptions that occur
        except IOError:
            handle_exception()
    To read from the file, open in read mode
        fh = open(filename, "r")
    Iterate through each line
        for each_line in fh:
            print(each_line, end="")
    And close the file handler
        fh.close()

4)  To read and write to a binary file you need to create a file
    handler
        try:
            fh = open(filename, "wb")
    Write some data to the file
            try:
                fh.write(b"abc")
    Then close the file handle so data persists
            finally:
                fh.close()
    And handle any exceptions that occur
        except IOError:
            handle_exception()
    To read from the file, open in read mode
        fh = open(filename, "rb")
    Iterate through the bytes
        byte = fh.read(1)
        while byte:
            print(byte)
            byte = fh.read(1)
    And close the file handler
        fh.close()

5)  To write to csv file
    Import csv
        import csv
    Open file in write mode
        with open(filename, "w", newline="") as csvfile:
    Create csv writer
            csv_writer = csv.writer(csvfile)
    Use writerow method for headers
            csv_writer.writerow(headers)
    Use writerows method for data
            csv_writer.writerows(each_row)

    To read from csv file
    Import csv
        import csv
    Open file in read mode
        with open("employees.csv", newline="") as csvfile:
    Create csv reader
            csv_reader = csv.reader(csvfile)
    Iterate along each row to print
            for each_row in csv_reader:
                print(",".join(each_row))

6)  Methods of os module
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
"""