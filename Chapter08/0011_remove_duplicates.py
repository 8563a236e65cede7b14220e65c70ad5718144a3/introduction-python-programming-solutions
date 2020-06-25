"""
Program 8.9
Accepts a Sentence as Input and Removes
All Duplicate Words. Print the sorted words
"""


def unique_words(user_input):
    words = user_input.split()
    print(f"The unique and sorted words are {sorted(list(set(words)))}")


def main():
    sentence = input("Enter a sentence\n")
    unique_words(sentence)


if __name__ == "__main__":
    main()
