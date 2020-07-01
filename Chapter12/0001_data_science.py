"""
Introduction to Data Science
    A data scientist can be thought of as someone who knows more
    about statistics than a computer scientist and more about computer
    science than a statistician

Functional Programming
    Python supports a form of programming called Functional Programming
    (FP) that involves programming with functions where functions can
    be passed, stored, and returned.
    FP decomposes a problem into a set of functions
    The gist of FP is that every function is understood solely in terms
    of its inputs and its outputs

Lambda
    Small anonymous functions can be created with the lambda keyword
    Lambda functions are created without using def keyword and without
    a function name
    They are syntactically restricted to a single expression
        lambda argument_list: expression
    Here lambda is a keyword, argument_list is a comma separated list
    of arguments, and expression is an arithmetic expression using
    these argument lists
    A colon separates both argument_list and expression
    No need to enclose argument_list within brackets
"""
addition_operation = lambda a, b: a + b
addition_operation(100, 8)

"""
Iterators
    Iterators are an important foundation for writing functional-style
    programs.
    Iteration is a general term for taking each item of something, 
    one after another.
    An iterable is an object that has an __iter__() method that returns
    an iterator. So an iterable is an object you can get an iterator
    from. Lists, dictionaries, tuples and strings are iterable in
    Python.
    An iterator is an object with a __next__() method. Whenever you use
    a for loop, the __next__() method is called automatically to get
    each item from the iterator, thus going through the process
    of iteration.
    Iterators are stateful, meaning once you have consumed an item
    from them, it's gone
"""
phone = "jio"
it_object = iter(phone)
type(it_object)

next(it_object)
next(it_object)
next(it_object)
next(it_object) #StopIteration

"""
Generators
    Generators are a special class of functions that simplify the task
    of writing iterators.
    Regular functions compute a value and return it, but generators
    return an iterator that returns a stream of values.
    Generators can be thought of as resumable functions
    A generator function does not include a return statement
    Any function containing a yield keyword is a generator function
    Difference between yield and return is that on reaching a yield
    the generator's state of execution is temporarily suspended and
    local variables are preserved.
    Generator functions are used for calculating large sets of
    results where you do not know if you are going to need all results
"""


def generate_ints(N):
    for i in range(N):
        yield i

gen = generate_ints(3)
gen
next(gen)
next(gen)
next(gen)
next(gen)

"""
List Comprehensions
    List comprehensions provide a concise way to create lists. Common
    applications of list comprehensions are to make new lists where
    each element is the result of some operation applied to each member
    of another sequence or iterable or to create a subsequence of those
    elements that satisfy a certain condition.
    
    list_variable = [variable[expression] for variable in input [predicate]]
    
    A list comprehension consists of brackets containing a variable or
    expression followed by a for clause, then predicate True or False
    using an if clause.
    The components expression and predicate are optional.
    The new list resulting from evaluation the expression in the context
    of the for and if classes that follow it will be assigned to
    list_variable
    The variable represents members of input
    The order of execution in a list comprehension is
        If the if condition is not specified, then the Middle Part and
        First Part gets executed
        If the if condition is specified, then the Middle Part, Last
        Part and First Part gets executed.
"""
hardy_ramanujan = []
for number in "1729":
    hardy_ramanujan.append(number)
hardy_ramanujan
hardy_ramanujan = []

hardy_ramanujan = [number for number in "1729"]
hardy_ramanujan

"""
    Comprehensions can be thought of as a compact for of a
    for loop. In the list comprehension, the variable number indicates
    the item that will be inserted into the list at each step of
    the for loop.
    In the for loop, the iterating variable number iterates through
    each character of the string "1729" 
"""
display_upper_case = [each_char.upper() for each_char in "farrago"]
display_upper_case

squares = [x**2 for x in range (1, 10)]
squares

even_square = [x ** 2 for x in range(1, 10) if x % 2 == 0]
even_square

words = [each_word for each_word in input().split()]
words
words.sort()
print(" ".join(words))

"""
JSON and XML in Python
    JSON (JavaScript Object Notation) and XML (EXtensible Markup 
    Language) standards are commonly used for transmitting data in
    web applications

Using JSON with Python
    JSON is a lightweight text-based data-interchange format.
    It is simple for humans to read and write and easy enough
    for machines to parse and generate.
    JSON is a text format that is completely language independent,
    but uses conventions that are familiar to programmers of
    various languages.
    Built-in data types are
        strings
        numbers
        booloeans
        null,
        objects
        arrays
    JSON is built on two structures:
        A collection of string: value properties. In various languages
        this is realized as an object, record, struct, dictionary,
        hash table, keyed list or associative array
        An ordered list of values. In most languages, this is realized
        as an array, vector, list or sequence.
    
    JSON objects can have one or more properties, each of which is a
    string:value pair.
    An object begins with a left brace ({) and ends with a right 
    brace (}), and the string:value pairs are separated by a comma.
    Each string is followed by a colon, and the string: value
    pairs are separated by a comma.
    Conventionally, a space is used after the colon
    In JSON, an array is an ordered collection of values. An array
    begins with a left bracket ([) and ends with a right bracket (])
    Values are separated by a comma (,)
    In JSON, a value can be a string in double quotes, a number, true
    or false or null, an object or an array. 
    These structures can be nested
    In JSON, it is required to use double quotes around string
    properties and single quotes are not valid
    In JSON, a number is very much like a Python number, except that
    the octal and hexadecimal formats are not used
    You can validate JSON using an application like JSONLint
    
    json module has dump() and dumps() for serializing and load() 
    for deserializing
    
"""