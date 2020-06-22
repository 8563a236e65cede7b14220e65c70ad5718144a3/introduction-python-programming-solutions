"""
Program 6.7
Check if Items in List are Sorted in Ascending or Descending Order
"""


def check_for_sort_order(list_items):
    ascending = descending = True
    print(f"List items:\n{list_items}")
    for i in range(len(list_items) - 1):
        if list_items[i] < list_items[i+1]:
            descending = False
        if list_items[i] > list_items[i+1]:
            ascending = False
        if not ascending and not descending:
            break

    if ascending:
        print("Items in list are in Ascending order")
    elif descending:
        print("Items in list are in Descending order")
    else:
        print("Items in list are not sorted")


def main():
    check_for_sort_order([1, 4, 2, 5, 3])
    check_for_sort_order([1, 2, 3, 4, 5])
    check_for_sort_order([5, 4, 3, 2, 1])


if __name__ == "__main__":
    main()

