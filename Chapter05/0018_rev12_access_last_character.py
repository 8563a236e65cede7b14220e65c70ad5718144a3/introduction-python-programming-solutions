"""
Review Question 12
Access last character of string
"""


def print_last_character(string):
    index = len(string) - 1
    print(string[index])


def main():
    user_string = input("Enter string\n")
    print_last_character(user_string)


if __name__ == "__main__":
    main()


