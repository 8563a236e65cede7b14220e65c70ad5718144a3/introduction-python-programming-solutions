"""
Review Question 10
Create a dictionary that accepts a country name
as a key and its capital city as the value.
Display the details in sorted order
"""


def build_dictionary(dictionary):
    while True:
        country = input("Enter country name ")
        capital = input("Enter capital ")
        dictionary.update({country: capital})
        command = input("Enter y to add another entry ")
        if command != "y":
            break


def display_sorted(dictionary):
    sorted_keys = sorted(dictionary)
    for key in sorted_keys:
        print(f"[{key}] = [{dictionary[key]}]")


def main():
    dictionary = dict()
    build_dictionary(dictionary)
    display_sorted(dictionary)


if __name__ == "__main__":
    main()
