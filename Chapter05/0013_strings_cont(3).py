"""
Formatting strings
    %-formatting
    str.format()
    f-strings

    %-formatting
        limited in types it supports
            int
            str
            doubles
        traps
"""
almanac = "nostradamus"
"seer: %s" % almanac

almanac = ("nostradamus", 1567)
"seer: %s" % almanac #TypeError

"""
Passing Multiple values not supported in % formatting

str.format was created to address some of the problems
of %-formatting
    very verbose however
"""
value = 4 * 20
"The value is {value}.".format(value=value)
"The value is {}.".format(value)

f"The value is {value}"

"""
Backslashes may not appear inside the expression portions of
f-strings, so you cannot use them. Backslashes may occur inside
the string portions of an f-string
"""
f'{\'quoted string\'}'  #Syntax Error
f'{"quoted string"}'

"""
Format Specifiers
The syntax for f-string formatting operations is
    f'string_statements {variable_name[:{width}.{precision}]}'
        string_statement is a string consisting of a sequence
        of characters
        width and precision are optional
        if specified, both should be included within curly braces
        variable_name should be separated with a colon
"""
width = 10
precision = 5
value = 12.34567
f"result: {value:{width}.{precision}}"
f"result: {value:{width}}"
f"result: {value:.{precision}}"

"""
Escape sequences
    \       Break a Line into Multiple Lines while ensuring the
            continuation of the line
    \\      Inserts a backslash character in the string
    \'      Inserts a Single Quote character in the string
    \"      Inserts a Double Quote character in the string
    \n      Inserts a New Line in the string
    \t      Inserts a tab in the string
    \b      Inserts a backspace in the string
    \r      Inserts a carriage return in the string
    \u      Inserts a unicode character in the string
    \0oo    Inserts a character in the string based on its Octal value
    \xhh    Inserts a character in the string based on its Hex value
"""

print("You can break \
single line \
to muliple lines")

print("print backslash \\ inside a string")

print('print a single quote \' inside a string')
print("print a double quote \" inside a string")

print("First line \nSecond Line")
print("tab\tspacing")
print("same\rlike")
print("He\bi")
print("\u20B9")
print("\046")
print("\x24")

"""
Raw strings
    A raw string is created by prefixing the character r to the string
        ignores all types of formatting within a string including the
        escape characters
"""
print(r"Bible says, \"Taste and see that the LORD is good; blessed is the man who takes refuged in him.\"")

"""
Unicodes
    prefix u on the string literal
    unicode string is different type of object from regular "str" type
"""
unicode_string = u"A unicode \u018e string \xf1"
unicode_string
