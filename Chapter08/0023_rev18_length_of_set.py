"""
Review Question 18
Length of Set
"""


def length(set_to_count):
    count = 0
    for element in set_to_count:
        count += 1
    return count


def main():
    alphabets = set("abcdefg")
    print(f"Length = {length(alphabets)}")


if __name__ == "__main__":
    main()
