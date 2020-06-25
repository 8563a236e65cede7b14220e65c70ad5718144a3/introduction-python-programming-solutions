"""
Program 9.4
Read "rome.txt" using readline() Method
"""


def main():
    with open("Chapter09/rome.txt") as file_handler:
        print("Print a single line from the file")
        print(file_handler.readline(), end="")
        print("Print another single line from the file")
        print(file_handler.readline(), end="")


if __name__ == "__main__":
    main()
