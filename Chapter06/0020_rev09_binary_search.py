"""
Review Question 9
Use binary search to find the key element in this list
"""


def binary_search(list_name, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if list_name[mid] == x:
            return mid
        elif list_name[mid] > x:
            return binary_search(list_name, l, mid - 1, x)
        else:
            return binary_search(list_name, mid + 1, r, x)
    else:
        return -1


def main():
    integer_list = [2, 3, 4, 10, 40]
    x = 10

    result = binary_search(integer_list, 0, len(integer_list) - 1, x)

    if result != -1:
        print(f"Element present at index {result}")
    else:
        print("Element is not present in list")


if __name__ == "__main__":
    main()


