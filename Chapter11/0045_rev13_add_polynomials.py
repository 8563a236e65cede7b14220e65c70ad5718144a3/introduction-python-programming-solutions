"""
Review Question 13
Add two polynomials using classes
"""


class Polynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        return Polynomial(self.a + other.a, self.b + other.b, self.c + other.c)

    def __str__(self):
        return f"{self.a}x^2 + {self.b}x + {self.c}"


def main():
    poly1 = Polynomial(1, 2, 3)
    poly2 = Polynomial(2, 2, 2)
    print(f"Polynomial 1 = {poly1}")
    print(f"Polynomial 2 = {poly2}")
    print(f"Polynomial 1 + Polynomial 2 = \n{poly1 + poly2}")


if __name__ == "__main__":
    main()
