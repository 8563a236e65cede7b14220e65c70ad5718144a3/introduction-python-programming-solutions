"""
Review Question 11
Write a Program to unpack a tuple to several variables
"""


def main():
    my_tuple = ("a", "b", "c", "d")
    (a, b, c, d) = my_tuple
    print(f"Tuple\n{my_tuple}")
    print(f"a={a}\nb={b}\nc={c}\nd={d}")


if __name__ == "__main__":
    main()
