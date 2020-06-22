"""
Review Question 19
Insert a string into the middle of another string
"""


def insert_string(main, sub):
    mid = int(len(main) / 2)
    result = main[:mid] + sub + main[mid:]
    return result


def main():
    main_string = input("Enter main string\n")
    sub_string = input("Enter sub string\n")
    result = insert_string(main_string, sub_string)
    print(f"The new string is\n{result}")


if __name__ == "__main__":
    main()


