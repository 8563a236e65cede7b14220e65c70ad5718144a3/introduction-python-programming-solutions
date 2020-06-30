"""
Inheritance
    Single inheritance enables a derived class to inherit variables
    and methods from a single base class
    This includes the __init__() method
    If you do not define it in a derived class, you will get one from
    the base class.

Using super() Function and Overriding Base Class Methods
    In a single inheritance, the built-in super() function can
    be used to refer to base classes without naming them explicitly,
    thus making the code more maintainable.
    If you need to access the data attributes from the base class, in
    addition to the data attributes being specified in the derived
    class's __init__() method, then you must explicitly call the
    base class __init__() method using super(), since this will not
    happen automatially.
    If you do not need any data attributes from the base class, then
    there is no need to use super() function to invoke base class
    __init__() method.
    The syntax for using super() in derived class __init__() method
    definition looks like:
        super().__init__(base_class_parameter(s))
    It is used as below:
        class DerivedClassName(BaseClassName):
        def __init__(self, derived_class_parameter(s), base_class_parameter(s)):
            super().__init__(base_class_parameter(s))
            self.derived_class_instance_variable = derived_class_parameter

    Method overriding, in object-oriented programming, is a language
    feature that allows a derived class to provide its own implementation
    of a method that is already provided in base class.
    Derived classes may override methods of their base class.
    When you change the definition of parent methods, you can override
    them.
    These methods have the same name as those in the base class.
    The method in the derived class and the method in the base
    class each should have the same method signature.
    An overriding method in a derived class may, in fact, want to extend
    rather than simply replace the base class method of the same name.
    When constructing the base and derived claases, it is important
    to keep program design in mind, so that overriding does not produce
    unnecessary or redundant code

    Method signature refers to the method name, order and the total
    number of its parameters. Return types and thrown exceptions
    are not considered to be a part of the method signature.

    super() is also useful for accessing the base class methods
    that have been overriden in a derived class without explicitly
    specifying the base class name
        super().invoke_base_class_method(argument(s))
"""