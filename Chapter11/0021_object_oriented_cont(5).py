"""
Inheritance
    Inheritance enables new classes to receive or inherit
    variables and methods of existing classes. Inheritance is a
    way to express a relationship between classes.
    If you want to build a new class, which is already similar to one
    that already exists, then instead of creating a new class from
    scratch, you can reference the existing class and indicate what
    is different by overriding some of its behaviour or by adding
    some new functionality.
    A class that is used as th basis for inheritance is called a
    superclass or base class. A class that inherits from a base
    class is called a subclass or derived class.
    The terms parent class and child class are also used
    A derived class inherits variables and methods for its base
    class while adding additional variables and methods of its
    own.
    Inheritance easily enables reusing of existing code
    You should only use inheritance when there is an is-a relationship
    between the derived class and the base class

    You can create a derived class as follows
        class DerivedClassName(BaseClassName):
            <statement-1>
            ...
            <statement-n>
    To create a derived class, you add BaseClassName after the
    DerivedClassName within parenthesis, followed by a colon.
    The derived class is said to directly inherit from the
    listed base class

    Arbitrary expressions are also allowed, such as when the base
    class is defined in another module
        class DerivedClassName(modname.BaseClassName):
            <statement-1>
            ...
            <statement-1>
    All classes, except the special class object, are derived classes,
    even if they do not have a base class name.
    The object class is the only class that is not derived, since
    it is the base of the inheritance hierarchy.
    Classes without a base class name are implicitly derived directly
    from the class object.
    Leaving off the class object from the base class name is just
    shorthand for specifying that object is the base class

Accessing the Inherited Variables and Methods
    Execution of a derived class definition proceeds the same as
    for a base class.
    When the derived class object is constructed, the base class
    is also remembered.
    This is used for resolving variable and method attributes.
    If a requested attribute is not found in the derived class,
    the search proceeds to look in the base class
    The rule is applied recursively if the base class itself is
    derived from some other class.
    Inherited variables and methods are accessed just as if they
    had been created in the derived class itself

"""