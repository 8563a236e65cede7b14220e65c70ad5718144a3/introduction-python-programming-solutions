"""
Program 9.14
Read and display rows in "employees.csv" that start
with employee name "Jerry"
"""
import csv


def main():
    with open("Chapter09/employees.csv", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        print("Print rows in CSV file that start with employee name 'Jerry'")
        for each_row in csv_reader:
            if each_row[0] == "Jerry":
                print(",".join(each_row))


if __name__ == "__main__":
    main()
