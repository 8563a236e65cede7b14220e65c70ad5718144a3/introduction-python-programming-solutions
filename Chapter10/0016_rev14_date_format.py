"""
Review Question 14
Read a file and convert date of yyyy-mm-dd format
to dd-mm-yyyy format
"""
import re


def main():
    with open("Chapter10/date.txt", "r") as f:
        date = f.read()
        pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
        replaced_string = pattern.sub(r"\3-\2-\1", date)
        print(f"Original date\n{date}")
        print(f"Modified date\n{replaced_string}")


if __name__ == "__main__":
    main()
