#################################
#     Arithmetic Operators      #
#################################
p = 2
q = 3

#Addition
p + q   #5
#Subtraction
p - q   #-1
#Multiplication
p * q   #6
#Division
q / p   #1.5
#Modulus
q % p   #1
#Exponent
p ** q  #8
#Floor division
9 // 2  #4

#Further examples
10 + 35     #45
-10 + 35    #25
4 * 2       #8
4 ** 2      #16
45 / 10     #4.5
45 // 10.0  #4.0
2025 % 10   #5
2025 // 10  #202
#################################

#################################
#     Assignment Operators      #
#################################
#Basic assignment
x = 5
x = x + 1
x

x += 1
x

#Name error
z = z + 1

z = 0
x = z + 1
x

#Examples
p = 10
q = 12
q += p
q
q *= p
q
q /= p
q
q %= p
q
q **= p
q
q //= p
q

#Note, no autoincrement ++ and autodecrement -- operators
#################################

#################################
#     Comparison Operators      #
#################################
#Examples
10 == 12
10 != 12
10 < 12
10 > 12
10 <= 12
10 >= 12
"P" < "Q"
"Aston" > "Asher"
True == True
#################################

#################################
#     Logical Operators         #
#################################
p = True
q = False
p and q
p or q
not p

#Examples
True and False
True or False
not(True) and False
not(True and False)
(10 < 0) and (10 > 2)
(10 < 0) or (10 > 2)
not(10 < 0 or 10 > 2)
#################################

#################################
#     Bitwise Operators         #
#################################
p = 60
q = 13

#Binary AND
p & q

#Binary OR
p | q

#Binary XOR
p ^ q

#Binary Ones Complement
~p

#Binary Left Shift
p << 2

#Binary Right Shift
p >> 2