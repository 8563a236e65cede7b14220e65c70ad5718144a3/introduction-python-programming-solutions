"""
Program 5.3
Print the characters which are common in two strings
"""
def common_characters(string_1, string_2):
    for letter in string_1:
        if letter in string_2:
            print(f"Character '{letter}' is found in both the strings")


def main():
    common_characters("rose", "goose")


if __name__ == "__main__":
    main()


