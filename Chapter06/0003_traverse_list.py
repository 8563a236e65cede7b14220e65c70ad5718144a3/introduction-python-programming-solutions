"""
Program 6.2
Illustrate Traversing of Lists Using the for loop
"""


def main():
    fast_food = ["waffles", "sandwich", "burger", "fries"]
    for each_food_item in fast_food:
        print(f"I like to eat {each_food_item}")

    for each_food_item in ["waffles", "sandwich", "burger", "fries"]:
        print(f"I like to eat {each_food_item}")


if __name__ == "__main__":
    main()


