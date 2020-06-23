"""
Program 7.8
Accept a Sentence and Calculate Number
of Digits, Uppercase and Lowercase Letters
"""


def main():
    sentence = input("Enter a sentence\n")
    construct_dictionary = {"digits": 0, "lowercase": 0, "uppercase": 0}
    for each_character in sentence:
        if each_character.isdigit():
            construct_dictionary["digits"] += 1
        elif each_character.isupper():
            construct_dictionary["uppercase"] += 1
        elif each_character.islower():
            construct_dictionary["lowercase"] += 1
    print("The number of digits, lowercase and uppercase letters are")
    print(construct_dictionary)


if __name__ == "__main__":
    main()
