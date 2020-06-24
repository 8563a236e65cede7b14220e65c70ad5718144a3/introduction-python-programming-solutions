"""
Review Question 12
Create a dictionary that friends names as
keys and phone numbers as values. Print dictionary
in sorted order.
Prompt user to check for name in dictionary.
If name not present, add details
"""


def build_dictionary(dictionary):
    while True:
        name = input("Enter friend name ")
        number = input("Enter phone number ")
        dictionary.update({name: number})
        command = input("Enter y to add another entry ")
        if command != "y":
            break


def display_sorted(dictionary):
    sorted_keys = sorted(dictionary)
    for key in sorted_keys:
        print(f"[{key}] = [{dictionary[key]}]")


def search_dictionary(dictionary, key):
    if key in dictionary:
        print("Contact Found")
        print(f"[{key}] = [{dictionary[key]}]")
    else:
        print("Contact Not Found")
        name = input("Enter friend name ")
        number = input("Enter phone number ")
        dictionary.update({name: number})


def main():
    dictionary = dict()
    build_dictionary(dictionary)
    display_sorted(dictionary)
    key = input("Enter contact to search for ")
    search_dictionary(dictionary, key)
    key = input("Enter contact to search for ")
    search_dictionary(dictionary, key)
    display_sorted(dictionary)


if __name__ == "__main__":
    main()
