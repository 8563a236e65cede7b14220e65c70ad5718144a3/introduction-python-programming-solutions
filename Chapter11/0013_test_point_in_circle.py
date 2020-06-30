"""
Program 11.10
Given the Coordinates (x,y) of a Center of a Circles and
Its Radius, Determine Whether the Point Lies Inside the
Circle, On the Circle or Outside the Circle
"""


class Circle:
    def __init__(self, radius=0, circle_x=0, circle_y=0, point_x=0, point_y=0):
        self.radius = radius
        self.circle_x_coord = circle_x
        self.circle_y_coord = circle_y
        self.point_x_coord = point_x
        self.point_y_coord = point_y
        self.status = ""

    def check_point_status(self):
        x_diff2 = (self.point_x_coord - self.circle_x_coord) ** 2
        y_diff2 = (self.point_y_coord - self.circle_y_coord) ** 2
        r2 = self.radius ** 2
        if x_diff2 + y_diff2 < r2:
            self.status = f"Point with coordinates " \
                          f"{(self.point_x_coord, self.point_y_coord)} " \
                          f"is inside the Circle"
        elif x_diff2 + y_diff2 > r2:
            self.status = f"Point with coordinates " \
                          f"{(self.point_x_coord, self.point_y_coord)} " \
                          f"is outside the Circle"
        else:
            self.status = f"Point with coordinates " \
                          f"{(self.point_x_coord, self.point_y_coord)} " \
                          f"is on the Circle"
        return self


def main():
    point = Circle(10, 2, 3, 9, 9)
    returned_object = point.check_point_status()
    print(returned_object.status)
    print(f"Is point an instance of Circle Class? "
          f"{isinstance(point, Circle)}")
    print(f"Is returned_object an instance of Circle Class? "
          f"{isinstance(returned_object, Circle)}")
    print(f"Identity of the location of a point object is {id(point)}")
    print(f"Identity of the location of returned_object is "
          f"{id(returned_object)}")


if __name__ == "__main__":
    main()
