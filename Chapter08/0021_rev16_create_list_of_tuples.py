"""
Review Question 16
Accept a range and create a list of tuples within
that range with the first element as the number and
the second element as the square of the number
"""


def create_squares(n):
    number_list = list()
    for i in n:
        number_list.append((i, i*i))
    return number_list


def main():
    number = int(input("Enter a number "))
    result = create_squares(range(1, number + 1))
    print(f"(i, i*i)\n{result}")


if __name__ == "__main__":
    main()
