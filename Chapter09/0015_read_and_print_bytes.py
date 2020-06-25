"""
Program 9.11
Program to Read and Print Each Byte in the Binary File
"""


def main():
    with open("Chapter09/workfile", "wb") as f:
        f.write(b"abcdef")
    with open("Chapter09/workfile", "rb") as f:
        byte = f.read(1)
        print("Print each byte in the file")
        while byte:
            print(byte)
            byte = f.read(1)


if __name__ == "__main__":
    main()
