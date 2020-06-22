"""
Review Question 20
Sort a string lexicographically
"""


def sort_lexic(string):
    str_list = list(string)
    str_list.sort()
    return "".join(str_list)


def main():
    user_string = input("Enter string to sort\n")
    result = sort_lexic(user_string)
    print(f"The sorted string is {result}")


if __name__ == "__main__":
    main()


