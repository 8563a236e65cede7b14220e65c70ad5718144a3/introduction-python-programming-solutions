"""
Review Question 14
Remove newline characters from a file
"""


def remove_newlines(filename):
    with open(filename, "r") as f:
        f_list = f.readlines()
        n = len(f_list)
        for i in range(0, n):
            f_list[i] = f_list[i].replace("\n", "")
        print("".join(f_list))


def main():
    filename = input("Enter filename ")
    remove_newlines(filename)


if __name__ == "__main__":
    main()
