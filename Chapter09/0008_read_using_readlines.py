"""
Program 9.4
Read "rome.txt" using readlines() Method
"""


def main():
    with open("Chapter09/rome.txt") as file_handler:
        print("Print file contents as a list")
        print(file_handler.readlines())


if __name__ == "__main__":
    main()
