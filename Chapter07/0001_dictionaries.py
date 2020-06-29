"""
Dictionaries
    Also known as associative memories or associative arrays
    A dictionary is a collection of an unordered set of key:value
    pairs, with the requirements that the keys are unique within
    a dictionary.

    Dictionaries are constructed by using curly braces wherein you
    include a list of key:value pairs separated by commas.
    There is a colon (:) separating each of these key and value
    pairs where the words to the left of the colon operator are
    they keys and the words to the right of the colon operator
    are the values.

    Dictionaries are indexed by keys, unlike lists which are indexed
    by a range of numbers.

    dictionary_name = {key_1:value_1, key_2: value_2, ..., key_n:value_n}
"""
fish = {"g": "goldfish", "s": "shark", "n": "needlefish", "b": "barramundi", "m":"mackerel"}
fish

"""
Dictionary keys are immutable and can either be a string or number
Since lists can be modified in place using index assignments,
slice assignments, or methods like append() and extend(), you 
cannot use lists as keys. Duplicate keys are not allowed in the
dictionary
"""
mixed_dict = {"portable": "laptop", 9: 11, 7: "julius"}
mixed_dict
type(mixed_dict)

"""
Create empty dictionary
    dictionary_name = {}
"""
empty_dictionary = {}
empty_dictionary

"""
In dictionaries, the order of key:value pairs does not matter
"""
pizza = {"pepperoni": 3, "calzone": 5, "margherita": 4}
fav_pizza = {"margherita": 4, "pepperoni": 3, "calzone": 5}
pizza == fav_pizza

"""
Before python 3.6, dictionaries resulted in an unordered output
From python 3.6, output is ordered by insertion order

Accessing and Modifying key:value Pairs in Dictionaries
    dictionary_name[key]
    dictionary_name[key] = value
        if the key is already present in the dictionary, then the
        key gets updated with the new value, otherwise the key:value
        pair gets added to the dictionary
"""
renaissance = {"giotto": 1305, "Donatello": 1440, "Michaelangelo": 1511, "Botticelli": 1480, "clouet": 1520}
renaissance
renaissance["giotto"] = "1310"
renaissance
renaissance["Michaelangelo"]
renaissance["leonardo"] = 1503
renaissance
renaissance["piero"]    #KeyError

"""
Check presence of a key in the dictionary by using
in and not in membership operators
"""
clothes = {"rainy": "raincoats", "summer": "tees", "winter": "sweaters"}
"spring" in clothes
"spring" not in clothes

"""
dict() Function
    Used to create a dictionary
    dict([**kwargs])
    dict() creates an empty dictionary
    Optional keyword arguments are used to initialize dictionary
    kwarg=value
"""
numbers = dict(one=1, two=2, three=3)
numbers

"""
Syntax for dict() when iterables are used is
    dict(iterable[, **kwarg])
"""
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

"""
Built in functions
len()       returns the number of items (key:value pairs)
all()       returns True if all keys in dictionary are True
any()       returns True if any of the keys in the dictionary are True
sorted()    returns a list of items, which are sorted based on dictionary keys
"""
presidents = {"washington": 1732, "jefforson": 1751, "lincoln": 1809, "roosevelt": 1858, "eisenhower": 1890}
len(presidents)

all_dict_func = {0: True, 2: False}
all(all_dict_func)
all_dict_func = {1: True, 2: False}
all(all_dict_func)

any_dict_func = {1: False, 2: False}
any(any_dict_func)

sorted(presidents)
sorted(presidents, reverse=True)

sorted(presidents.values())
sorted(presidents.items())

"""
Dictionary Methods
clear()         dict_name.clear()       removes all key:value pairs from the dictionary
fromkeys()      dict_name.fromkeys(seq  creates a new dictionary from the given sequence of
                    [,value])           elements with a value provided by the user
get()           dict_name.get(key       returns the value associated with the specified key
                    [,default])         in the dictionary. If key is not present, then it
                                        returns the default value. If default not given,
                                        defaults to None, so that this method never raises a
                                        KeyError
items()         dict_name.items()       method returns a new view of dictionary's key and value
                                        pairs as tuples
keys()          dict_name.keys()        returns a new view consisting of all the keys in the dictionary
pop()           dict_name.pop(key       removes the key from the dictionary and returns its vale. If
                    [,default])         the key is not present, then it returns the default value. If
                                        default is not given and the key is not in the dictionary, then
                                        it results in KeyError
popitem()       dict_name.popitem()     removes and returns an arbitrary (key, value) tuple pair from
                                        the dictionary. If the dictionary is empty, the calling popitem()
                                        results in KeyError
setdefault()    dict_name.setdefault(   returns a value for the key present in the dictionary. If the key
                    key[,default])      is not present, the insert the key into the dictionary with a
                                        default value and return the default value. If key is present,
                                        default deaults to None, so that this method never raises a KeyError
update()        dict_name.update(       updates the dictionary with the key:value pairs from other dictionary
                    [other])            object and it returns None
values()        dict_name.values()      returns a new view consisting of all the values in the dictionary

*   objects returned by dict.keys(), dict.values() and dict.items()
    are view objects. They provide a dynamic view of the dictionary's
    entries, thus when the dictionary changes, the view reflects
    these changes
"""
dir(dict)

box_office_billion = {"avatar": 2009, "titanic": 1997, "starwards": 2015, "harry_potter": 2011, "avengers": 2012}
box_office_billion
box_office_billion_fromkeys = box_office_billion.fromkeys(box_office_billion)
box_office_billion_fromkeys
box_office_billion_fromkeys = box_office_billion.fromkeys(box_office_billion, "billion_dollar")
box_office_billion_fromkeys
print(box_office_billion.get("frozen"))
box_office_billion.get("frozen", 2013)
box_office_billion.keys()
box_office_billion.values()
box_office_billion.items()
box_office_billion.update({"frozen": 2013})
box_office_billion
box_office_billion.setdefault("minions")
box_office_billion
box_office_billion.setdefault("ironman", 2013)
box_office_billion

box_office_billion.pop("avatar")
box_office_billion.popitem()
box_office_billion.clear()
box_office_billion

"""
Use list() to coerce views from keys(), values() and items()
to become a list and editable
Views are normally read-only
"""
box_office_billion = {"avatar": 2009, "titanic": 1997, "starwards": 2015, "harry_potter": 2011, "avengers": 2012}
list(box_office_billion.keys())
list(box_office_billion.values())
list(box_office_billion.items())

"""
Populating Dictionaries with key:value Pairs
    use update()
    or dict_name[key] = value
"""
countries = {}
countries.update({"Asia": "India"})
countries.update({"Europe": "Germany"})
countries.update({"Africa": "Sudan"})
countries

