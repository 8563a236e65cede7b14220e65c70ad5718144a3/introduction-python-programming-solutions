#Program 3.1
#Print if number is positive
number = int(input("Enter a number"))
if number >= 0:
    print(f"The number entered by the user is a positive number")

#Program 3.2
#Read luggage weight and charge tax
weight = int(input("How many pounds does your suitcase weigh?"))
if weight > 50:
    print(f"There is a $25 surcharge for heavy luggage")
    print(f"Thank you")

#Program 3.3
#Program to find if given number is odd or even
number = int(input("Enter a number"))
if number % 2 == 0:
    print(f"{number} is Even number")
else:
    print(f"{number} is Odd number")

#Program 3.4
#Find the greater of two numbers
number_1 = int(input("Enter the first number"))
number_2 = int(input("Enter the second number"))
if number_1 > number_2:
    print(f"{number_1} is greater than {number_2}")
else:
    print(f"{number_2} is greater than {number_1}")

#Program 3.5
#Print grade
score = float(input("Enter your score"))
if score < 0 or score > 1:
    print("Wrong Input")
elif score >= 0.9:
    print("Your Grade is \"A\"")
elif score >= 0.8:
    print("Your Grade is \"B\"")
elif score >= 0.7:
    print("Your Grade is \"C\"")
elif score >= 0.6:
    print("Your Grade is \"D\"")
else:
    print("Your Grade is \"F\"")

#Program 3.6
#Display Cost of Each Type of Fruit
fruit_type = input("Enter the Fruit Type:")
if fruit_type == "Oranges":
    print("Oranges are $0.59 a pound")
elif fruit_type == "Apples":
    print("Apples are $0.32 a pound")
elif fruit_type == "Bananas":
    print("Bananas are $0.48 a pound")
elif fruit_type == "Cherries":
    print("Cherries are $3.00 a pound")
else:
    print(f"Sorry, we are out of {fruit_type}")

#Program 3.7
#Check if a leap year
year = int(input("Enter a year"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is not a Leap Year")
    else:
        print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

#Program 3.8
#While loop
i = 0
while i < 10:
    print(f"Current value of i is {i}")
    i = i + 1

#Program 3.9
#Find average of n Natural Numbers
number = int(input("Enter a number up to which you want to find the average"))
i = 0
sum = 0
count = 0
while i < number:
    i = i + 1
    sum = sum + i
    count = count + 1
average = sum / count
print(f"The average of {number} natural numbers is {average}")

#Program 3.10
#GCD of Two Positive Numbers
m = int(input("Enter first positive number"))
n = int(input("Enter second positive number"))
if m == 0 and n == 0:
    print("Invalid Input")
if m == 0:
    print(f"GCD is {n}")
if n == 0:
    print(f"GCD is {m}")
while m != n:
    if m > n:
        m = m - n
    if n > m:
        n = n - m
print(f"GCD of two numbers is {m}")

#Program 3.11
#Find the sum of digits in a number
number = int(input("Enter a number"))
result = 0
remainder = 0;
while number != 0:
    remainder = number % 10
    result = result + remainder
    number = int(number / 10)
print(f"The sum of all digits is {result}")

#Program 3.12
#Display Fibonacci Sequences up to nth Term
nterms = int(input("How many terms?"))
current = 0
previous = 1
count = 0
next_term = 0
if nterms <= 0:
    print("Please enter a positive number")
elif nterms == 1:
    print("Fibonacci sequence")
    print("0")
else:
    print("Fibonacci sequence")
    while count < nterms:
        print(next_term)
        current = next_term
        next_term = previous + current
        previous = current
        count += 1

#Program 3.13
#Check for largest number
largest_number = int(input("Enter the largest number initially"))
check_number = input("Enter a number to check whether it is the largest or not")
while check_number != "done":
    if largest_number > int(check_number):
        print(f"Largest Number is {largest_number}")
    else:
        largest_number = int(check_number)
        print(f"Largest Number is {largest_number}")
    check_number = input("Enter a number to check whether it is largest or not")

'''
    Range function
    range([start,] stop [,step])
'''

#Program 3.14
#Demonstrate for loop using range()
print("Only \"stop\" argument value specified in range function")
for i in range(3):
    print(f"{i}")
print("Both \"start\" and \"stop\" argument values specified in range function")
for i in range(2, 5):
    print(f"{i}")
print("All three arguments \"start\", \"stop\" and \"step\" specified in range function")
for i in range(1, 6, 3):
    print(f"{i}")

#Program 3.15
#Iterate through string
for each_character in "Blue":
    print(f"Iterate through character {each_character} in the string \"Blue\"")

#Program 3.16
#Find sum of all odd and even numbers
number = int(input("Enter a number"))
even = 0
odd = 0
for i in range(number):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
print(f"Sum of Even numbers are {even} and Odd numbers are {odd}")

#Program 3.17
#Factorial
number = int(input("Enter number"))
factorial = 1
if number < 0:
    print("Factorial doesn't exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
print(f"The factorial of number {number} is {factorial}")

#Program 3.18
#Infinite while loop and break
n = 0
while True:
    print(f"The latest value of n is {n}")
    n = n + 1

n = 0
while True:
    print(f"The latest value of n is {n}")
    n = n + 1
    if n > 5:
        print(f"The value of n is greater than 5")
        break

#Program 3.19:
#Check whether a number is prime
number = int(input("Enter a number > 1:"))
prime = True
for i in range(2, number):
    if number % i == 0:
        prime = False
        break
if prime:
    print(f"{number} is a prime")
else:
    print(f"{number} is not a prime")

#Program 3.20
#continue statement
n = 10
attempt = 0
while n > 0:
    print(f"The current value of number is {n}")
    if n == 5:
        print(f"Breaking at {n}")
        n = 10
        attempt = attempt + 1
        if attempt == 2:
            break
        continue
    n = n - 1

#Program 3.21
#Check for ValueError Exception
while True:
    try:
        number = int(input("Please enter a number:"))
        print(f"The number you have entered is {number}")
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

#Program 3.22
#Check for ZeroDivisionError
x = int(input("Enter value for x:"))
y = int(input("Enter value for y:"))

try:
    result = x / y
except ZeroDivisionError:
    print("Division by Zero!")
else:
    print(f"Result is {result}")
finally:
    print("Executing finally clause")

#Program 3.23
#Read list of numbers until user enters "done". Use try and except
#to detect if user does not enter number. Display Total, Count and Average
total = 0
count = 0
while True:
    num = input("Enter a number:")
    if num == "done":
        print(f"Sum of all the entered numbers is {total}")
        print(f"Count of total numbers entered {count}")
        print(f"Average is {total / count}")
        break
    else:
        try:
            total += float(num)
        except:
            print("Invalid input")
            continue
        count += 1
