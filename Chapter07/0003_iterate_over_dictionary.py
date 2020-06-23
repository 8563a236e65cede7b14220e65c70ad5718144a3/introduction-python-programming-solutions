"""
Program 7.2
Illustrate Traversing of key:value Pairs in Dictionaries
Using for Loop
"""
currency = {"India": "Rupee", "USA": "Dollar", "Russia": "Ruble", "Japan": "Yen", "Germany": "Euro"}


def main():
    print("List of Countries")
    for key in currency.keys():
        print(key)
    print("List of Currencies in Different Countries")
    for value in currency.values():
        print(value)
    for key, value in currency.items():
        print(f"'{key}' has currency of type '{value}'")


if __name__ == "__main__":
    main()
