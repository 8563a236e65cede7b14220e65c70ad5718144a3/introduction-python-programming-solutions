"""
Program 5.9
Count the Occurrences of User-Entered Words in a sentence
"""


def count_word(word_occurrence, user_string):
    word_count = 0
    for each_word in user_string.split():
        if each_word == word_occurrence:
            word_count += 1
    print(f"The word '{word_occurrence}' has occurred {word_count} times")


def main():
    input_string = input("Enter a string ")
    user_word = input("Enter a word to count its occurrence")
    count_word(user_word, input_string)

    print(f"Using count() = {input_string.count(user_word)}")


if __name__ == "__main__":
    main()


