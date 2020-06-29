"""
Review Question 7
Write a regular expression which matches strings which starts
with a sequence of digits - at least one digit - followed by
a blank and after these arbitrary characters
"""
import re


def main():
    user_string = input("Enter sequence to match ")

    pattern = re.compile(r"\d+\s+\w+")
    match_object = pattern.match(user_string)
    if match_object:
        print("Pattern matches")
    else:
        print("Pattern does not match")


if __name__ == "__main__":
    main()
