"""
Revision Question 10
Read first n lines of file
"""


def read_lines(filename, n):
    with open(filename) as f:
        for i in range(n):
            print(f.readline(), end="")


def main():
    filename = input("Enter filename ")
    n = int(input("Enter number of lines to read "))
    read_lines(filename, n)


if __name__ == "__main__":
    main()
