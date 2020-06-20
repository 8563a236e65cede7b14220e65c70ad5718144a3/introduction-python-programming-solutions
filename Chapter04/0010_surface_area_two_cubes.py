'''
Program 4.7
Calculate and add the surface area of two cubes using
nested functions
'''

def add_cubes(a, b):
    def cube_surface_area(x):
        return 6 * pow(x, 2)
    return cube_surface_area(a) + cube_surface_area(b)

def main():
    result = add_cubes(2,3)
    print(f"The surface area after adding two CUbes is {result}")

if __name__ == "__main__":
    main()
