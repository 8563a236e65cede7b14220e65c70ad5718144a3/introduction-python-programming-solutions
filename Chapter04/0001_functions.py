'''
Functions
    Functions are used when you have a block of statements
    that needs to be executed multiple times within the
    program
    Functions can either be built-in functions or user-defined

Built-In functions
    abs(x)                      absolute value of a number
    min(arg1, arg2, ...)        minumum of arguments
    max(arg1, arg2, ...)        maximum of arguments
    divmod(a, b)                returns quotient and remainder of
                                arguments
    pow(x, y)                   x ** y
    len(s)                      returns length or number of items
                                in an object
'''
abs(-3)
min(1,2,3,4,5)
max(4,5,6,7,8)
divmod(5,2)
divmod(8.5, 3)
pow(3,2)

'''
Commonly Used Modules
    Reusable libraries of code having a .py extension
    Implements a group of methods and statements
    Use the import statement to import modules
        import module_name
    Using a function defined in a module
        module_name.function_name()
'''
import math
print(math.ceil(5.4))
print(math.sqrt(4))
print(math.pi)
print(math.cos(1))
math.factorial(6)
math.pow(2,3)

#List module contents
dir(math)

#Help
help(math.gcd)

'''
Random library
'''
import random
print(random.random())
print(random.randint(5,10)) #inclusive of boundaries

'''
Package management
    apt install python3-pip
    pip3 install arrow
    conda install arrow - when using anaconda
'''
import arrow
a = arrow.utcnow()
a.now()

'''
Function definitions and calling
    def function_name(parameter_1, ..., parameter_n):
        statements()
        
    Function consists of def keyword followed by the name of
    the function, a list of parameters, a colon and a 
    block of statements
    
    Calling a function
    function_name(argument_1, argument_2, ..., argument_n)
'''
