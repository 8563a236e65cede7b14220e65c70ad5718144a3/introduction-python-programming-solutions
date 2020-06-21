"""
Strings
    A string consists of a sequence of characters. You use
    single or double quotation marks to represent them
"""


single_quote = 'This is a single message'
double_quote = "Hey it is my books"
single_char_string = "A"
empty_string = ""
single_within_double_quote = "Opportunities don't happen. You create them"
double_within_single_quote = "Why did she call the man 'smart'?"
same_quotes = 'I\'ve an idea'
triple_quote_string = '''This
is
triple
quote
'''
triple_quote_string
type(single_quote)

"""
str() function
    returns a string which is considered an informal or nicely
    printable representation of the given object
        str(object)
"""
str(10)
create_string = str()
type(create_string)

"""
Basic String Operations
    strings can be concatenated with _
    strings can be repeated with *
"""
string_1 = "face"
string_2 = "book"
concatenated_string = string_1 + string_2
concatenated_string

concatenated_string_with_space = "Hi " + "There"
concatenated_string_with_space

singer = 50 + "cent"    #Type error
singer = str(50) + "cent"
singer

repitition_of_string = "wow" * 5
repitition_of_string

"""
Membership operators
    in
    not in
"""
fruit_string = "apple is a fruit"
fruit_sub_string = "apple"
fruit_sub_string in fruit_string

another_fruit_string = "orange"
another_fruit_string not in fruit_string

"""
String Comparison
    You can compare strings based on ASCII value using
        <, >, <=, >=, ==, !=
"""
"january" == "jane"
"january" != "jane"
"january" < "jane"
"january" > "jane"
"january" <= "jane"
"january" >= "jane"
"filled" > ""

"""
Built-In Functions Used On strings
    len()   number of characters in string
    max()   returns character having highest ASCII value
    min()   returns character having lowest ASCII value
"""
count_characters = len("eskimos")
count_characters
max("axel")
min("brad")

"""
Accessing Characters in String by Index Number
    string_name[index]
"""
word_phrase = "be yourself"
word_phrase[0]
word_phrase[1]
word_phrase[2]
word_phrase[3]
word_phrase[10]
word_phrase[11]

word_phrase[-1]
word_phrase[-2]

"""
String Slicing and Joining
    string_name[start:end[:step]]
    you can access a sequence o characters by specifying a
    range of index numbers separated by a colon
    String slicing returns a sequence of characters beginning
    at start and extending up to but not including end.
    Can use position or negative integers
"""
healthy_drink = "green tea"
healthy_drink[0:3]
healthy_drink[0:5]
healthy_drink[6:]
healthy_drink[:]
healthy_drink[4:4]
healthy_drink[6:20]

healthy_drink[-3:-1]
healthy_drink[6:-1]

newspaper = "new york times"
newspaper[0:12:4]
newspaper[::4]
newspaper[::-1]