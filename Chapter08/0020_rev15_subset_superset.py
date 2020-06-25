"""
Review Question 15
Demonstrate use of issubset and issuperset
"""


def main():
    alpha1 = set("abcdefghijklm")
    alpha2 = set("nopqrstuvwxyz")
    alphabets = alpha1.union(alpha2)

    print(f"Alpha1\n{alpha1}")
    print(f"Alpha2\n{alpha2}")
    print(f"Alphabets\n{alphabets}")

    print(f"alpha1.issubset(alphabets) = {alpha1.issubset(alphabets)}")
    print(f"alpha1.issuperset(alphabets) = {alpha1.issuperset(alphabets)}")
    print(f"alphabets.issuperset(alpha1) = {alphabets.issuperset(alpha1)}")


if __name__ == "__main__":
    main()
