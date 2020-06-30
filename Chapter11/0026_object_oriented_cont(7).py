"""
Multiple Inheritances
    A derived class definition with multiple base classes looks like
        class DerivedClassName(Base_1, Base_2, Base_3):
            <statement-1>
            ...
            <statement-N>
    In the simplest case, the search for attributes inherited from a
    parent class is depth-first, left-to-right, not searching twice
    in the same class where there is an overlap in the hierarchy.
    If an attribute is not found in DerivedClassName, it is searched
    for in Base_1, then (recursively) in the base classes of Base_1,
    and if it was not found there, it would be searched for in
    Base_2 and so on.
    Even though multiple inheritances are available in Python, it is
    not highly encouraged to use it as it is hard and error prone

    You can call the base class method directly using Base Class name
    itself without using the super() function
        BaseClassName.methodname(self, arguments)
    Use issubclass() to check class inheritance
        issubclass(DerivedClassName, BaseClassName)
    
"""