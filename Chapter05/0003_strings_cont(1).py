"""
Joining strings using join() Method
    string_name.join(sequence)
"""
date_of_birth = ["17", "09", "1950"]
":".join(date_of_birth)

social_app = ["instagram", "is", "a", "photo", "sharing", "application"]
" ".join(social_app)

numbers = "123"
characters = "amy"
password = numbers.join(characters)
password

"""
Split Strings Using split() Method
    The split() method returns a list of string items by breaking up
    the string using the delimiter string
    string_name.split([seperator [, maxsplit]])
    
    here separator is the delimiter string and is optional
        if separator not specified, then whitespace is considered
        delimiter
    if maxsplit is given, at most maxsplit splits are done
        if not specified or -1, then no limit on number of splits
"""
inventors = "edison,tesla,marconi,newton"
inventors.split(",")

watches = "rolex hublot cartier omega"
watches.split()

"""
Strings are immutable
    strings cannot be modified
    the characters in a string cannot be changed once a string
    value is assigned to string variable
    you can assign different string values to the same string variable
"""
immutable = "dollar"
immutable[0] = "c"  #TypeError

string_immutable = "c" + immutable[1:]
string_immutable

immutable = "rollar"
immutable

"""
String Traversing
    Since the string is a sequence of characters, each of these
    characters can be traversed using the for loop
"""