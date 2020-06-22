"""
Review Question 16
Parse a binary number to a decimal integer
"""


def bin_to_dec(string):
    result = 0
    n = len(string)
    for i in range(n):
        result += int(string[i]) * (2 ** (n - i - 1))
    return result


def main():
    binary = input("Enter binary number\n")
    result = bin_to_dec(binary)

    print(f"{binary} as decimal is {result}")


if __name__ == "__main__":
    main()


