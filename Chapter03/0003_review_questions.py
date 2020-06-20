'''
1)  Sequential Control Flow Statements:
        This refers to the line by line execution, in which
        the statements are executed sequentially, in the same
        order in which they appear in the program
    Decision Control Flow Statements:
        Depending on whether a condition is True or False,
        the decision structure may skip the execution of an
        entire block of statements or even execute one block
        of statements instead of another (if, if...else,
        if...elif...else)
    Loop Control Flow Statements:
        This is a control structure that allows the execution
        of a block of statements multiple times until a loop
        termination condition is met (for loop and while loop).
        Loop Control Flow Statements are also called Repetition
        statements or Iteration statements.

2)  for iteration_variable in sequence:
        statements()
    "for" and "in are keywords
    a colon should be present at the end
    there must be indentation for the statements

    for i in range(10):
        print(i)

3)  break allows you to exit the loop as a whole
    continue allows you to skip the current iteration

4)  if i > 10:
        print("bigger than 10")
    else:
        print("smaller than 10")

    if...else will test if a single condition is true
    and branch based upon the outcome of the test

    if i < 10 and i >= 5:
        print("i between 5 and 10")
    elif i < 5:
        print("i less than 5")
    else:
        print("i greater than 10")

    if...elif...else will test multiple conditions
    and branch based on the first test that returns
    true. If no test returns true, then the else branch
    is taken.

5)  for i in range(10):
        print(i)

    range allows one to generate a sequence of values.
    If only one argument is specified, range generates a
    sequence of values from 0 up to but not including the
    number specified in the first argument.
    If two arguments are specified, range will start the
    sequence from the first argument and end before the
    number indicated by the second argument.
    With three arguments, range starts at the first argument
    and ends before the second argument, with a difference
    between consecutive terms dictated by the third argument.

6)  You use try...except to handle exceptions that arise during
    the course of the program. Handling of exceptions ensures that
    the flow of the program does not get interrupted when an
    exception occurs which is done by trapping run-time errors.
    Handling of exceptions results in the execution of all
    the statements in the program.

7)  while Boolean_Expression:
        statements()

    while is a keyword. The colon should be present at the end.
    The statements that follow must be indented.

    i=0
    while i<10:
        print(i)
        i += 1

8)  Syntax errors occur when you enter in code that is not syntactically
    valid i.e. does not make sense within the constructs of the language
    An exception is an unwanted even that interrupts the normal flow
    of the program.

9)  try:
        statement_1
    except Exception_Name_1:
        statement_2
    except Exception_Name_2:
        statement_3
        ...
    else:e
        statement_4
    finally:
        statement_5

    try, except, else and finally are keywords. Colons should be
    present at the endof each statement with a keyword.
    The statements that follow within the block must be properly
    indented.
    else and finally are optional
'''

#Question 10
#Program to display Richter scale information
value = float(input("Please enter richter magnitude value"))
if value > 9.0:
    print("Causes unbelievable damage")
elif value > 8.0 and value <= 9.0:
    print("Causes major destruction")
elif value > 7.0 and value <= 8.0:
    print("Causes damage to most buildings")
elif value > 6.0 and value <= 7.0:
    print("Causes damage to well-built structures")
elif value > 5.0 and value <= 6.0:
    print("Causes damage to poorly constructed buildings")
elif value > 4.0 and value <= 5.0:
    print("Damage done to weak buildings")
elif value > 2.0 and value <= 4.0:
    print("Very rarely causes damage")
elif value > 1.0 and value <= 2.0:
    print("Microearthquakes not felt or rarely felt")
else:
    print("invalid input")

#Question 11
#Display Pascal's triangle
n = int(input("Enter the number of rows to print"))
temp = 0
for line in range(n):
    for i in range(line + 1):
        temp = 1
        k = i
        if k > line - i:
            k = line - k
        for j in range(k):
            temp = temp * (line - j)
            temp = temp // (j + 1)
        print(f"{temp}", end=" ")
    print("")

#Question 12
#Program to display pattern
n = int(input("Input number of rows"))
row_length = 20
for i in range(n):
    for j in range(i + 1):
        print(i + 1, end="")
    for j in range(row_length - 2 * (i + 1)):
        print(" ", end="")
    for j in range(i + 1):
        print(i + 1 - j, end="")
    print("")

#Question 13
#Add up even numbers between 100 and 200
#with while loop
number = 101
sum = 0
while number < 200:
    if number % 2 == 0:
        sum += number
    number += 1
print(f"The sum is {sum}")

#Question 14
#Sum up series

#a 1 + 1/2 + 1/3 + ... + 1/n
n = int(input("Enter number of terms in series"))
sum = 0
for i in range(1, n+1):
    sum += 1 / i
print(f"The sum is {sum}")

#b 1/1 + 2^2 / 2 + 3^3 /3 + ... + n^n / n
n = int(input("Enter number of terms in series"))
sum = 0
for i in range(1, n+1):
    sum += (i ** i) / i
print(f"The sum is {sum}")

#Question 15
#Find the depreciated value of an asset
amt = int(input("Enter purchase price"))
year = int(input("Enter years of service"))
dep = float(input("Enter depreciation as decimal"))

value = amt * (1 - dep) ** year
print(f"The depreciated value is {value}")

