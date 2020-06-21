'''
1)  A function is a block of statements that are grouped together
    and given a name. They can be executed any number of times by
    using the given name to invoke it in other parts of the program.
    Advantages
        Reduce duplication of code
        Improve clarity of code
        Reuse of code

2)  Built-in functions are functions that are built into the Python
    Interpreter. User-defined functions are functions that the user
    creates through a function definition within the code, that can
    be called in other parts of the code by name. It is not defined
    within the Python Interpreter at outset.

3)  def function_name(parameter_1, parameter_2, ..., parameter_n):
        statements()

    To invoke within main
        def main():
            function_name(argument_1, argument_2, ..., argument_n)

        if __name__ == "__main__":
            main()

4)  Built-in functions are functions that are built into the Python
    Interpreter and are always available
        abs(-3)
        min(1,2,3,4,5)
        max(4,5,6,7,8)
        divmod(5,2)
        pow(3,2)
        len("Japan")

5)  A variable is a global variable if its value is accessible and
    modifiable throughout your program. Global variables have a
    global scope. A variable that is defined inside a function
    definition is a local variable. The local variable is created
    and destroyed every time the function is executed, and it cannot
    be accessed by any code outside the function definition

6)  *args and **kwargs allows you to pass a variable number of
    arguments to the calling function. The user does not know in
    advance how many arguments will be passed to the calling function.
    *args as a parameter in a function definition allows you to pass
    a non-keyworded, variable length tuple argument list to the
    calling function. **kwargs as a parameter in a function definition
    allows you to pass keyworded, variable length dictionary argument
    list to the calling function. *args must come after all the
    positional parameters and **kwargs must come right at the end

    def print_args(*args, **kwargs):
        for arg in args:
            print(arg)
        for kw in kwargs:
            print(kw, ":", kwargs[kw])

    def main():
        print_args(1,"a",2,"b",a="1",b="2")

    if __name__ == "__main__":
        main()

7)  A function can return multiple values separated by a comma
    which by default is constructed as a tuple. When calling
    function receives a tuple from the function definition,
    it is common to assign the result to multiple variables
    by specifying the same number of variables on the left-hand
    side of the assignment as they were returned from the function
    definition

        def multiple_return():
            a = 1
            b = 2
            return a, b

        def main():
            a, b = multiple_return()
            print(f"a={a} b={b}")

        if __name__ == "__main__":
            main()

8)  There are tools to process docstrings into online documents or
    printed documentation
'''