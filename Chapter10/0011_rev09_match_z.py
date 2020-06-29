"""
Review Question 9
Matches a word containing "z"
"""
import re


def main():
    user_string = input("Enter sequence ")
    pattern = re.compile(r"\b\w*z\w*\b")
    match_object = pattern.search(user_string)
    if match_object:
        print("Match found")
        print(match_object.group())
    else:
        print("No match found")


if __name__ == "__main__":
    main()
