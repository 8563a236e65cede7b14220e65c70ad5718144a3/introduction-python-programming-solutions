"""
Review Question 12
Read the last n lines of a file
Prompt the user to enter the value for n
"""


def read_lines(filename, n):
    contents = list()
    with open(filename, "r") as f:
        contents = f.readlines()
        if len(contents) - n > 0:
            for i in range(len(contents)-n, len(contents)):
                print(contents[i], end="")
        else:
            for i in range(0, len(contents)):
                print(contents[i], end="")
        print()


def main():
    filename = input("Enter filename ")
    n = int(input("Enter number of lines "))
    read_lines(filename, n)


if __name__ == "__main__":
    main()
