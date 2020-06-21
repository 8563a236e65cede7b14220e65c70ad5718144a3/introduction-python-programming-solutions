'''
Review Question 9
Program to perform arithmetic operations using functions
'''


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def main():
    while True:
        command = input("Enter command (add, sub, mul, div). Enter \"done\" to exit\n")

        if command == "done":
            break
        else:
            a = float(input("Enter first number\n"))
            b = float(input("Enter second number\n"))

            if command == "add":
                c = add(a, b)
                print(f"Sum of {a} and {b} = {c}")
            elif command == "sub":
                c = sub(a, b)
                print(f"Difference of {a} and {b} = {c}")
            elif command == "mul":
                c = mul(a, b)
                print(f"Product of {a} and {b} = {c}")
            elif command == "div":
                try:
                    c = div(a, b)
                except ZeroDivisionError:
                    print("Division by zero!")
                else:
                    print(f"Quotient of {a} and {b} = {c}")
            else:
                print("Invalid option")


if __name__ == "__main__":
    main()
