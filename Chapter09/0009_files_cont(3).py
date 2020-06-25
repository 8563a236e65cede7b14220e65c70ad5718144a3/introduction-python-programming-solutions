"""
write() Method
"""
file_handler = open("Chapter09/moon.txt", "w")
file_handler.write("Moon is a natural satellite")
file_handler.close()
file_handler = open("Chapter09/moon.txt", "a+")
file_handler.write("of the earth")
file_handler.close()
file_handler = open("Chapter09/moon.txt", "r")
file_handler.read()
file_handler.close()
file_handler = open("Chapter09/moon.txt", "w")
file_handler.writelines(["Moon is a natural satellite", "", "of the earth"])
file_handler.close()
file_handler = open("Chapter09/moon.txt")
file_handler.read()
file_handler.close()

"""
seek() Method
"""
f = open("Chapter09/workfile", "w")
f.write("0123456789abcdef")
f.close()
f = open("Chapter09/workfile", "r")
f.seek(5)
f.read()
f.close()

"""
In text files, those opened without a b in the mode string, only
allow seeks relative to the beginning of the file - except for 
seeking to the end of the file with seek(0, 2). 
"""
f = open("Chapter09/workfile", "w")
f.write("0123456789abcdef")
f.close()
f = open("Chapter09/workfile", "rb+")
f.seek(2)
f.seek(2, 1)
f.read()
f.seek(-3, 2)
f.read()

"""
tell() method returns the file handler's current position
"""
f = open("Chapter09/workfile", "w")
f.write("0123456789abcdef")
f.close()

f = open("Chapter09/workfile")
s1 = f.read(2)
print(s1)
f.tell()

s2 = f.read(3)
print(s2)
f.tell()

f.close()

