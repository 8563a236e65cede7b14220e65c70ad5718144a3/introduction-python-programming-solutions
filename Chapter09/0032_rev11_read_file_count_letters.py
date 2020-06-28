"""
Review Question 11
Count the occurrences of each letter in a file
Prompt user to enter filename
"""


def count_letters(filename):
    count_letters = dict()
    upper = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower = set("abcdefghijklmnopqrstuvwxyz")
    with open(filename, "r") as f:
        contents = f.read()
        for each_character in contents:
            if each_character in lower or each_character in upper:
                count_letters[each_character] = count_letters.get(each_character, 0) + 1
    print(count_letters)


def main():
    filename = input("Enter filename ")
    count_letters(filename)


if __name__ == "__main__":
    main()
