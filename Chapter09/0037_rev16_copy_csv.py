"""
Review Question 16
Read and write the contents from one csv file to another
"""
import csv


def copy_csv():
    with open("Chapter09/pokemon.csv", "r") as in_file, open("Chapter09/pokemon2.csv", "w") as out_file:
        csvreader = csv.reader(in_file)
        csvwriter = csv.writer(out_file)
        for each_row in csvreader:
            csvwriter.writerow(each_row)


def main():
    copy_csv()


if __name__ == main():
    main()
