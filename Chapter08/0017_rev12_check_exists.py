"""
Review Question 12
Check whether an item exists within a tuple
"""


def check_exists1(tuple_to_check, item):
    found = 0
    n = len(tuple_to_check)
    for i in range(n):
        if tuple_to_check[i] == item:
            found = 1
            break
    if found:
        print(f"Found item at index {i}")
    else:
        print("Item not found")


def check_exists2(tuple_to_check, item):
    try:
        index = tuple_to_check.index(item)
    except ValueError:
        print("Item not found")
    else:
        print(f"Found item at index {index}")


def main():
    my_tuple = tuple("abcdefghijklmnopqrstuvwxyz")
    print(f"Tuple\n{my_tuple}")
    search = input("Enter letter to search: ")
    print(f"Using check_exists1():")
    check_exists1(my_tuple, search)
    print(f"Using check_exists2():")
    check_exists2(my_tuple, search)


if __name__ == "__main__":
    main()
