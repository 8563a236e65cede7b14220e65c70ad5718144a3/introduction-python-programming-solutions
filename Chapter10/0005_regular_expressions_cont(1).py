"""
Named Groups in Python Regular Expressions
    Instead of referring to the groups by numbers, you can reference
    them by a name
        (?P<name>RE)
    where first name character is ? followed by letter P that stands
    for Python Specific extension, name is the name of the group written
    within angle brackets, and RE is the regular expression.
"""
import re

pattern = re.compile(r"(?P<word>\b\w+\b)")
match_object = pattern.search("laugh out loud")
match_object.group("word")
match_object.group(1)

"""
Regular Expression with glob Module
    glob module finds all the file names matching a specified pattern
    With Python 3.5+, glob supports "**" directive which is only parsed
    if you supply the recursive flag.
        glob.glob(pathname, **, recursive=True)
    glob() method of glob modules returns a possible list of file names
    that match a pathname, which must be a string containing a path
    specification. Here pathname can be either absolute, or relative
    If recursive is True, the pattern "**" will match any files and
    zero or more directories and subdirectories
"""