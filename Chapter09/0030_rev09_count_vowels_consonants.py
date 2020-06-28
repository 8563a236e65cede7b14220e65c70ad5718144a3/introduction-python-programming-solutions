"""
Review Question 9
Display number of vowels and consonants in a file
"""


def count_vowels_consonants(filename):
    count = {"vowels": 0, "consonants": 0}
    vowels = set("AEIOUaeiou")
    consonants = set("BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz")
    with open(filename, "r") as f:
        word_list = f.read().split()
        for each_word in word_list:
            for each_character in list(each_word):
                if each_character in vowels:
                    count["vowels"] += 1
                elif each_character in consonants:
                    count["consonants"] += 1
                else:
                    pass
    print(count)


def main():
    filename = input("Enter filename ")
    count_vowels_consonants(filename)


if __name__ == "__main__":
    main()
