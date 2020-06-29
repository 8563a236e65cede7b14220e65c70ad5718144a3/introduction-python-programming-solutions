"""
Review Question 11
Search numbers (0-9) of length between 1 to 3
in a given string
"""
import re


def main():
    user_string = input("Enter sequence ")
    pattern = re.compile(r"\b(\d{1,3})\b")
    match_list = pattern.findall(user_string)

    if len(match_list) == 0:
        print("No matches found")
    else:
        print(f"Matches found\n{match_list}")


if __name__ == "__main__":
    main()
