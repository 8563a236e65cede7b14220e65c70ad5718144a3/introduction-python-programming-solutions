"""
Program 11.12
Illustrate Class Variables and Instance Variables
"""


class Dog:
    kind = "canine"
    def __init__(self, name):
        self.dog_name = name


def main():
    d = Dog("Fido")
    e = Dog("Buddy")
    print(f"Value for Shared Variable or Class Variable "
          f"'kind' is '{d.kind}'")
    print(f"Value for Shared Variable or Class Variable "
          f"'kind' is '{e.kind}'")
    print(f"Value for Unique Variable or Instance Variable"
          f"'dog_name' is '{d.dog_name}'")
    print(f"Value for Unique Variable or Instance Variable"
          f"'dog_name' is '{e.dog_name}'")


if __name__ == "__main__":
    main()
