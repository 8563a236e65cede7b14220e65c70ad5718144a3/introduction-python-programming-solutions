"""
Review Question 14
Format date string from forward slashes to hyphens
"""


def replace_slash(string):
    print(string.replace("/","-"))


def main():
    user_string = input("Enter string in dd/mm/yyyy format\n")
    replace_slash(user_string)


if __name__ == "__main__":
    main()


