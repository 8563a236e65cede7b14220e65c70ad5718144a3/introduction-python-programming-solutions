"""
Program 10.2
Python Program to Check the Validity of a Password
Given by User
The password should satisfy the following criteria:
    Contains at least 1 letter between a and z
    Contains at least 1 number between 0 and 9
    Contains at least 1 letter between A and Z
    Contains at least 1 character from $, #, @
    Minimum length of password: 6
    Maximum length of password: 12
"""
import re


def main():
    lower_case_pattern = re.compile(r"[a-z]")
    upper_case_pattern = re.compile(r"[A-Z]")
    number_pattern = re.compile(r"\d")
    special_character_pattern = re.compile(r"[$#@]")
    password = input("Enter a Password ")
    if len(password) < 6 or len(password) > 12:
        print("Invalid Password. Length Not Matching")
    elif not lower_case_pattern.search(password):
        print("Invalid Password. No Lower-Case Letters")
    elif not upper_case_pattern.search(password):
        print("Invalid Password. No Upper-Case Letters")
    elif not number_pattern.search(password):
        print("Invalid Password. No Numbers")
    elif not special_character_pattern.search(password):
        print("Invalid Password. No Special Characters")
    else:
        print("Valid Password")


if __name__ == "__main__":
    main()
