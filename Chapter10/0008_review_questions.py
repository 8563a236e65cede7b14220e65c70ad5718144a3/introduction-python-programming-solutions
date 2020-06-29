"""
Review Questions
1)  In a raw string, escape sequences are not parsed, which
    results in easier to read regular expressions (since you do
    not have to keep escaping the backslashes)

2)  Regular expressions provide a powerful way to search and
    manipulate strings. Regular expressions are essentially a tiny,
    highly specialized programming language embedded inside Python
    and made available through the re module.
    Useful for finding phone numbers, email addresses, dates,
    and any other data that has a consistent format

3)  Special Character [xyz]
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

4)
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
    pattern = re.compile(r"(e)g")
    match_object = pattern.match("egg is a nutritional food")
    match_object
    match_object.group()
    match_object.group(0)

    pattern = re.compile(r"tree:\w\w\w")
    match_object = pattern.search("Example for tree:oak")
    if match_object:
        print(f"Matched string is {match_object.group()}")
    else:
        print("Match not found")

5)  Greedy matching matches as many characters as possible while
    non-greedy matches the fewest possible characters.
        \d+ matches "123" in "123abc"
        \d+? matches "1" in "123abc"



"""