'''
Program 4.3
Demonstrate Using the Same Variable Name in Calling
Function and Function Definition
    arguments passed by the calling program and the parameters
    used to receive the values in the function definition may
    have the same variable names
        exist in different scopes however and thus independent
'''

god_name = input("Who is the God of Seas according to Greek Mythology?")

def greek_mythology(god_name):
    print(f"The God of seas according to Greek Mythology is {god_name}")

def main():
    greek_mythology(god_name)

if __name__ == "__main__":
    main()
