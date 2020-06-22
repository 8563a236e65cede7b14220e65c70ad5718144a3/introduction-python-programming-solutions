"""
Program 6.3
Display the Index Values of Items in List
"""


def main():
    silicon_valley = ["google", "amd", "yahoo", "cisco", "oracle"]
    for index_value in range(len(silicon_valley)):
        print(f"The index value of '{silicon_valley[index_value]} is {index_value}")


if __name__ == "__main__":
    main()


