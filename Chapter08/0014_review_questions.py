"""
Review Questions
1)  A tuple is a finite ordered list of values of possibly different
    types which is used to bundle related values together without
    having to create a specific type to hold them.
    Tuples are immutable

2)  Relation between Tuples and Lists
        Often used in different situations and for different
        purposes
        Tuples are immutable and usually contain a heterogeneous
        sequence of elements that are accessed via unpacking or
        indexing
        Lists are mutable and their items are accessed via indexing
        Items cannot be added, removed or replaced in a tuple

3)  You must use the set() function since {} creates an empty dictionary

4)  Slicing
        tuple_name[start:stop[:step]]
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

5)  Relation between Tuples and Dictionaries
        Tuples can be used as key:value pairs to build dictionaries

        fish_weight_kg = (
            ("white_shark", 520),
            ("beluga", 1571),
            ("greenland_shark", 1400)
        )

        fish_weight_kg_dict = dict(fish_weight_kg)
        fish_weight_kg_dict

6)  Using zip() Function
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

        x = [1, 2, 3]
        y = [4, 5, 6]
        zipped = zip(x, y)
        list(zipped)

7)  Set Methods
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

8)  Fronzenset
        A frozenset is basically the same as a set, except that it is
        immutable
        Since they are immutable, they can be used as members in other
        sets and as dictionary keys.
        Frozensets have the same functions as normal sets, except none
        of the functions that change the contents are available.

    fs = frozenset(["g","o","o", "d"])
    fs

    animals = set([fs, "cattle", "horse"])

    official_languages_world = {"english": 59, "french": 29, "spanish": 21}
    frozenset(official_languages_world)
    frs = frozenset(["german"])
    official_languages_world = {"english": 59, "french": 29, "spanish": 21, frs: 6}
    official_languages_world

9)  You cannot delete or remove items from tuples as they are
    an immutable type.

    For sets you can use
    discard()       set_name.discard(item)          removes an item from the set if it is present
    clear()         set_name.clear()                removes all the items from the set
    pop()           set_name.pop()                  removes and returns an arbitrary item from the set. It
                                                    raises KeyError if the set is empty
    remove()        set_name.remove(item)           removes an item from the set. It raises KeyError if
                                                    the item is not contained in the set
"""
