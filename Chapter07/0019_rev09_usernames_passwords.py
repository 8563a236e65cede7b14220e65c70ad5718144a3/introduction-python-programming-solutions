"""
Review Question 9
Create a dictionary that contains usernames
as the key and passwords as the value.
Make up five entries and then demonstrate
the use of clear() and fromkeys()
"""


def create_pwd_shadow():
    pwd_shadow = {
        "A": "xyz",
        "B": "uvw",
        "C": "rst",
        "D": "opq",
        "E": "lmn"
    }
    return pwd_shadow


def new_pwd_list(pwd_shadow):
    return pwd_shadow.fromkeys(pwd_shadow)


def clear_pwd_list(pwd_shadow):
    pwd_shadow.clear()


def main():
    pwd_shadow = create_pwd_shadow()
    print(f"Shadow file\n{pwd_shadow}")
    new_shadow = new_pwd_list(pwd_shadow)
    print(f"New Shadow dictionary\n{new_shadow}")
    clear_pwd_list(pwd_shadow)
    print(f"Cleared shadow file\n{pwd_shadow}")


if __name__ == "__main__":
    main()
