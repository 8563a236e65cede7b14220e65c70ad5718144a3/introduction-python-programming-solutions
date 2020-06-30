"""
Program 11.3
Calculate the Arc Length of an Angle by Assigning
Values to the Radius and Angle Data Attributes of
the class ArcLength
"""
import math


class ArcLength:
    def __init__(self):
        self.radius = 0
        self.angle = 0

    def calculate_arc_length(self):
        result = 2 * math.pi * self.radius * self.angle / 360
        print(f"Length of an Arc is {result}")


def main():
    al = ArcLength()
    al.radius = 9
    al.angle = 75

    print(f"Angle is {al.angle}")
    print(f"Radius is {al.radius}")
    al.calculate_arc_length()


if __name__ == "__main__":
    main()
