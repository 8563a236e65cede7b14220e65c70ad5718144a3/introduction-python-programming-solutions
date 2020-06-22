"""
Review Question 18
Accept user string and remove vowels
"""


def remove_vowels(string):
    result = str()
    for each_char in string:
        if each_char in "aeiou":
            pass
        else:
            result += each_char
    return result


def main():
    user_string = input("Enter string\n")
    print(f"without vowels = {remove_vowels(user_string)}")


if __name__ == "__main__":
    main()


