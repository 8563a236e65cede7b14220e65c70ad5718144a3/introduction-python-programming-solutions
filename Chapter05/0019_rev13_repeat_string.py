"""
Review Question 13
Ask a user for a string and a number and then repeat
the string that number of times
"""


def repeat_string(string, times):
    print(string * times)


def main():
    user_string = input("Enter a string\n")
    times = int(input("Enter repeats"))
    repeat_string(user_string, times)


if __name__ == "__main__":
    main()


