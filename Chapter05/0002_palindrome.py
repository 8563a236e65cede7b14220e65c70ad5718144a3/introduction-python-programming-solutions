"""
Program 5.1
Determine whether a Given String is a
Palindrome or not using slicing
"""

def main():
    user_string = input("Enter string:\n")
    if user_string == user_string[::-1]:
        print("User entered string is a palindrome")
    else:
        print("User entered string is not a palindrome")


if __name__ == "__main__":
    main()

