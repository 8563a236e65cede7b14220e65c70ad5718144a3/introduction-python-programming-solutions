"""
Review Question 6
Input employee information: name, employee id, salary
Output employee ID and salary of specified employee given name
"""


def employee_input(dictionary):
    number = int(input("Enter Number of Employees "))
    for i in range(number):
        name = input("Enter employee name ")
        employee_id = input("Enter employee id ")
        salary = float(input("Enter employee salary "))
        dictionary[name] = [employee_id, salary]


def print_details(dictionary):
    name = input("Enter employee name to search ")

    if name in dictionary.keys():
        print(f"Employee ID: {dictionary[name][0]}")
        print(f"Salary: {dictionary[name][1]}")
    else:
        print("Employee not in database")


def main():
    dictionary = dict()
    employee_input(dictionary)
    print_details(dictionary)


if __name__ == "__main__":
    main()
