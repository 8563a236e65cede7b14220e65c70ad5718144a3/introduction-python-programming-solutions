"""
Review Question 12
Create a dictionary that contains author name
as the key and ISBN as the value.
Make up five entries and then demonstrate
the use of clear() and fromkeys()
"""


def create_author_isbn():
    author_isbn = {
        "A": "xyz",
        "B": "uvw",
        "C": "rst",
        "D": "opq",
        "E": "lmn"
    }
    return author_isbn


def new_author_isbn_dict(author_isbn):
    return author_isbn.fromkeys(author_isbn)


def clear_author_isbn(author_isbn):
    author_isbn.clear()


def main():
    author_isbn = create_author_isbn()
    print(f"Author ISBN dictionary\n{author_isbn}")
    new_author_isbn = new_author_isbn_dict(author_isbn)
    print(f"New Author ISBN dictionary\n{new_author_isbn}")
    clear_author_isbn(author_isbn)
    print(f"Cleared Author ISBN dictionary\n{author_isbn}")


if __name__ == "__main__":
    main()
