"""
Nested Lists
    A list inside another list is called a nested list and you
    can get the behaviour of nested lists in Python by storing
    lists within the elements of another list
    Traverse through items of a nested list using a for loop

    nested_list_name = [[item_1, item_2, item_3],
                        [item_4, item_5, item_6],
                        [item_7, item_8, item_9]]
"""
asia = [["India", "Japan", "Korea"],
        ["Srilanka", "Myanmar", "Thailand"],
        ["Cambodia", "Vietnam", "Isreal"]]


asia[0]
asia[0][1]
asia[1][2] = "Philippines"
asia

