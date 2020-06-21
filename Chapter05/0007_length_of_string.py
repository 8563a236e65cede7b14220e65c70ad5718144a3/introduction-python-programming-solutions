"""
Program 5.5
Calculate the length of a string without using the
built-in length function
"""


def strlen(string):
    count = 0
    for each_character in string:
        count += 1
    return count

def main():
    user_string = input("Enter a string:\n")
    length = strlen(user_string)
    print(f"The length of \n'{user_string}'\nis {length}")


if __name__ == "__main__":
    main()


