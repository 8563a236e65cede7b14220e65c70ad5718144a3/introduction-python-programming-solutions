"""
Program 7.4
Count the Number of Times an Iteem
Appears in the List
"""
novels = [
    "gone_girl",
    "davinci_code",
    "game_of_thrones",
    "gone_girl",
    "davinci_code"
]


def main():
    count_items = dict()
    for book_name in novels:
        count_items[book_name] = count_items.get(book_name, 0) + 1
    print("Number of times a novelappears in the list is ")
    print(count_items)


if __name__ == "__main__":
    main()
