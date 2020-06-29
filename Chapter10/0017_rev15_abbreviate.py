"""
Review Question 15
Abbreviate "Street" as "St.
"""
import re


def main():
    address = input("Enter address ")
    pattern = re.compile(r"Street")
    replaced_string = pattern.sub("st.", address)
    print(f"Original String\n{address}")
    print(f"Modified String\n{replaced_string}")


if __name__ == "__main__":
    main()
