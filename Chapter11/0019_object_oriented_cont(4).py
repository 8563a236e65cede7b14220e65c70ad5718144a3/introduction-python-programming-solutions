"""
Using Private Instance Variables and Methods
    Instance variables or methods, which can be accessed within the
    same class, and can't be seen outside, are called private instance
    variables or private methods.
    Since there is a valid use-case for class-only private members
    (namely to avoid name clashes of names with names defined by
    subclasses), there is support for such a mechanism, which is called
    name mangling.
    In Python, an identifier prefixed with a double underscore
    (e.g. __spam) and with no trailing underscores should be treated
    as private (whether it is a method or instance variable)
    Any identifier of the form __spam is textually replaced with
    _classname__spam, where classname is the current classname
    with a leading underscore(s) stripped
    Name mangling is intended to give classes an easy way to
    define "private" instance variables and methods, without
    having to worry about instance variables defined by derived
    classes
    Mangling rules are designed mostly to avoid accidents,
    it is still possible to access or modify a variable that is
    considered private
"""