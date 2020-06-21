'''
Review Question 10
Program to find the largest of three numbers using functions
'''


def largest(a, b, c):
    return max(a, b, c)


def main():
    a = float(input("Enter first number\n"))
    b = float(input("Enter second number\n"))
    c = float(input("Enter third number\n"))

    print(f"The largest number from ({a},{b},{c}) is {largest(a, b, c)}")


if __name__ == "__main__":
    main()

