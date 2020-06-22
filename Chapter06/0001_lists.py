"""
Lists
    A list is a container that holds a number of items
    Each element is called an item
    ALl items in a list are assigned to a single variable
    Lists can be simple or nested with varying types of values

Creating Lists
    list_name = [item_1, item_2, ..., item_n]
    empty_list = []
"""
superstore = ["metro", "tesco", "walmart", "kmart", "carrefour"]
superstore

number_list = [4, 4, 6, 7, 2, 9, 10, 15]
number_list

mixed_list = ['dog', 87.23, 65, [9, 1, 8, 1]]
mixed_list
type(mixed_list)

empty_list = []
empty_list
type(empty_list)

"""
Basic List Operations
    Lists can be concatenated with +
    * is used to create a repeated sequence of list items
    == is used to check for equality
    in and not in test set membership
"""
list_1 = [1, 3, 5, 7]
list_2 = [2, 4, 6, 7]
list_1 + list_2
list_1 * 3
list_1 == list_2

list_items = [1, 3, 5, 7]
5 in list_items
10 in list_items

"""
The list function
    list([sequence])
    where sequence can be a string, tuple or list itself. If the
    optional sequence is not specified then an empty list is created
"""
quote = "How you doing?"
string_to_list = list(quote)
string_to_list

friends = ["j", "o", "e", "y"]
friends + quote     #TypeError

"""
Indexing and Slicing in Lists
    list_name[index]
"""
superstore = ["metro", "tesco", "walmart", "kmart", "carrefour"]
superstore[0]
superstore[1]
superstore[2]
superstore[3]
superstore[9]   #IndexError

superstore[-3]

"""
Modifying items in Lists
    Lists are mutable
"""
fauna = ["pronghorn", "alligator", "bison"]
fauna
fauna[0] = "groundhog"
fauna
fauna[2] = "skunk"
fauna
fauna[-1] = "beaver"
fauna

"""
***
    Assigning an existing list variable to a new variable
    does not make a new copy of the list. Just yields a 
    pointer to the original list's memory location
***
"""
zoo = ["Lion", "Tiger", "Zebra"]
forest = zoo
type(zoo)
type(forest)
forest
zoo[0] = "Fox"
forest
forest[1] = "Deer"
forest
zoo

"""
Slicing
    Slicing of lists is allowed in Python wherein a part of
    the list can be extracted by specifying index range along with 
    the colon (:) operator which itself is a list
        list_name[start:stop[:step]]
    where both start and stop are integer values. Includes start
    value but excludes the stop index value. Step specifies the
    increment value to slice by and is optional
"""
fruits = ["grapefruit", "pineapple", "blueberries", "mango", "banana"]
fruits[1:3]
fruits[:3]
fruits[2:]
fruits[1:4:2]
fruits[:]
fruits[::2]
fruits[::-1]
fruits[-3:-1]

"""
Built-In Functions used on lists

len()       returns the number of items in a list
sum()       returns the sum of numbers in the list
any()       returns True if any of the Boolean values in the list is True
all()       returns True if all the Boolean values in the list are true
sorted()    returns a modified copy of the list while leaving the original list untouched
"""
lakes = ["superior", "erie", "huron", "ontario", "powell"]
len(lakes)

numbers = [1, 2, 3, 4, 5]
sum(numbers)
max(numbers)
min(numbers)

any([1, 1, 0, 0, 1, 0])
all([1, 1, 1, 1])

lakes_sorted_new = sorted(lakes)
lakes_sorted_new

"""
List Methods
append()    list.append(item)       adds a single item to the end of the list.
                                    Does not return a new list and just modifies
                                    the original
count()     list.count(item)        counts the number of times item has occurred
                                    in the list
insert()    list.insert(index,item) inserts the item at the given index, shifting 
                                    items to the right
extend()    list.extend(list2)      adds the items in list2 to the end of the list
index()     list.index(item)        searches for the given item from the start of the 
                                    list and returns its index. If the value appears 
                                    more than once, only the index of the first occurrence
                                    is returned. If the item is not present in the list 
                                    then ValueError is thrown
remove()    list.remove(item)       searches for the first instance of the given item in the
                                    list and removes it. If the item is not present in the 
                                    list then ValueError is thrown
sort()      list.sort               sorts the items in the list in-place. Modifies the
                                    original list and does not return a new list
reverse()   list.reverse()          reverses the items in place in the list. Modifies the
                                    original list and does not return a new list
pop()       list.pop([index]        removes and returns the item at the given index. Returns
                                    the rightmost item if the index is omitted
"""
dir(list)

cities = ["oslo", "delhi", "washington", "london", "seattle", "paris", "washington"]
cities.count("seattle")
cities.index("washington")
cities.reverse()
cities
cities.append("brussels")
cities
cities.sort()
cities
cities.pop()
cities
more_cities = ["brussels", "copenhagen"]
cities.extend(more_cities)
cities
cities.remove("brussels")
cities

"""
Populating Lists with items
    Start with empty list and use append() or extend() to add items
"""
continents = []
continents.append("Asia")
continents.append("Europe")
continents.append("Africa")
continents