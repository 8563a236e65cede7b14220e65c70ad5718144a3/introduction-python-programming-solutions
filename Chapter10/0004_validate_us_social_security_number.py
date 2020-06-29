"""
Program 10.3
Validate U.S.-based Social Security Number
"""
import re


def main():
    pattern = re.compile(r"\b\d{3}-?\d{2}-?\d{4}\b")
    match_object = pattern.search("Social Security Number"
                                  "For James is 916-30-2017")
    if match_object:
        print(f"Extracted Social Security Number is {match_object.group()}")
    else:
        print("No Match")


if __name__ == "__main__":
    main()
