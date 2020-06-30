"""
Objects as Return Values
    It is important to note that everything in Python is an object,
    including classes
    Python does not include any primitive, unboxed values
    Anything that can be used as a value (int, str, float, functions,
    modules, etc.) is implemented as an object
    The id() function is used to find the identity of the location of the
    object in memory.
        id(object)
    The function returns the "identity" of an object
    This is an integer (or long integer), which is guaranteed
    to be unique and constant for this object during its lifetime.
    Two objects with non-overlapping lifetimes may have the same id()
    value

    You can check whether an object is an instance of a given class
    or not by using the isinstance() function
        isinstance(object, classinfo)
    Where object is an object instance and classinfo can be a class,
    or a tuple containing classes, or other tuples. The isinstance()
    function returns a Boolean stating whether the object is an
    instance or subclass of another object
"""