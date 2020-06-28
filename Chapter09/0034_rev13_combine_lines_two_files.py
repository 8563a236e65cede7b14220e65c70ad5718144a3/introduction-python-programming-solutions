"""
Review Question 13
Combine each line from first file with correspond line in second file
"""


def combine(filename1, filename2):
    f1_list = list()
    f2_list = list()
    with open(filename1, "r") as f1, open(filename2) as f2:
        f1_list = f1.readlines()
        f2_list = f2.readlines()
        n1 = len(f1_list)
        n2 = len(f2_list)
        n_min = min(n1, n2)
        for i in range(0, n_min):
            print(f1_list[i].replace("\n", "") +
                  " " + f2_list[i].replace("\n", ""))


def main():
    filename1 = input("Enter first filename ")
    filename2 = input("Enter second filename ")
    combine(filename1, filename2)


if __name__ == "__main__":
    main()
