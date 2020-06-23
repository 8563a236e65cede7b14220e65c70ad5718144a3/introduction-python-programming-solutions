"""
Revision Question 12
Print maximum value of the second half of the list
"""


def print_max(integer_list):
    mid = len(integer_list) // 2
    print(f"Max = {max(integer_list[mid:])}")


def main():
    integer_list = list([23, 22, 21, 20, 6, 3, 9, 8])
    print_max(integer_list)


if __name__ == "__main__":
    main()


