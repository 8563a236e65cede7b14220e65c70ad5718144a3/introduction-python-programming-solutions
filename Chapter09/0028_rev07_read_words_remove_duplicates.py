"""
Review Question 7
Prompt user to enter a text file, read words from the file
and display all non-duplicate words in ascending order
"""


def read_words(filename):
    words = set()
    with open(filename, "r") as f:
        for each_row in f:
            words.update(set(each_row.split()))
    return words


def main():
    filename = input("Enter filename ")
    word_set = read_words(filename)
    print(f"{sorted(word_set)}")
    print(f"{len(word_set)}")


if __name__ == "__main__":
    main()
