"""
Program 11.8
Demonstrate Passing of an Object as an
Argument to a Function Call
"""


class Track:
    def __init__(self, song, artist):
        self.song = song
        self.artist = artist


def print_track_info(vocalist):
    print(f"Song is '{vocalist.song}'")
    print(f"Artist is '{vocalist.artist}'")


def main():
    singer = Track("The First Time I Ever Saw Your Face",
                   "Roberta Flack")
    print_track_info(singer)


if __name__ == "__main__":
    main()
