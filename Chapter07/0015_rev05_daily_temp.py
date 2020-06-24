"""
Review Question 5
Prompt user for average temperature for each day of
the week and return a dictionary containing the entered
information
"""


def create_dictionary():
    temperature = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0,
    }

    for key in temperature.keys():
        temperature[key] = int(input(f"Enter Temperature on {key} "))

    print(temperature)


def main():
    create_dictionary()


if __name__ == "__main__":
    main()
