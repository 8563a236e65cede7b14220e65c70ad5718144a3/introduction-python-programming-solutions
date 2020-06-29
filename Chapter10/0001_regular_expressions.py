"""
Regular Expression Operations
    Regular expressions are made available through the re module
    Use a sequence of characters and symbols to define a pattern
    of text

Special Character [xyz]
    Square brackets are used to indicate a set of characters
    Used for specifying a character class, also called a "character
    set"
    Put the characters you wish to match between square brackets
    Matches any one of the characters in the brackets, including
    escape sequences
    Special characters like . and * are not special inside []
    Characters can be listed individually or can be a range of
    characters by giving two characters separated by a hyphen e.g.
    a-z
        [abc] = [a-c]
            matches a, b or c
        [akm$]
            matches a, k, m or $ since $ is not special within
            brackets
        [a-d] = [abcd]

Special Character .
    A period
    Matches any single character except newline "\n"
        .n matches "an" and "on"

Special Character ^
    Matches the start of the string and, in multiline mode, also
    matches immediately after each newline
        ^A does not match "A" in "an A"
           does match "A" in "An E"
    You can match the characters not listed within the class
    by complementing the character set. If the first character
    in the character set is ^, all characters that are not in
    the character set will be matched.
    ^ not as the first character in a character class has no
    special meaning
        [^abc] = [^a-c]
            initially match "r" in "brisket"
            initially match "h" in "chop"

Special Character $
    Matches the end of a string or just before the newline at
    the end of the string
        t$ does not match "t" in "eater"
           does match "t" in "eat"

Special Character *
    Matches the preceding expression 0 or more times
        bo* matches "boooo" in the string "A ghost booooed"
            matches "b" in "A bird warbled"
            does not match anything in "A goat grunted"

Special Character +
    Matches the preceding expression 1 or more times
        a+ matches "a" in "candy"
           matches al the "a"s in "caaaaaaandy"
           does not match anything in "cndy"

Special Character ?
    Matches the preceding expression 0 or 1 time
        e?le? matches "el" in "angel"
              matches "le" in "angle"
              matches "l" in "oslo"
    If used immediately after any of the special characters
    *, + or {}, makes the special character non-greedy (matching
    the fewest possible characters), as opposed to the default
    which is greedy (matching as many characters as possible)
        \d+ matches "123" in "123abc"
        \d+? matches "1" in "123abc"

Special Character \d
    Matches any decimal digit [0-9]
        \d = [0-9]
        \d matches "2" in "B2 is the suite number"

Special Character \D
    Matches any non-digit character. Equivalent to [^0-9]
        \D matches "B" in "B2 is the suite number"

Special Character \w
    Matches a "word" character and it can be a letter, digit or
    underscore. Equivalent to [a-zA-Z0-9_]. Note that although
    "word" is the mnemonic for this, it only matches a single
    word character, not a whole word
        \w matches "a" in "apple"
           matches "5" in "$5.28"
           matches "3" in "3D"

Special Character \W
    Matches any non-word character. Equivalent to
    [^A-Za-z0-9_]
        \W matches "%" in "50%"

Special Character \s
    Matches a single whitespace character including space,
    newline, tab and form feed. Equivalent to [ \n\t\f]
        \s\w* matches "bar" in "foo bar"

Special Character \S
    Matches any non-whitespace character. Equivalent to
    [^ \n\t\f]
        \S* matches "foo" in "foo bar"

Special Character \b
    Matches a word boundary
    There are three different positions that qualify as word
    boundaries when the special character \b is placed
        Before the first character in the string if the first
        character in the string is a word character
        After the last character in the string and if the last
        character in the string is a word character
        Between two characters in the string, where one is a
        word character in the string and the other is not a
        word character
    \b allows you to perform a search of a complete word using
    a regular expression in the form of \bword\b. It won't
    match when it is contained inside another word
    Note that a word is defined as a sequence of word characters
        \bm matches "m" in "moon"
        oo\b does not match "oo" in "moon" because substring "oo"
        followed by word character "n"
        oon\b matches "oon" in "moon" because "oon" is the end of the
        string, thus not followed by a word character
        \bfoo\b matches "foo" in "foo", "foo.", "(foo)", "bar foo baz"
        \bfoo\b does not match "foobar" or "foo3"
        \w\b\w will never match anything because \b can never be
        preceded and followed by a word character

Special Character \B
    Matches a non-word boundary. Matches the following cases
    when \B is placed:
        Before the first character of the word and if the first
        character is not a word character
        After the last character of the word and if the last
        character is not a word character
        Between two-word characters
        Between two non-word characters
    The beginning and end of a string and considered non-word
    characters. The "\B" special character matches an empty string,
    only when it is not a the beginning or end of the word
        \B.. matches the subtring "oo" in "noonday" and the pattern
        y\B. matches the substring "ye" in the string "possibly
        yesterday"

Special Character \
    Matches according to the following rules
        A backslash that precedes a non-special character indicates
        that the next character is special and is not to be
        interpreted literally.
        A backslash that precedes a special character indicates
        that the next character is not special and should be
        interpreted literally
            "b" matches lowercase "b"s
            "\b" does not match any character, forms the special
            word boundary character
            a* relies on special character "*" to match 0 or more
            a's.
            a\* removes the specialness of the "*" to enable matches
            like "a*"

Special Character {m, n}
    Where m and n are positive integers and m <= n
    Matches at least m and at most n occurrences of the preceding
    expression
    If n is omitted i.e. {m,}, then it matches at least m occurrences
    of the preceding expression. Here m must be a positive integer
        a{1,3} matches nothing in "cndy"
               matches "a" in "candy"
               matches "aa" in "caandy"
               matches "aaa" in "caaaaaaandy"
        a{2,}  matches "aa", "aaa", "aaaa", ... but not "a"

Special Character {m}
    Matches exactly m occurrences of the preceding expression.
    Here m must be a positive integer
        a{2} doesn't match "a" in "candy"
             does match all the a's in "caandy"
             matches first two a's in "caaandy"

Special Character |
    A | B matches "A", or "B" (if there is not match for "A"),
    where A and B are regular expressions
        green | red matches "green" in "green apple"
                    matches "red" in "red apple"
    The order of "A" and "B" matters
        a*|b matches the empty string in the string "b"
        b|a* matches "b" in the same string

Using r Prefix for Regular Expressions
    Consider r"^$" - matches the empty string
    ^ indicates the start of the line
    $ indicates the end of the line
    Having nothing in between ^ and $ therefore matches an empty
    line
    "r" tells Python that the expression is a raw string
    Raw strings are handy in regular expressions because escape
    sequences are not parsed
        "\n" is a single newline character
        r"\n" would be two characters, a backslash and an "n"
        r'[\w]' = '[\\w]'

Special Character (...)
    Matches whatever regular expression pattern is inside the
    parentheses and causes that part of the matched substring to be
    remembered. Once remembered, the substring can be recalled
    for other use.
    Parts of a regular expression pattern bounded by parentheses
    are called groups, and they contain the matched substring.
    The parentheses are also called as capturing parentheses
    or capturing group.
    Parentheses indicate the start "(" and end ")" of a group
    Based on the number of parentheses used in a regular expression
    the number of groups are created.
    If your regular expression contains a single pair of
    parentheses (one capturing group) you only get one group in
    your match
    If there are two pairs of parentheses, you get two groups in
    your match, etc.
    If you use a repetition operation on a capturing group (+ or *)
    the group gets "overwritten" each time the group is repeated,
    meaning that only the last match is captured
    The contents of a group can be retrieved after a match has been
    performed.
    Groups are numbered starting from 0, group(0) up to group(99)
    To match literals ( or ) use \( and \), or enclose them inside
    character class [(], [)]
    Parenthesis not only group substrings, they create backreferences
    as well.
    A backreference in a regular expression identifies a previously
    matched and remembered group and allows you to specify its contents
    i.e. backreference matches a substring already found in a group.
    Simply add \ and number of group to match again
    "\1" finds the content matched by the first group in a regular
    expression
    Always represent backreferences as raw strings in regular
    expressions
        Chapter (\d+)\.\d* illustrates additional escaped and
        special characters and indicates that part of the pattern
        should be remembered. It matches precisely the characters
        "Chapter" followed by a space, followed by on or more
        numeric characters, followed by a decimal point, followed
        by any numeric character 0 or more times
        In addition, parentheses are used to remember the first
        matched numeric characters
        matches "Open Chapter 4.3, paragraph 6" where "4" is
        remembered
        does not match "Chapter 3 and 4" because string does not
        have a period after the 3
    To match a substring without causing the matched part to be
    remembered within parentheses prefix the pattern with ?:
        (?:\d+) matches one or more numeric characters but does
        not remember the matched characters

Regular Expression Methods
    Import re module
    re module provides an interface to the Python regular expression
    engine.
    Regular expressions can be compiled into a pattern object,
    which has methods for various operations such as searching
    for pattern matches, finding all pattern matches or
    performing string substitutions
    Whenever you have to use the same regular expression again and
    again on different strings, then it is an excellent idea to
    construct a regular expression as a Python object
        re.compile(pattern[,flags])
            where pattern is the regular expression and the optional
            flags argument is used to enable various special
            features and syntax variations
                re.A enables ASCII only matching
                re.I enables case-insensitive matching
                re.M enables multiline matching
                    "^" matches at beginning of string and also
                    beginning of each line
                    "$" matches end of string and also the end
                    of each line
        compile() returns a regular expression as a Python object
        which can be used for matching patterns by using its
        match(), search(), sub(), findall() and other methods
-------------------------------------------------------------------------------
search()    regex_object.           This method scans through string looking
                search(string[,     for the first location where this regular
                pos[,endpos]])      expression produces a match and returns
                                    a corresponding match object. Returns
                                    None if no position in the string matches
                                    the pattern
-------------------------------------------------------------------------------
match()     regex_object.           This method returns None if the string
                match(string[,      does not match the pattern and returns a
                pos[,endpos]])      match object if the method finds a match
                                    Matches characters at the beginning of the
                                    string in accordance with the regular
                                    expression pattern. Note that even in
                                    MULTILINE mode, the match() method will
                                    only match at the beginning of the string
                                    and not at the beginning of each line
-------------------------------------------------------------------------------
findall()   regex_object.           Returns all non-overlapping matches of a
                findall(string[,    pattern in string, as a list of strings.
                pos[,endpos]])      The string is scanned left-to-right and
                                    matches are returned in the order found.
                                    If the pattern includes two ore more
                                    parenthesis groups, then instead of
                                    returning a list of strings, findall()
                                    returns a list of tuples. Each tuple
                                    represents one match of the pattern, and
                                    inside the tuple is the group(1), group(2)
                                    ... substrings. Empty matches are included
                                    in the result
-------------------------------------------------------------------------------
sub()       regex_object.           This method returns the string obtained by
                sub(pattern,        replacing the leftmost non-overlapping
                repl, string,       occurrences of the pattern in string by
                count=0,            by the replacement repl. If the pattern
                flags=0)            is not found, the string is returned
                                    unchanged. Any backslash escapes in repl are
                                    processed i.e. \n is converted to a single
                                    newline character, \r is converted to
                                    a carriage return and so forth.
                                    Unknown escapes such as \& are left alone.
                                    Backreferences such as \2 are replaced with
                                    the substring matched by group 2 in the
                                    pattern.
-------------------------------------------------------------------------------

Match Objects
    match() and search() methods supported by a compiled regular
    expression object returns None if no match is found. If they
    are successful, a match object instance is returned, containing
    information about the match like the substring it has matched,
    where the match starts and ends, and much more.
    Since match() and search() return None when there is no match,
    you can test whether there was a match with a simple if
    statement
        match_object = regex_object.search(string)
        if match_object:
            statement_1
            ...
            statment_n
    If Match object is True, then execute the statements

Match Object Methods
---------------------------------------------------------------------------------------
group()     match_object.               This method returns one or more subgroups
                group([group1,...])     of the match. If there is a single argument
                                        the result is a single string. If there are
                                        multiple arguments, the result is a tuple with
                                        one item per argument. Without arguments,
                                        group1 defaults to zero and the whole match is
                                        returned. If a groupN argument is zero, the
                                        corresponding return value is the entire
                                        matching string. If it is in the inclusive
                                        range of [1...99], then it is the string
                                        matching the corresponding parenthesized
                                        group. If the group number is negative or
                                        larger than the number of groups defined in
                                        the pattern, then IndexError is raised.
                                        If a group is contained in a part of the
                                        pattern that did not match, the corresponding
                                        result in None. If a group is contained in a
                                        part of the pattern that matched multiple times
                                        the last match is returned
---------------------------------------------------------------------------------------
groups()    match_object.               Returns a tuple containing all the subgroups
                groups(default=None)    of the match, from 1 to however many groups
                                        are in the pattern. Default argument is used
                                        for groups that did not participate in the
                                        match; it defaults to None
---------------------------------------------------------------------------------------
start()     match_object.               start() returns the index of the start and
                start([group])          end method returns the index of the the end
end()       match_object.               of the substring matched by group. Default value
                end([group])            of group is zero, which means the whole matched
                                        substring is returned else a value of -1 is
                                        returned if a group exists but did not contribute
                                        to the match
---------------------------------------------------------------------------------------
span()      match_object.               This method returns a tuple containing the
                span([group])           (m.start(group), m.end(group)) positions of the
                                        match
---------------------------------------------------------------------------------------

In order to build and use regular expressions, perform the following
steps
    1) Import re regular expression module
    2) Compile regular expression pattern using re.compile() method.
       This method returns the regular expression pattern as an
       object
    3) Invoke an appropriate method supported by the compiled regular
       expression object which returns a matched object instance
       containing information about matched strings
    4) Call methods(group() method most appropriate for most cases)
       associated with the matched object to display the results

"""
import re

pattern = re.compile(r"(e)g")
pattern
match_object = pattern.match("egg is a nutritional food")
match_object
match_object.group()
match_object.group(0)

match_object = pattern.match("brownegg is a nutritional food")
match_object.group()    #AttributeError

pattern = re.compile(r"(ab)*")
match_object = pattern.match("ababababab")
match_object.span()
match_object.start()
match_object.end()

pattern = re.compile(r"(a(b)c)d")
method_object = pattern.match("abcd")
method_object.group(0)
method_object.group(1)
method_object.group(2)
method_object.group(2, 1, 2)
method_object.groups()

pattern = re.compile(r"\d+")
match_list = pattern.findall("Everybody thinks they're famous when "
                             "they get 100000 followers on Instagram "
                             "and 5000 on Twitter")
match_list

pattern = re.compile(r"([\w\.]+)@([\w\.]+)")
matched_email_tuples = pattern.findall(
    "bill_gates@microsoft.com and steve.jobs@apple.com are visionaries"
)
print(matched_email_tuples)
for each_mail in matched_email_tuples:
    print(f"User name is {each_mail[0]}")
    print(f"Domain name is {each_mail[1]}")

pattern = re.compile(r"(\w+)\s(\w+)")
replaced_string = pattern.sub(r"\2 \1", "Ken Thompson")
replaced_string

pattern = re.compile(r",")
replaced_string = pattern.sub("$", "this,is,a,test")
replaced_string

pattern = re.compile(r"tree:\w\w\w")
match_object = pattern.search("Example for tree:oak")
if match_object:
    print(f"Matched string is {match_object.group()}")
else:
    print("Match not found")
