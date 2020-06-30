"""
Program 11.13
Demonstrate the Difference between Abstraction and Encapsulation
"""


class foo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


def main():
    foo_object = foo(3, 4)
    print(foo_object.add())


if __name__ == "__main__":
    main()
