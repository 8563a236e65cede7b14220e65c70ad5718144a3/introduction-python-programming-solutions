"""
Program 9.13
Read and display each row in "biostats.csv"
"""
import csv


def main():
    with open("Chapter09/biostats.csv", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        print("Print each row in CSV file")
        for each_row in csv_reader:
            print(",".join(each_row))


if __name__ == "__main__":
    main()
