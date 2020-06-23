"""
Review Question 8
Sort elements in a list in ascending order using insertion sort
"""


def insertion_sort(list_name):
    for j in range(1, len(list_name)):
        key = list_name[j]
        i = j - 1
        while i >= 0 and list_name[i] > key:
            list_name[i+1] = list_name[i]
            i = i - 1
        list_name[i+1] = key


def main():
    integer_list = list([5, 2, 4, 6, 1, 3])
    print(f"List is\n{integer_list}")
    insertion_sort(integer_list)
    print(f"Sorted list is\n{integer_list}")


if __name__ == "__main__":
    main()


