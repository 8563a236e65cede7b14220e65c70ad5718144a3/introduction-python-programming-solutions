"""
Revision Question 22
Program to concatenate two strings without + operator
"""


def concatenate(string1, string2):
    return "".join([string1, string2])


def main():
    string1 = input("Enter string1\n")
    string2 = input("Enter string2\n")
    result = concatenate(string1, string2)
    print(f"The concatenated string is\n{result}")


if __name__ == "__main__":
    main()


