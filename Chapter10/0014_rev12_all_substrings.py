"""
Review Question 12
Find all substrings in a string
"""
import re


def main():
    user_string = input("Enter string ")
    user_substring = input("Enter substring ")

    pattern = re.compile(user_substring)
    match_list = pattern.findall(user_string)
    if len(match_list) == 0:
        print("No match found")
    else:
        print(f"Matches found\n{match_list}")


if __name__ == "__main__":
    main()
