"""
Program 9.2
Read and Print Each Line in "japan.txt" File Using
with Statement.
"""


def read_file():
    print("Printing each line in text file")
    with open("Chapter09/japan.txt") as file_handler:
        for each_line in file_handler:
            print(each_line, end="")
        print()


def main():
    read_file()


if __name__ == "__main__":
    main()
