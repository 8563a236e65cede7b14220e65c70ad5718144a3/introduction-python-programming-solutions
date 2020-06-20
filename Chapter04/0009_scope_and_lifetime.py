'''
Program 4.7
Demonstrate Scope of Variables

You can nest a function definition within another function definition
    inner function can "inherit" the arguments and variables of its
    outer function definition
'''

test_variable = 5

def outer_function():
    test_variable = 60

    def inner_function():
        test_variable = 100
        print(f"Local variable value of {test_variable} having local scope to inner function is displayed")

    inner_function()

    print(f"Local variable value of {test_variable} having local scope to outer function is displayed")

outer_function()

print(f"Global variable value of {test_variable} is displayed")
