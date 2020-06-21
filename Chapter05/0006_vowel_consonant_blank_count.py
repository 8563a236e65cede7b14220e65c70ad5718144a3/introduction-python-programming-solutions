"""
Program 5.4
Count the Total Number of Vowels, Consonants and
Blanks in a String
"""


def main():
    user_string = input("Enter a string:\n")
    vowels = 0
    consonants = 0
    blanks = 0
    for each_character in user_string:
        if each_character in "aeiou":
            vowels += 1
        elif each_character == " ":
            blanks += 1
        else:
            consonants += 1
    print(f"Total number of Vowels in user entered string is {vowels}")
    print(f"Total number of Consonants in user entered string is {consonants}")
    print(f"Total number of Blanks in user entered string is {blanks}")


if __name__ == "__main__":
    main()


