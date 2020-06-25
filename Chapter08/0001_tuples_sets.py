"""
Tuples and Sets
    In mathematics a tuple is a finite ordered list (sequence) of
    elements.
    A tuple is defined as a data structure that comprises and
    ordered, finite sequence of immutable, heterogeneous elements
    that are of fixed sizes.
    Tuples solve the problem of returning more than one value
    from a function and also for passing multiple values through
    one function parameter.

Creating tuples
    A tuple is a finite ordered list of values of possibly different
    types which is used to bundle related values together, without
    having to create a specific type to hold them.
    Tuples are immutable

    tuple_name = (item_1, item_2, ..., item_n)
"""
internet = ("cern", "timbernersless", "www", 1980)
internet
type(internet)

f1 = "ferrari", "redbull", "mercedes", "williams", "renault"
f1
type(f1)

"""
Tuples can be formed with or without parentheses, it is
the commas that are significant in the syntax

Empty tuple
    tuple_name = ()
"""
empty_tuple = ()
empty_tuple

"""
Tuples can contain heterogenous data types
and be nested
"""
air_force = ("f15", "f22a", "f35a")
fighter_jets = (1988, 2005, 2016, air_force)
fighter_jets
type(fighter_jets)

"""
Empty tuples and tuples with one item
    It is not sufficient to enclose a single value
    in parentheses
"""
empty = ()
singleton = ("hello",)
singleton

"""
Basic Tuple Operations
    You can use the + operator to concatenate tuples together
    You can use * to repeat the sequence of tuple items
    You can use == to test for equality
    You can use in and not in to test for the presence of an item
    in a tuple
    For position by position comparison, you can use 
        <, <=, >, >=, == and !=
"""
tuple_1 = (2, 0, 1, 4)
tuple_2 = (2, 0, 1, 9)
tuple_1 + tuple_2
tuple_1 * 3
tuple_1 == tuple_2

tuple_items = (1, 9, 8, 8)
1 in tuple_items
25 in tuple_items

tuple_1 = (9, 8, 7)
tuple_2 = (9, 1, 1)
tuple_1 > tuple_2
tuple_1 != tuple_2

"""
The tuple() Function
    tuple([sequence])
    where the sequence can be a number, string or tuple itself
    if optional sequence is not specified, an empty tuple is
    created
"""
norse = "vikings"
string_to_tuple = tuple(norse)
string_to_tuple

zeus = ["g", "o", "d", "o", "f", "s", "k", "y"]
list_to_tuple = tuple(zeus)
list_to_tuple

string_to_tuple + "scandinavia" #TypeError
list_to_tuple + ["g", "r", "e", "e", "k"]   #TypeError
list_to_tuple + tuple(["g", "r", "e", "e", "k"])

letters = ("a", "b", "c")
numbers = (1, 2, 3)
nested_tuples = (letters, numbers)
nested_tuples
tuple("wolverine")

"""
Indexing and Slicing in Tuples
    Each item in a tuple can be called individually through
    indexing. The expression inside the bracket is called the
    index. Square brackets [] are used by tuples to access
    individual items, with the first item at index 0, the
    second item at index 1 etc.
        tuple_name[index]
"""
holy_places = (
    "jerusalem",
    "kashivishwanath",
    "harmandirsahib",
    "bethlehem",
    "mahabodhi"
)
holy_places

holy_places[0]
holy_places[1]
holy_places[2]
holy_places[3]
holy_places[4]
holy_places[5]  #IndexError
holy_places[-2]

"""
Slicing
    tuple_name[start:stop[:step]]
"""
colors = tuple("vibgyor")
colors

colors[1:4]
colors[:5]
colors[3:]
colors[:]
colors[::]
colors[1:5:2]
colors[::2]
colors[::-1]
colors[-5:-2]

"""
Built-In Functions Used on Tuples
len()       returns number of items in a tuple
sum()       returns sum of numbers in tuple
sorted()    returns a sorted copy of the tuple as
            a list while leaving the original tuple
            untouched
"""
years = (1987, 1985, 1981, 1996)
len(years)
sum(years)
sorted_years = sorted(years)
sorted_years

"""
Relation between Tuples and Lists
    Often used in different situations and for different
    purposes
    Tuples are immutable and usually contain a heterogeneous
    sequence of elements that are accessed via unpacking or
    indexing
    Lists are mutable and their items are accessed via indexing
    Items cannot be added, removed or replaced in a tuple
"""
coral_reef = ("great_barrier", "ningaloo_coast", "amazon_reef", "pickles_reef")
coral_reef[0] = "pickles_reef"  #Type Error

coral_reef_list = list(coral_reef)
coral_reef_list

"""
If an item within a tuple is mutable, then you can change it
    Consider a list as an item in a tuple
"""
german_cars = ["porsche", "audi", "bmw"]
european_cars = ("ferrari", "volvo", "renault", german_cars)
european_cars
european_cars[3].append("mercedes")
european_cars

"""
Relation between Tuples and Dictionaries
Tuples can be used as key:value pairs to build dictionaries
"""
fish_weight_kg = (
    ("white_shark", 520),
    ("beluga", 1571),
    ("greenland_shark", 1400)
)

fish_weight_kg_dict = dict(fish_weight_kg)
fish_weight_kg_dict

founding_year = {
    "Google": 1996,
    "Apple": 1976,
    "Sony": 1946,
    "ebay": 1996,
    "IBM": 1911
}

founding_year.items()
for company, year in founding_year.items():
        print(f"{company} was founded in the year {year}")

"""
Tuple Methods
count() tuple_name.count(item)  returns the number of times the item
                                has occurred in the tuple and returns
                                it
index() tuple_name.index(item)  searches for the given item from the
                                start of the tuple and returns its
                                index. If the value appears more than
                                once, you will get the index of the
                                first one. If the item is
                                not present then ValueError is thrown
"""
dir(tuple)
channels = ("ngc", "discovery", "animal_planet", "history", "ngc")
channels.count("ngc")
channels.index("history")

"""
Tuple packing and unpacking
"""
t = (12345, 54321, "hello!")
t

x, y, z = t
x
y
z
