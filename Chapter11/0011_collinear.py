"""
Program 11.9
Given Three Points (x1, y1), (x2, y2) and (x3, y2)
Check if they are Collinear
"""


class Collinear:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def check_for_collinear(self, point_2_obj, point_3_obj):
        a = (point_3_obj.y_coord - point_2_obj.y_coord) * (point_2_obj.x_coord - self.x_coord)
        b = (point_2_obj.y_coord - self.y_coord) * (point_3_obj.x_coord - point_2_obj.x_coord)
        if a == b:
            print("Points are Collinear")
        else:
            print("Points are not Collinear")


def main():
    point_1 = Collinear(1, 5)
    point_2 = Collinear(2, 5)
    point_3 = Collinear(4, 5)
    point_1.check_for_collinear(point_2, point_3)


if __name__ == "__main__":
    main()
