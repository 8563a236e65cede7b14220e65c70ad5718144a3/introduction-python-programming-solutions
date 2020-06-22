"""
Program 6.1
Dynamically Build User Input as a List
"""


def main():
    list_items = input("Enter list items separated by a space\n").split()
    print(f"List items are {list_items}")

    items_of_list = []
    total_items = int(input("Enter the number of items\n"))

    for i in range(total_items):
        item = input("Enter list item:\n")
        items_of_list.append(item)

    print(f"List items are {items_of_list}")


if __name__ == "__main__":
    main()