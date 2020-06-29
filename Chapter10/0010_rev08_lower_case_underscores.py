"""
Review Question 8
Find sequences of lower case letters joined with an underscore
"""
import re


def main():
    user_string = input("Enter sequence ")
    pattern = re.compile(r"[a-z]+_[a-z]+")
    print(pattern.findall(user_string))


if __name__ == "__main__":
    main()
