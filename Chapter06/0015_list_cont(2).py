"""
Del statement
    You can remove an item from a list based on its index rather
    than its value
    Difference between del statement and pop() is that the del
    statement does not return any value
    Del statement can also be used to remove slices from a list
    or clear an entire list
"""
a = [5, -8, 99.99, 432, 108, 213]
a
del a[0]
a
del a[2:4]
a
del a[:]
a