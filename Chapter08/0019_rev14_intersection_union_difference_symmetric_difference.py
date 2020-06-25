"""
Review Question 14
Program to create an intersection, union, set difference and
symmetric difference of sets
"""


def union(set1, set2):
    temp = set()
    temp.update(set1)
    temp.update(set2)

    return temp


def intersection(set1, set2):
    temp = set()
    for element in set1:
        if element in set2:
            temp.add(element)
    return temp


def difference(set1, set2):
    temp = set()
    for element in set1:
        if element not in set2:
            temp.add(element)
    return temp


def symmetric_difference(set1, set2):
    temp = set()
    for element in set1:
        if element not in set2:
            temp.add(element)
    for element in set2:
        if element not in set1:
            temp.add(element)
    return temp


def main():
    european_flowers = {
        "sunflowers",
        "roses",
        "lavender",
        "tulips",
        "goldcrest"
    }

    american_flowers = {
        "roses",
        "tulips",
        "lilies",
        "daisies"
    }

    print(f"set1\n{american_flowers}")
    print(f"set2\n{european_flowers}")
    print(f"Union\n{union(american_flowers, european_flowers)}")
    print(f"Union Method\n{american_flowers.union(european_flowers)}")
    print(f"Intersection\n{intersection(american_flowers, european_flowers)}")
    print(f"Intersection Method\n{american_flowers.intersection(european_flowers)}")
    print(f"Difference\n{difference(american_flowers, european_flowers)}")
    print(f"Difference Method\n{american_flowers.difference(european_flowers)}")
    print(f"Symmetric Difference\n{symmetric_difference(american_flowers, european_flowers)}")
    print(f"Symmetric Difference Method\n{american_flowers.symmetric_difference(european_flowers)}")


if __name__ == "__main__":
    main()
