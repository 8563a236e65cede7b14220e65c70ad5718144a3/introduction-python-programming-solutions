"""
Review Question 7
Write a function named addfriot which is passed with a set
of fruit names and their prices and returns a dictionary containing
the entered information and raises a ValueError exception if the
fruit is already present
"""


def addfruit(dictionary):
    name = input("Enter fruit name ")
    price = float(input("Enter Price "))

    if name in dictionary.keys():
        raise ValueError("Fruit is Already Present")
    else:
        dictionary.update({name: price})


def main():
    fruits = {}
    while True:
        command = input("Add another fruit (y/n)")
        if command == "y":
            addfruit(fruits)
            print(fruits)
        else:
            break


if __name__ == "__main__":
    main()
