"""
Review Question 7
Create a list of 10 random integers and then sort list
into odd_list and even_list which contain the odd and
even values respectively
"""
import random

def create_random_list(n):
    random_list = list()
    for i in range(n):
        random_list.append(random.randint(0, 100))
    return random_list


def sort_odd_even(integer_list):
    odd_list = list()
    even_list = list()
    for item in integer_list:
        if item % 2 == 0:
            even_list.append(item)
        else:
            odd_list.append(item)
    return odd_list, even_list


def main():
    random_list = create_random_list(10)
    odd_list, even_list = sort_odd_even(random_list)
    print(f"The list is\n{random_list}")
    print(f"The odd list is\n{odd_list}")
    print(f"The even list is\n{even_list}")


if __name__ == "__main__":
    main()


