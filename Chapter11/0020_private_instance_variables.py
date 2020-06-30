"""
Program 11.15
Demonstrate Private Instance Variables
"""


class PrivateDemo:
    def __init__(self):
        self.nonprivateinstance = "I'm not a private instance"
        self.__privateinstance = "I'm a private instance"

    def display_privateinstance(self):
        print(f"{self.__privateinstance} used within the method of a class")


def main():
    demo = PrivateDemo()
    print("Invoke Method having private instance")
    print(demo.display_privateinstance())
    print("Invoke non-private instance variable")
    print(demo.nonprivateinstance)
    print("Get attributes of the object")
    print(demo.__dict__)
    print("Trying to access private instance variable outside"
          " the class results in an error")
    print(demo.__privateinstance)   #AttributeError


if __name__ == "__main__":
    main()
