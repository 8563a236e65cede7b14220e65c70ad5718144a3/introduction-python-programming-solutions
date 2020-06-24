"""
Review Questions

1)  A dictionary is a collection of an unordered set of key:value
    pairs, with the requirement that the keys are unique within
    a dictionary. Unlike lists which are index by numbers,
    dictionaries are indexed by keys which are useful when
    the underlying data is represented by some form of key value
    relationship

2)  A dictionary can be created in a variety of ways
        dict1 = {}
        dict2 = dict()
        dict3 = {key_1: value_1, ..., key_n: value_n}
        dict4 = dict([("a",1), ("b", 2)])

3)
    keys()          dict_name.keys()        returns a new view consisting of all the keys in the dictionary
    values()        dict_name.values()      returns a new view consisting of all the values in the dictionary
    get()           dict_name.get(key       returns the value associated with the specified key
                    [,default])             in the dictionary. If key is not present, then it
                                            returns the default value. If default not given,
                                            defaults to None, so that this method never raises a
                                            KeyError
    clear()         dict_name.clear()       removes all key:value pairs from the dictionary

4)  The use of dictionaries within dictionaries is called nesting
    of dictionaries. You can assign a dictionary as a value to a
    key inside another dictionary

    student_details = {
        "name": "jasmine",
        "registration_number": "X1",
        "marks": {"python": 95, "java": 90}
    }
"""