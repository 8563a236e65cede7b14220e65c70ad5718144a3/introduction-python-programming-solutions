"""
Review Question 19
Store latitude and longitude of your house
as tuple
"""


def main():
    lat = int(input("Enter latitude "))
    long = int(input("Enter longitude "))

    lat_long_tuple = (lat, long)

    print(f"Latitude and longitude of house {lat_long_tuple}")


if __name__ == "__main__":
    main()
