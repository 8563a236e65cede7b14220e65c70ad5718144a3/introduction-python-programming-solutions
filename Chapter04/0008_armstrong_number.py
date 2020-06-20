'''
Program 4.6
Check if a three digit number is an Armstrong
number
'''

user_number = int(input("Enter a 3 digit positive number to check for Armstrong number"))

def check_armstrong_number(number):
    result = 0
    temp = number
    while temp != 0:
        last_digit = temp % 10
        result += pow(last_digit, 3)
        temp = int(temp / 10)
    if number == result:
        print(f"Entered number {number} is an Armstrong number")
    else:
        print(f"Entered number {number} is not an Armstrong number")

def main():
    check_armstrong_number(user_number)

if __name__ == "__main__":
    main()

