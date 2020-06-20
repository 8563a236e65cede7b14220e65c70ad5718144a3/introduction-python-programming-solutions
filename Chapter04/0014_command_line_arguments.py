'''
Program 4.12
Demonstrate Command Line Arguments in Python

You need to import the sys module to access command
line arguments. All command line arguments can be printed
as a list of strings by executing sys.argv
'''

import sys

def main():
    print(f"sys.argv prints all the arguments at the command line including file names {sys.argv}")
    print(f"len(sys.argv) prints the total number of command line arguments including file name {len(sys.argv)}")
    print("You can use a for loop to traverse through sys.argv")

    for arg in sys.argv:
        print(arg)

if __name__ == "__main__":
    main()