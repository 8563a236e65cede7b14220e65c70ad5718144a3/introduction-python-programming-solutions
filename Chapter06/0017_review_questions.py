"""
Review Questions

1)  Lists avoid having a separate variable to store each item which is
    less efficient and more error prone when you have to perform some
    operations on these items.
    Lists are flexible because they can have values added, removed
    and changed
    Lists allow you to store heterogeneous data types

2)  A list can be created in a few ways
        a_list = list()
        a_list = []

3)  List Methods
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

4)  A list inside another list is called a nested list and you
    can get the behaviour of nested lists by storing lists
    within the elements of another list
    You can traverse through the items of nested lists using the for
    loop
        nested_list_name = [[item_1, item_2, item_3],
                            [item_4, item_5, item_6],
                            [item_7, item_8, item_9]]

        asia = [["India", "Japan", "Korea"],
                ["Srilanka", "Myanmar", "Thailand"],
                ["Cambodia", "Vietnam", "Isreal"]]
        asia[0]
        asia[0][1]
        asia[1][2] = "Philippines"
        asia

5)  Slicing of lists is allowed in Python wherein a part of
    the list can be extracted by specifying index range along with
    the colon (:) operator which itself is a list
        list_name[start:stop[:step]]
    where both start and stop are integer values. Includes start
    value but excludes the stop index value. Step specifies the
    increment value to slice by and is optional
    fruits = ["grapefruit", "pineapple", "blueberries", "mango", "banana"]
    fruits[1:3]
    fruits[:3]
    fruits[2:]
    fruits[1:4:2]
    fruits[:]
    fruits[::2]
    fruits[::-1]
    fruits[-3:-1]

6)  a)
        pop()       list.pop([index]        removes and returns the item at the given index. Returns
                                            the rightmost item if the index is omitted
        remove()    list.remove(item)       searches for the first instance of the given item in the
                                            list and removes it. If the item is not present in the
                                            list then ValueError is thrown
    b)  You can remove an item from a list based on its index rather
        than its value. Difference between del statement and pop()
        is that the del statement does not return any value
        Del statement can also be used to remove slices from a list
        or clear an entire list
    c)
        append()    list.append(item)       adds a single item to the end of the list.
                                            Does not return a new list and just modifies
                                            the original
        insert()    list.insert(index,item) inserts the item at the given index, shifting
                                            items to the right
"""