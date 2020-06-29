"""
Review Question 13
Extract year, month and date from an url
"""
import re


def main():
    url = input("Enter url ")
    date = re.compile(r"\d{4}/\d{2}/\d{2}")
    match_object = date.search(url)
    if match_object:
        print("Match found")
        print(match_object.group())
    else:
        print("No match found")


if __name__ == "__main__":
    main()
