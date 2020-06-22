"""
Review Question 21
Replace a string with another without using built-in methods
"""


def replace_str(main_string, substring, replacement):
    string = main_string
    length = len(substring)
    index = string.find(substring)

    while index != -1:
        string = string[:index] + replacement + string[index+length:]
        index = string.find(substring)

    return string


def main():
    main_string = input("Enter string\n")
    substring = input("Enter substring\n")
    replacement = input("Enter replacement\n")

    string = replace_str(main_string, substring, replacement)
    print(f"The replaced string is\n{string}")


if __name__ == "__main__":
    main()


