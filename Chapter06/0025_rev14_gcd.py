"""
Review Question 14
Write a program to find the greatest common denomiantor
of five numbers
"""
import math


def main():
    my_list = list()
    gcd_list = list()
    for i in range(5):
        my_list.append(int(input(f"Enter number {i+1}\n")))

    for i in range(5):
        for j in range(i+1, 5):
            gcd_list.append(math.gcd(my_list[i], my_list[j]))

    print(f"GCD = {min(gcd_list)}")


if __name__ == "__main__":
    main()


