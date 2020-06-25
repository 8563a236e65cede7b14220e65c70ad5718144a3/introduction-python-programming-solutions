"""
Fronzenset
    A frozenset is basically the same as a set, except that it is
    immutable
    Since they are immutable, they can be used as members in other
    sets and as dictionary keys.
    Frozensets have the same functions as normal sets, except none
    of the functions that change the contents are available.
"""
dir(frozenset)

fs = frozenset(["g","o","o", "d"])
fs

animals = set([fs, "cattle", "horse"])

official_languages_world = {"english": 59, "french": 29, "spanish": 21}
frozenset(official_languages_world)
frs = frozenset(["german"])
official_languages_world = {"english": 59, "french": 29, "spanish": 21, frs: 6}
official_languages_world
