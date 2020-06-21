"""
Review Question 13
Program to display pascal's triangle with functions
"""


def binom(line, i):
    temp = 1
    k = i
    if k > line - i:
        k = line - k
    for j in range(k):
        temp = temp * (line - j)
        temp = temp // (j + 1)
    return temp


def pascal(n):
    temp = 0

    for line in range(n):
        for i in range(line + 1):
            temp = binom(line, i)
            print(f"{temp}", end=" ")
        print("")


def main():
    n = int(input("Enter the number of rows to print"))
    pascal(n)


if __name__ == "__main__":
    main()

