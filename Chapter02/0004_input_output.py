#Input
person = input("What is your name")
person

#Output
print("Hello World!!")

#str.format
#Program 2.1
country = input("Which country do you live in?")
print("I live in {0}".format(country))

#Program 2.2
a = 10
b = 20
print("The values of a is {0} and b is is {1}".format(a, b))
print("The values of b is {1} and a is is {0}".format(a, b))

print("Give me {ball} ball".format(ball = "tennis"))

#f-strings
#Program 2.3
country = input("Which country do you live in?")
print(f"I live in {country}")

#Program 2.4
radius = int(input("Enter the radius of a circle"))
area_of_a_circle = 3.1415 * radius * radius
circumference_of_a_circle = 2 * 3.1415 * radius
print(f"Area = {area_of_a_circle} and Circumference={circumference_of_a_circle}")

#Program 2.5
number_of_days = int(input("Enter number of days"))
number_of_years = int(number_of_days / 365)
number_of_weeks = int(number_of_days % 365 / 7)
remaining_number_of_days = int(number_of_days % 365 % 7)
print(f"Years = {number_of_years}, Weeks = {number_of_weeks}, Days = {remaining_number_of_days}")
