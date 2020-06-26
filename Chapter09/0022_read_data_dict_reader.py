"""
Program 9.16
Read Data from "pokemon.csv" csv File
Using DictReader
"""
import csv


def main():
    with open("Chapter09/pokemon.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"{row['Pokemon']}, {row['Type']}")


if __name__ == "__main__":
    main()
