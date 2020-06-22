"""
Review Question 24
Program to extract first n characters of a string
"""


def extract(string, n):
    return string[:n]

def main():
    user_string = input("Enter string\n")
    n = int(input("Enter number of characters to extract\n"))

    result = extract(user_string, n)
    print(f"The substring is\n{result}")


if __name__ == "__main__":
    main()


