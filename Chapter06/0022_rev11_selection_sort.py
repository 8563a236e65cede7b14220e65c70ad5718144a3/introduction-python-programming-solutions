"""
Review Question 11
Sort elements in a list in ascending order using selection sort
"""


def selection_sort(integer_list):
    for i in range(len(integer_list)):
        min_index = i
        for j in range(i + 1, len(integer_list)):
            if integer_list[min_index] > integer_list[j]:
                min_index = j
        integer_list[i], integer_list[min_index] = integer_list[min_index], integer_list[i]


def main():
    integer_list = list([64, 25, 12, 22, 11])
    print(f"Unsorted list\n{integer_list}")
    selection_sort(integer_list)
    print(f"Sorted list\n{integer_list}")


if __name__ == "__main__":
    main()


