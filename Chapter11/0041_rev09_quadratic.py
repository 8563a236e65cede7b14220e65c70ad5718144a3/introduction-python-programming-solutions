"""
Review Question 9
Create a class named quadratic, where a, b and c are data attributes
and the methods are
    a) __init__() to initialize the data attributes
    b) roots() to compute the quadratic equation
"""
import math


class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def roots(self):
        b2_4ac = self.b ** 2 - 4 * self.a * self.c
        if b2_4ac < 0:
            print("No real roots")
        else:
            x1 = (-self.b - math.sqrt(b2_4ac)) / (2 * self.a)
            x2 = (-self.b + math.sqrt(b2_4ac)) / (2 * self.a)
            print(f"The roots are {(x1, x2)}")


def main():
    quad = Quadratic(1, -5, 6)
    quad.roots()


if __name__ == "__main__":
    main()
