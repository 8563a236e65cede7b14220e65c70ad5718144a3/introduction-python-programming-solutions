'''
Review Question 12
Area of a pentagon with functions
Let a be the side length and A be the area of a regular
pentagon. Then
    A = 0.25 * sqrt(5(5+2*sqrt(5))) * a * a
'''


import math

def area(a):
    return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a * a


def main():
    a = float(input("Enter side length\n"))
    print(f"Area of pentagon with side length a = {area(a)}")


if __name__ == "__main__":
    main()


