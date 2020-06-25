"""
Program 9.6
Remove the comment character from all the lines in a given
Python source file
"""


def main():
    with open("Chapter09/Sample_Program.py") as file_handler:
        for each_row in file_handler:
            each_row = each_row.replace("#", "")
            print(each_row, end="")
        print()


if __name__ == "__main__":
    main()
