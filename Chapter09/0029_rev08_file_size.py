"""
Review Question 8
Get the file size of a plain text file
"""


def filesize_1(filename):
    filesize = 0
    with open(filename, "r") as f:
        filesize = len(f.read())
    return filesize


def filesize_2(filename):
    filesize = 0
    with open(filename, "r") as f:
        f.seek(0, 2)
        filesize = f.tell()
    return filesize


def main():
    filename = input("Enter file name ")
    print(f"Method 1: {filesize_1(filename)} bytes")
    print(f"Method 2: {filesize_2(filename)} bytes")


if __name__ == "__main__":
    main()
