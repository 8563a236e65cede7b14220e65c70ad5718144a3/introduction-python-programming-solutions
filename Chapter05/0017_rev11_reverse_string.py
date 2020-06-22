"""
Review Question 11
Take a string as an argument and display the letters backwards,
one per line
"""


def reverse_string(string):
    rev_string = string[::-1]
    for each_char in rev_string:
        print(each_char)


def main():
    user_string = input("Enter string\n")
    reverse_string(user_string)


if __name__ == "__main__":
    main()


