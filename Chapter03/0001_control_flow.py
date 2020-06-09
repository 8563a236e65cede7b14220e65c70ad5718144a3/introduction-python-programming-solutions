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
