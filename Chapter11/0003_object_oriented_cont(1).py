"""
Creating Objects in Python
    Object refers to a particular instance of a class where the
    object contains variables and methods defined in the class.
    Class objects support two kinds of operations: attribute
    references and instantiation.
    Attribute refers to any name (variables or methods) following
    a dot.
    The act of creating an object from a class is called instantiation
    The names in a class are referenced by objects and are called
    attribute references.
    There are two kinds of attribute references, data attributes and
    method attributes.
    Variables defined within the methods are called instance variables
    and are used to store data values.
    New instance variables are associated with each of the objects that
    are created for a class.
    These instance variables are also called data attributes
    Method attributes are methods inside a class and are referenced by
    objects of a class.

    To access a data attribute
        object_name.data_attribute_name
    Assign value to data attribute
        object_name.data_attribute_name = value
            value can be of integer, float, string types or other object
    Call method attribute
        object_name.method_attribute_name()
    Class instantiation
        object_name = ClassName(arg1, arg2, ..., argn)

    Whenever you call a method using an object, the object itself
    is automatically passed in as the first parameter to the self
    parameter variable.
    The remaining parameter variables must be supplied as arguments
    in the calling method.

The Constructor Method
    First method definition of a class
        def __init__(self, par1, ..., parn):
            statement(s)

    The __init()__ method defines and initializes the instance
    variables.
    It is invoked as soon as an object of a class in instantiated.
    __init()__ method for a newly created object is automatically
    executed with all of its parameters.
    The parameters of the __init__() method are initialized with the
    arguments that you had passed during instantiation of the class
    object
    Class methods that begin with a double underscore __ are
    called special methods as they have a special meaning.
"""