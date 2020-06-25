"""
Review Question 17
Write a program to clear a set
"""


def clear1(set_to_clear):
    while True:
        try:
            set_to_clear.pop()
        except KeyError:
            break


def clear2(set_to_clear):
    temp_set = set(set_to_clear)
    for element in temp_set:
        set_to_clear.remove(element)


def clear3(set_to_clear):
    temp_set = set(set_to_clear)
    for element in temp_set:
        set_to_clear.discard(element)


def main():
    alphabets = set("abcdefg")
    print(f"Alphabets\n{alphabets}")
    print(f"Method 1 pop()")
    clear1(alphabets)
    print(f"Alphabets\n{alphabets}\n")

    alphabets = set("abcdefg")
    print(f"Alphabets\n{alphabets}")
    print(f"Method 2 remove()")
    clear2(alphabets)
    print(f"Alphabets\n{alphabets}\n")

    alphabets = set("abcdefg")
    print(f"Alphabets\n{alphabets}")
    print(f"Method 3 discard()")
    clear3(alphabets)
    print(f"Alphabets\n{alphabets}\n")


if __name__ == "__main__":
    main()
