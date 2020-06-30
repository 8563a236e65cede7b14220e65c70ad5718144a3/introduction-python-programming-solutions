"""
Review Questions

1)  A class is a blueprint from which individual objects are created.
    An object is a bundle of related state (variables) and behaviour
    (methods).
    Objects contain variables, which represents the state information
    about the thing you are trying to model, and the methods represent
    the behaviour or functionality that you want to have
    A particular car e.g. VW beetle would be an object of the class
    vehicle

2)  The __init__() method defines and initializes the instance variables.
    It is invoked as soon as an object of a class is instantiated.
    The __init__() method for a newly created object is automatically
    executed with all of its parameters.

3)  Data attributes are instance variables that are unique to each
    object of a class, and Class attributes are class variables that
    is shared by all objects of a class.

4)  Encapsulation is the process of combining variables that store data
    and methods that work on those variables into a single unit called
    class.
    The variables are not accessed directly, they are accessed through
    the methods present in the class.
    Encapsulation ensures that the object's internal representation
    (its state and behaviour) are hidden from the rest of the application
    Thus, encapsulation makes data hiding possible.

    class foo:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def add(self):
            return self.a + self.b


    foo_object = foo(3,4)
    foo_object.add()

5)  Single inheritance is when a derived class inherits from only
    a single base class
    class A:
        pass
    class B(A):
        pass
    Multiple inheritance is when a derived class inherits from
    more than one base class
    class A:
        pass
    class B:
        pass
    class C(A, B):
        pass

6)  class Country:
        def __init__(self, country_name):
            self.country_name = country_name

        def country_details(self):
            print(f"Happiest Country in the world is {self.country_name}")


    class HappiestCountry(Country):
        def __init__(self, country_name, continent):
            super().__init__(country_name)
            self.continent = continent

        def happy_country_details(self):
            print(f"Happiest Country in the world is {self.country_name} "
                  f"and is in {self.continent}")


    def main():
        finland = HappiestCountry("Finland", "Europe")
        finland.happy_country_details()

7)  Polymorphism means that you can have multiple classes where each
    class implements the same variables or methods in different ways.

    class Vehicle:
        def __init__(self, model):
            self.model = model

        def vehicle_model(self):
            print(f"Vehicle Model name is {self.model}")


    class Bike(Vehicle):
        def vehicle_model(self):
            print(f"Vehicle Model name is {self.model}")


    class Car(Vehicle):
        def vehicle_model(self):
            print(f"Vehicle Model name is {self.model}")


    class Aeroplane:
        pass


    def vehicle_info(vehicle_obj):
        vehicle_obj.vehicle_model()


    def main():
        ducati = Bike("Ducati-Scrambler")
        beetle = Car("Volkswagon-Beetle")
        boeing = Aeroplane()

        for each_obj in [ducati, beetle, boeing]:
            try:
                vehicle_info(each_obj)
            except AttributeError:
                print("Expected method not present in the object")

8)  Operator Overloading is a specific case of polymorphism, where
    different operators have different implementations depending
    on their arguments. A class can implement certain operations
    that are invoked by a special syntax by defining methods
    with special names called Magic Methods.

    class Complex:
        def __init__(self, real, imaginary):
            self.real = real
            self.imaginary = imaginary

        def __add__(self, other):
            return Complex(self.real + other.real, self.imaginary + other.imaginary)

        def __str__(self):
            return f"{self.real} + i{self.imaginary}"


    def main():
        complex_number_1 = Complex(4, 5)
        complex_number_2 = Complex(2, 3)
        complex_number_sum = complex_number_1 + complex_number_2
        print(f"Addition of two complex numbers {complex_number_1} and "
              f"{complex_number_2} is {complex_number_sum}")
"""