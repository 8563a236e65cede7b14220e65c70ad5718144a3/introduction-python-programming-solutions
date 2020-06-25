"""
Program 9.3
Read "rome.txt" File Using read() Method
"""


def main():
    with open("Chapter09/rome.txt") as file_handler:
        print("Print entire file contents")
        print(file_handler.read(), end="")
        print()


if __name__ == "__main__":
    main()

