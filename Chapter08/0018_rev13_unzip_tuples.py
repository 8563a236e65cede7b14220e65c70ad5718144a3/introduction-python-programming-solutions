"""
Review Question 13
Unzip a list of tuples into individual lists
"""


def unzip(zipped):
    zip_list = list(zipped)
    print(f"The zipped list is\n{zip_list}")
    n_items = len(zip_list)
    n_lists = len(zip_list[0])
    result = []

    for lists in range(n_lists):
        result.append([])
        for items in range(n_items):
            result[lists].append(zip_list[items][lists])
    return result


def main():
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)

    list_of_lists = unzip(zipped)
    print(f"The list of lists is:\n{list_of_lists}")


if __name__ == "__main__":
    main()
