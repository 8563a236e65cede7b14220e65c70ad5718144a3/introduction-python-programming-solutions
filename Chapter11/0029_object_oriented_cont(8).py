"""
Method Resolution Order (MRO)
    Denotes the way Python resolves a method found in multiple base
    classes.
    MRO uses the C3 linearization algorithm to determine the order
    of the methods to be invoked in multiple inheritances while
    guaranteeing monotonicity
    MRO applies a set of rules to resolve the method order by
    constructing linearlization
        class_name.mro()

    L(Derived Class) = [Derived_Class] +
        merge(L(Base_Class_1), ..., L(Base_Class_n),
            [Base_Class_1, ..., Base_Class_n])
    The ordering of base classes of a derived class from the nearest
    base class to the furthest base class with the derived class
    preceding the base classes is called the local precedence of
    classes.
    The list of base classes as the larst argument in the merge
    part preserves the local precedence order of the base classes.

    An MRO is monotonic when the following is True:
        if Base_Class_1 precedes Base_Class_2 in the linearization of
        Derived_Class, then Base_Class_1 precedes Base_Class_2 in the
        linearization of any derived classes of Derived_Class itself.
    The construction of linearization for MRO should respect local
    precedence ordering and monotonicity

    The linearization result for a class is replaced by a list sequence.
    The presence of a class in the first position in multiple list
    sequences at the same time is called Head or good Head, but
    it should not appear in any other position.
    If a class is in the first position in one of the list sequence,
    and it is present in a different position, other than the first
    position itself, in the other list sequences, or if a class is not
    present in the first position at all in any of the list sequences,
    then it is called a Tail

"""