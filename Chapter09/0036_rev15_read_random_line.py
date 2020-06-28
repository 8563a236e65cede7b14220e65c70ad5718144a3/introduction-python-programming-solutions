"""
Review Question 15
Read random line of file
"""
import random


def read_random_line(filename):
    with open(filename, "r") as f:
        f_list = f.readlines()
        n = len(f_list)
        print(f_list[random.randint(0, n-1)], end="")


def main():
    filename = input("Enter filename ")
    read_random_line(filename)


if __name__ == "__main__":
    main()
