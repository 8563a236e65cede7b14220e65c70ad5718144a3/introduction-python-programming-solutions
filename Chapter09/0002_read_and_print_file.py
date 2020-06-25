"""
Program 9.1
Read and Print each line in "egypt.txt" file.
"""


def read_file():
    try:
        file_handler = open("Chapter09/egypt.txt", "r")
    except IOError:
        print("IOError")
    else:
        print("Printing each line in the text file")
        try:
            for each_line in file_handler:
                print(each_line, end="")
        finally:
            file_handler.close()
            print()


def main():
    read_file()


if __name__ == "__main__":
    main()
