"""
Bytes
    bytes(source[,encoding])
    where source is used to create a bytes object. It can be an
    integer or string
    bytes() class method returns a new bytes object
    bytes objects actually behave like immutable sequences of integers,
    with each value in the sequence ranging from 0 to 255

"""
print(b"Hello")
type(b"Hello")

for i in b"Hello":
    print(i)

bytes(3)
bytes([70])
bytes([72, 101, 108, 108, 111])
print(b"\x61")
bytes("Hi", "utf-8")

"""
The Pickle Module
    Pickle can take almost any Python object and convert it to a string
    representation. This process is called pickling.
    Reconstructing the object from string representation is called
    unpickling
        If you have object x and a file object f which has been opened for
        writing, then the simplest way to pick the object is
            pickle.dump(x, f)
        dump() writes a pickled representation of object x to the open
        file object f.
        
        If f is a file object which has been opened for reading, then
        the simplest way to unpickle the object is
        x = pickle.load(f)
        load() reads a pickled object representation from the open file
        object f and returns the reconstituted object hierachy specified
        therein.
        
        Pickling is the standard way to make Python objects persistent.
"""