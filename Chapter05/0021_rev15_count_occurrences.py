"""
Review Question 15
Count occurrences of character in string
"""


def count_character(string, char):
    count = 0
    for each_char in string:
        if each_char == char:
            count += 1
    return count


def main():
    user_string = input("Enter a string\n")
    user_char = input("Enter a character to count\n")

    result = count_character(user_string, user_char)

    print(f"Number of occurrences = {result}")
    print(f"Number of occurrences with count()= {user_string.count(user_char)}")


if __name__ == "__main__":
    main()


