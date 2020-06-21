"""
String Methods
    Get a list of all methods associated with string
"""
dir(str)

"""
isidentifier()  l
------------------------------------------------------------------------------------------------
capitalize()    string_name.capitalize()        returns a copy of the string with its
                                                first character capitalized and the rest
                                                lowered
------------------------------------------------------------------------------------------------
casefold()      string_name.casefold()          returns a casefold copy of the string.
                                                Casefolded strings may be used for caseless
                                                matching
------------------------------------------------------------------------------------------------
center()        string_name.center(width[,      makes string_name centered by taking width
                    fillchar])                  parameter into account. Padding is specified
                                                by parameter fillchar. Default filler is space
------------------------------------------------------------------------------------------------
count()         string_name.count(substring[,   returns the number of non-overlapping 
                    start [,end]])               occurrences of substring in the range [start,
                                                end]. Optional arguments are interpreted as in
                                                slice notation
------------------------------------------------------------------------------------------------
endswith()      string_name.endswith(suffix[,   returns True if the string_name ends with the 
                    start[,end]])                specified suffix substring, otherwise returns
                                                False. With optional start, test beginning at
                                                that position. With optional end, stop comparing
                                                at that position
------------------------------------------------------------------------------------------------
find()          string_name.find(substring[,    Checks if substring appears in string_name or if
                    start[,end]])               substring appears in string_name by starting at
                                                index start and ending index end. Return 
                                                position of the first character of the first
                                                instance of string substring in string_name,
                                                otherwise return -1 if substring not found in
                                                string_name
------------------------------------------------------------------------------------------------
isalnum()       string_name.isalnum()           returns True if all characters in the string are
                                                alphanumeric and there is at least one character
                                                else returns False
------------------------------------------------------------------------------------------------
isalpha()       string_name.isalpha()           returns True if all characters in the string are
                                                alphabetic and there is at least one character
                                                else returns False
------------------------------------------------------------------------------------------------
isdecimal()     string_name.isdecimal()         returns True if all characters in the string are
                                                decimal and there is at least one character
                                                else returns False
------------------------------------------------------------------------------------------------
isdigit()       string_name.isdigit()           returns True if all characters in the string are
                                                digits and there is at least one character
                                                else returns False
------------------------------------------------------------------------------------------------
isidentifier()  string_name.isidentifier()      returns True if the string is a valid identifier
                                                else returns False
------------------------------------------------------------------------------------------------
islower()       string_name.islower()           returns True if all characters in the string are
                                                lowercase else returns False
------------------------------------------------------------------------------------------------
isspace()       string_name.isspace()           returns True if all characters in the string are
                                                whitespace and there is at least one character
                                                else returns False
------------------------------------------------------------------------------------------------
isnumeric()     string_name.isnumeric()         returns True if all characters in the string are
                                                numeric and there is at least one character
                                                else returns False
------------------------------------------------------------------------------------------------
istitle()       string_name.isspace()           returns True if the string is a title cased
                                                string and there is at least one character else 
                                                returns False
------------------------------------------------------------------------------------------------
isupper()       string_name.isupper()           returns True if all cased characters in the
                                                string are uppercase and there is at least one 
                                                cased character else returns False
------------------------------------------------------------------------------------------------
upper()         string_name.upper()             converts lower case letters in a string to 
                                                uppercase
------------------------------------------------------------------------------------------------
lower()         string_name.lower()             converts upper case letters in a string to 
                                                lowercase
------------------------------------------------------------------------------------------------
ljust()         string_name.ljust(width[,       returns the left justified string. Total length
                    fillchar])                  of the string is defined in the first parameter
                                                of method width. Padding is done as defined in
                                                second parameter fillchar
------------------------------------------------------------------------------------------------
rjust()         string_name.rjust(width[,       returns the right justified string. Total length
                    fillchar])                  of the string is defined in the first parameter
                                                of method width. Padding is done as defined in
                                                second parameter fillchar
------------------------------------------------------------------------------------------------
title()         string_name.title()             returns "titlecased" versions of string
------------------------------------------------------------------------------------------------
swapcase()      string_name.swapcase()          returns a copy of the string with uppercase
                                                characters converted to lowercase and vice
                                                versa
------------------------------------------------------------------------------------------------
splitlines()    string_name.                    Returns a list of lines in the string, breaking
                    splitlines([keepends])      at line boundaries. Line breaks are not included
                                                in the resulting list unless keepends is given
                                                and true
------------------------------------------------------------------------------------------------
startswith()    string_name.startswith(prefix[, returns True if the string_name starts with the 
                    start[,end]])               specified prefix substring, otherwise returns
                                                False. With optional start, test beginning at
                                                that position. With optional end, stop comparing
                                                at that position
------------------------------------------------------------------------------------------------
strip()         string_name.strip([chars])      returns a copy of the string_name in which
                                                specified chars have been stripped from both
                                                sides of the string. If char is not specified
                                                then taken as default
------------------------------------------------------------------------------------------------
rstrip()        string_name.rstrip([chars])     removes all trailing whitespace of string_name
------------------------------------------------------------------------------------------------
lstrip()        string_name.lstrip([chars])     removes all leading whitespace of string_name
------------------------------------------------------------------------------------------------
replace()       string_name.replace(old,        replaces all occurrences of old in string_name
                    new[,max])                  with new. If optional argument max is given,
                                                then only the first max occurrences are replaced
------------------------------------------------------------------------------------------------
zfill()         string_name.zfill(width)        pads string_name on the left with zeros to fill
                                                width
------------------------------------------------------------------------------------------------
"""
fact = "Abraham Lincoln was also a champion wrestler"
fact.isalnum()

"sailors".isalpha()
"2018".isdigit()
fact.islower()
"TSAR BOMBA".isupper()
"columbus".islower()
warriors = "ancient gladiators were vegetarians"
warriors.endswith("vegetarians")
warriors.startswith("ancient")
warriors.startswith("A")
warriors.startswith("a")
"cucumber".find("cu")
"cucumber".find("um")
"cucumber".find("xyz")
warriors.count("a")

species = "charles darwin discovered galapagos tortoises"
species.capitalize()
species.title()

"Tortoises".lower()
"galapagos".upper()
"Centennial Light".swapcase()

"history does repeat".replace("does","will")

quote = "  Never Stop Dreaming  "
quote.rstrip()
quote.lstrip()
quote.strip()

"abc\n\ndefg\rkl\r\n".splitlines()

"scandinavian countries are rich".center(40)
