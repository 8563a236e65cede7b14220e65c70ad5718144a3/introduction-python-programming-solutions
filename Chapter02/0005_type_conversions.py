#Program 2.6
#Int
float_to_int = int(3.5)
string_to_int = int("1")    #Number treated as string
print(f"After Float to Integer Casting the result is {float_to_int}")
print(f"After String to Integer Casting the result is {string_to_int}")

numerical_value = input("Enter a number")
numerical_value

numerical_value = int(input("Enter a number"))
numerical_value

#Program 2.7
#float
int_to_float = float(4)
string_to_float = float("1")    #Number treated as string
print(f"After Integer to Float Casting the result is {int_to_float}")
print(f"After String to Float Casting the result is {string_to_float}")

#Program 2.8
#str function
int_to_string = str(8)
float_to_string = str(3.5)
print(f"After integer to string casting the result is {int_to_string}")
print(f"After float to string casting the result is {float_to_string}")

#Program 2.9
#chr() function
ascii_to_char = chr(100)
print(f"Equivalent Character for ASCII value of 100 is {ascii_to_char}")

#Program 2.10
#complex() function
complex_with_string = complex("1")
complex_with_number = complex(5, 8)
print(f"Result after using string in real part {complex_with_string}")
print(f"Result after using numbers in real and imaginary part {complex_with_number}")

#Program 2.11
#ord() function
unicode_for_integer = ord("4")
unicode_for_alphabet = ord("Z")
unicode_for_character = ord("#")
print(f"Unicode code point for integer value of 4 is {unicode_for_integer}")
print(f"Unicode code point for alphabet 'Z' is {unicode_for_alphabet}")
print(f"Unicode code point for character '#' is {unicode_for_character}")

#Program 2.12
#hex casting
int_to_hex = hex(255)
print(f"After Integer to Hex Casting the result is {int_to_hex}")

#Program 2.13
#octal casting
int_to_oct = oct(255)
print(f"After Integer to Hex Casting the result is {int_to_oct}")

#The type function
type(1)
type(6.4)
type("A")
type(True)

#is and is not operator
x = "Seattle"
x = "Seattle"
y = "Seattle"
x is y