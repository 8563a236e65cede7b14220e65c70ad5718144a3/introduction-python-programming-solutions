'''
1)  - Arithmetic Operators
        - + Addition
        - - Subtraction
        - * Multiplication
        - / Division
        - ** Exponent
        - // Floor division
    - Assignment Operators
        - = Assignment
        - += Addition Assignment
        - -= Subtraction Assignment
        - *= Multiplication Assignment
        - /= Division Assignment
        - **= Exponentiation Assignment
        - %= Remainder Assignment
    - Comparison Operators
        - == Equal to
        - != Not Equal To
        - > Greater than
        - < Less than
        - >= Greater than or equal to
        - <= Less than or equal to
    - Logical Operators
        - and Logical AND
        - or Logical OR
        - not Logical NOT
    - Bitwise Operators
        - & Binary AND
        - | Binary OR
        - ^ Binary XOR
        - ~ Binary Ones Complement
        - << Binary Left Shift
        - >> Binary Right Shift

2)  A variable is a named placeholder to hold any type of data, which
    the program can use to assign and modify during the course of execution.
    You assign a value with the following syntax: variable_name = expression.

3)  Binary Left Shift - The left operands value is moved left by the number
    of bits specified by the right operand.
        - 60 << 2 = 240
    Binary Right Shift - The left operand's value is moved right by the number
    of bits specified by the right operand.
        - 60 >> 2 = 15

4)  Operator precedence determines the way in which operators are parse with
    respect to each other. Operators with higher precedence become the operands
    of operators with lower precedence.
    Associativity determines the way in which operators of the same precedence are
    parsed. Almost all the operators have left-to-right associativity.
    From highest to lowest precedence:
    Operators                           Meaning
    ()                  Parentheses
    **                  Exponent
    +x,-x,~x            Unary plus, Unary minus, Bitwise NOT
    *,/,//,%            Multiplication, Division, Floor Division, Modulus
    +,-                 Addition, Subtraction
    <<,>>               Bitwise shift operators
    &                   Bitwise AND
    ^                   Bitwise XOR
    |                   Bitwise OR
    ==,!=,>,>=,<,<=     Comparisons
    is,is not,in,not in Identity, Membership operators
    not                 Logical NOT
    and                 Logical AND
    or                  Logical OR

5)  Assignment operators are used for assigning the values generated after
    evaluating the right operand to the left operand. Assignment operation
    always works from left to right.
        - z = p + q
        - z += p
        - z -= p
        - z *= p
        - z /= p
        - z **= p
        - z //= p
        - z %= p

6)  Use the input() function to read data from the keyboard. Everything
    is read as a string, so you will need to cast to other types if need
    be

7)  Type conversions allow you to explicitly cast, or convert a variable from
    one type to another.
        - float_to_int = int(3.5)
        - int_to_float = float(4)
        - int_to_string = str(8)
        - ascii_to_char = chr(100)
        - complex_with_number = complex(5,8)

8)  Data types specify the type of data like numbers and characters to be
    stored and manipulated within a program. Basic data types of Python are
        - Numbers
        - Boolean
        - Strings
        - None
'''

#Question 9
#Arithmetic operations on two input integers
int1 = int(input("Enter first integer"))
int2 = int(input("Enter second integer"))
print(f"int1 = {int1}, int2 = {int2}")
print(f"int1 + int2 = {int1 + int2}")
print(f"int1 - int2 = {int1 - int2}")
print(f"int1 * int2 = {int1 * int2}")
print(f"int1 / int2 = {int1 / int2}")

#Question 10
#Average of three input marks
mark1 = float(input("Enter mark 1"))
mark2 = float(input("Enter mark 2"))
mark3 = float(input("Enter mark 3"))
print(f"mark1 = {mark1}, mark2 = {mark2}, mark3 = {mark3}")
print(f"Average mark = {(mark1 + mark2 + mark3) / 3}")

#Question 11
#Kilogram to pound conversion
lb_per_kg = 2.20462
kg = float(input(f"Enter number of kilograms:"))
print(f"{kg} kgs is {kg * lb_per_kg} lbs")

#Question 12
#Surface area of prism
side_a = int(input("Enter the length of side A"))
side_b = int(input("Enter the length of side B"))
side_c = int(input("Enter the length of side C"))
surface_area = 2 * side_a * side_b + 2 * side_b * side_c + 2 * side_a * side_c
print(f"side_a = {side_a}, side_b = {side_b}, side_c = {side_c}")
print(f"Surface area = {surface_area}")

#Question 13
#Speed of a plane
distance = 395000
time = 9000
speed = distance / time
print(f"distance = {distance}m, time = {time}s")
print(f"speed = {speed} m.s^-1")

#Question 14
#Length of time to empty a pool
length = 12
width = 7
depth = 2
flow = 17

volume = length * width * depth
time = volume / flow

print(f"length = {length}, width = {width}, depth = {depth}, flow = {flow}")
print(f"volume = {volume}, time to empty = {time}s")

#Question 15
#Centigrade to fahrenheit converter
centigrade = float(input("Enter temperature in centigrade"))
fahrenheit = centigrade * 9 / 5 + 32
print(f"{centigrade} centigrade is {fahrenheit} fahrenheit")

#Question 16
#Number of seconds in a day
sec_per_min = 60
min_per_hour = 60
hrs_per_day = 24
sec_per_day = hrs_per_day * min_per_hour * sec_per_min
print(f"Seconds per day = {sec_per_day}s")

#Question 17
#Acceleration of car
v_initial = 0
v_final = 10
time = 20
acc = (v_final - v_initial) / time
print(f"Car acceleration: {acc} m.s^-2")
