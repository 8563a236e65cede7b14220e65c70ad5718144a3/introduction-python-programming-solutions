"""
Review Question 13
Create a list of numbers 1-100 that are either
divisible by 5 or 6
"""


def create_list():
    my_list = list()
    for i in range(1,101):
        if i % 5 == 0 or i % 6 == 0:
            my_list.append(i)
    return my_list


def main():
    my_list = create_list()
    print(f"The list is:\n{my_list}")


if __name__ == "__main__":
    main()


