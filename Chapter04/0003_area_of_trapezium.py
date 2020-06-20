'''
Program 4.2
Find area of Trapezium Using the Formula
Area = (1/2) * (a + b) * h
    a and b are the two bases
    h is the height
'''

def area_trapezium(a, b, h):
    area = 0.5 * (a + b) * h
    print(f"Area of A Trapezium is {area}")

def main():
    area_trapezium(10, 15, 20)

if __name__ == "__main__":
    main()
