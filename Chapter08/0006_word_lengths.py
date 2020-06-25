"""
Program 8.5
Sort Words in a Sentence in Decreasing Order of Their Length
Display Sorted Words along with Their Length
"""


def sort_words(user_input):
    list_of_words = user_input.split()
    words = list()
    for each_word in list_of_words:
        words.append((len(each_word), each_word))
    words.sort(reverse=True)
    print("After Sorting")
    for length, word in words:
        print(f"The word \"{word}\" is of {length} characters")


def main():
    sentence = input("Enter a sentence ")
    sort_words(sentence)


if __name__ == "__main__":
    main()
