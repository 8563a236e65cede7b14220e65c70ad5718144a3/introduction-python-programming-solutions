"""
Review Question 10
Make a list of the first eight letters of the alphabet,
then using the slice operation do the following:
    a) Print the first three letters of the alphabet
    b) Print any three letters from the middle
    c) Print the letters from any index to the end
"""


def main():
    alphabets = list("abcdefgh")

    print(f"First three letters\n{alphabets[:3]}")
    print(f"Middle letters\n{alphabets[4:7]}")
    print(f"Index to end\n{alphabets[3:]}")


if __name__ == "__main__":
    main()


