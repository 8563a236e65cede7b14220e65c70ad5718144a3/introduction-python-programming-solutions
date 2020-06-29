"""
Review Question 16
Find all five characters long words in a string
"""
import re


def main():
    user_string = input("Enter string ")
    pattern = re.compile(r"\b\w{5}\b")
    match_list = pattern.findall(user_string)

    if len(match_list) == 0:
        print("No match found")
    else:
        print(f"Matches found\n{match_list}")


if __name__ == "__main__":
    main()
