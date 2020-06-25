"""
File Object Attributes

file_handler.closed returns Boolean True if the file is closed or False otherwise
file_handler.mode   returns the access mode with which the file was opened
file_handler.name   returns the name of the file
"""
file_handler = open("Chapter09/computer.txt", "w")
print(f"File Name is {file_handler.name}")
print(f"File State is {file_handler.closed}")
print(f"File Opening Mode is {file_handler.mode}")

"""
File Methods to Read and Write Data
read()      fh.read([size])         Used to read the contents of a file up
                                    to a size and return it as a string. The
                                    size argument is optional, and, if it is
                                    not specified, then the entire contents
                                    of the file will be read and returned
readline()  fh.readline()           Used to read a single line in a file
readlines() fh.readlines()          Used to read all the lines of a file as
                                    a list
write()     fh.write(string)        Write the contents of the string to file,
                                    returning the number of characters written
writelines()fh.writelines(sequence) Write a sequence of strings to the file
tell()      fh.tell()               Returns an integer giving the file handler's
                                    current position within the file, measured in
                                    bytes from the beginning of the file
seek()      fh.seek(offset,         Used to change the file handler's position. The 
                from_what)          position is computer from adding offset to a
                                    reference point. The reference point is selected
                                    by the from_what argument. 
                                        0 measures from the beginning of the file
                                        1 uses the current file position
                                        2 uses the end of the file
                                    If from_what omitted, default value is 0
"""
f = open("Chapter09/example.txt", "w")
f.write("abcdefgh")
f.close()
f = open("Chapter09/example.txt")
print(f.read(2))
print(f.read(2))
print(f.read(2))
print(f.read(2))
f.close()
