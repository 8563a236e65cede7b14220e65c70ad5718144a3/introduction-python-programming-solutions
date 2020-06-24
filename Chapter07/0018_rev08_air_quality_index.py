"""
Review Question 8
Add air quality information as value and date as
key to dictionary from user input
"""


def air_quality():
    quality_index = dict()
    number = int(input("Enter number of entries "))
    for i in range(number):
        date = input("Enter date ")
        value = float(input("Enter value "))
        quality_index.update({date: value})
    return quality_index


def main():
    quality_index = air_quality()
    print(f"{quality_index}")


if __name__ == "__main__":
    main()
