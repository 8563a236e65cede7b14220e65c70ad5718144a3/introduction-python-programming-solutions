"""
Review Questions

1)  The len() function calculates the number of characters in a string.
    The whitespace characters are also counted
        count_characters = len("eskimos")

2)  You can creat strings in a variety of ways
        Single Quotes
            single_quote = 'This is a single message'
        Double Quotes
            double_quote = "This is a double message"
        Triple Quotes
            triple_quote= '''This is a triple quote'''
        str Function
            str_quote = str("ABC")

3)  With string slicing you can access a sequence of characters
    by specifying a range of index numbers separated by a colon.
    String slicing returns a sequence of characters beginning at
    start and extending up to but not including end. Also has a
    step parameter
        string_name[start:end[:step]]
        healthy_drink = "green tea"
        healthy_drink[0:3]
        healthy_drink[:5]
        healthy_drink[6:]
        healthy_drink[:]

4)  Escape sequences
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

5)  You can check for the presence of a string using in and not in
    membership operators. The in operator evaluates to True if
    the string value in the left operand appears in the sequence of
    characters of the string value in the left operand.
        fruit_string = "apple is a fruit"
        fruit_sub_string = "apple"
        fruit_sub_string in fruit_string

6)  %-formatting is one way of formatting strings in Python. %-formatting
    is limited to the types it supports - only int, str and doubles can
    be formatted. All other types are either not supported or converted
    to one of these types. Also, does not support tuples.

7)  a)  isidentifier() returns Boolean True if the string is a valid
        identifier, else it returns Boolean False

        isnumeric() returns Boolean True if all characters in the
        string_name are numeric characters, and there is at least
        one character, else it returns Boolean False

    b)  find() checks if a substring appears in string_name or if
        substring appears in string_name specified by starting
        index start and ending index end. Return position of the
        first character of the first instance of string substring
        in string_name, otherwise return -1 if substring is not
        found in string_name

        casefold() returns a casefolded copy of the string which
        may be used for caseless matching

    c)  split() returns a list of string items by breakup up the
        string using the delimiter string. A given string is split
        into list of strings based on the specified separator. If
        separator is not specified then whitespace is considered
        as the string delimiter. If maxsplit is given, at most
        maxsplit splits are done. If maxsplit is not given or -1
        then there is no limit on the number of splits

        splitlines() returns a list of the lines in the string,
        breaking at line boundaries. Line breaks are not
        included in the resulting list unless keepends is given
        and true.

8)  You would get a TypeError exception

10) Print the entire string variable message

17) a) False
    b) 2
    c) True
    d) PARIS
    e) 6
    f) london
"""