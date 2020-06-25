"""
Using zip() Function
The zip() function makes a sequence that aggregates elements from
each of the iterables (can be zero or more).
    zip(*iterables)

An iterable can be a list, string, or dictionary. It returns a sequence
of tuples where the i-th tuple contains the i-th element from each of
the iterables.
The aggregation of elements stops when the shortest input iterable is exhausted.
    e.g. if you pass one iterable with two items and another with five,
    the zip() function returns a sequence of two tuples.
With a single iterable argument, it returns an iterator of one
tuple. With no arguments, it returns an empty iterator
"""
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)

"""
To loop over two or more sequences at the same time, the entries
can be paired with the zip() function
"""
questions = ("name", "quest", "favourite color")
answers = ("lancelot", "the holy grail", "blue")
for q, a in zip(questions, answers):
    print(f"What is your {q}? It is {a}")

"""
Sets
    Python also includes a data type for sets. A set is an unordered
    collection with no duplicate items. Primary uses of sets include
    membership testing and eliminating duplicate entries.
    Sets also support mathematical operations, such as union, 
    intersection, difference, and symmetric difference.
    Curly braces or the set() function can be used to create sets 
    with a comma-separated list of items inside curly brackets {}.
    To create an empty set, you must use set() and not {} as the
    latter creates an empty dictionary.
"""
basket = {
    "apple",
    "orange",
    "apple",
    "pear",
    "orange",
    "banana"
}

print(basket)

"orange" in basket
"crabgrass" in basket

a = set("abracadabra")
b = set("alacazam")
a
b
a - b
a & b
a | b
a ^ b
len(basket)
sorted(basket)

"""
Sets are mutable
Indexing is not possible in sets, since set items are unordered.
You cannot access or change an item of the set using indexing
or slicing

Set Methods
add()           set_name.add(item)              adds an item to the set
clear()         set_name.clear()                removes all the items from the set
difference()    set_name.difference(*others)    returns a new set with the items in the set
                                                set_name that are not in the others set
discard()       set_name.discard(item)          removes an item from the set if it is present
intersection()  set_name.intersection(*others)  returns a new set with items common to the set
                                                and all others sets
isdisjoint()    set_name.isdisjoint(other)      returns True if set has no items in common with
                                                other set. Sets are disjoint if and only if
                                                their intersection is the empty set
issubset()      set_name.issubset(other)        returns True if every item in the set is in other set
issuperset()    set_name.issuperset(other)      returns True if every element in other set is in the set
pop()           set_name.pop()                  removes and returns an arbitrary item from the set. It 
                                                raises KeyError if the set is empty
remove()        set_name.remove(item)           removes an item from the set. It raises KeyError if
                                                the item is not contained in the set
symmetric_      set_name.symmetric              returns a new set with items in either the set or other
 difference()    difference(other)              but not both
union()         set_name.union(*others)         returns new set with items from set and all others sets
update()        set_name.update(*others)        update the set by adding items from all others sets
"""
dir(set)

european_flowers = {
    "sunflowers",
    "roses",
    "lavender",
    "tulips",
    "goldcrest"
}

american_flowers = {
    "roses",
    "tulips",
    "lilies",
    "daisies"
}


american_flowers
american_flowers.add("orchids")
american_flowers

american_flowers.difference(european_flowers)
american_flowers.intersection(european_flowers)
american_flowers.isdisjoint(european_flowers)
american_flowers.issuperset(european_flowers)
american_flowers.issubset(european_flowers)
american_flowers.symmetric_difference(european_flowers)
american_flowers.union(european_flowers)
american_flowers.update(european_flowers)
american_flowers

american_flowers.issuperset(european_flowers)
american_flowers.issubset(european_flowers)

american_flowers.discard("roses")
american_flowers
european_flowers.pop()
european_flowers
american_flowers.clear()
american_flowers
