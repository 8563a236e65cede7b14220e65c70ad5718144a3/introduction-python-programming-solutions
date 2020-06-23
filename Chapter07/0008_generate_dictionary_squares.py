"""
Program 7.7
Generate a Dictionary That Contains (i: i*i)
Such that i Is a Number Ranging from 1 to n
"""


def main():
    number = int(input("Enter a number\n"))
    create_number_dict = dict()
    for i in range(1, 1 + number):
        create_number_dict[i] = i * i
    print("The generated dictionary of the form (i: i*i) is")
    print(create_number_dict)


if __name__ == "__main__":
    main()
