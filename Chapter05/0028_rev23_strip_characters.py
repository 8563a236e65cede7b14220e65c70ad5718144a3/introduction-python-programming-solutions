"""
Review Question 24
Program to strip a set of characters from a string
"""


def strip(string, characters):
    result = str()
    for each_character in string:
        if each_character in characters:
            pass
        else:
            result += each_character
    return result


def main():
    user_string = input("Enter string to strip\n")
    characters = input("Enter characters to strip\n")

    result = strip(user_string, characters)
    print(f"The stripped string is\n{result}")


if __name__ == "__main__":
    main()


