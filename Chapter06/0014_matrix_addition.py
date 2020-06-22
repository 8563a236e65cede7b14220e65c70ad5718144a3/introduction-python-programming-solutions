"""
Program 6.12
Matrix Addition
"""
matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]


matrix_2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]


matrix_result = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]


def main():
    for rows in range(len(matrix_1)):
        for columns in range(len(matrix_2[0])):
            matrix_result[rows][columns] = matrix_1[rows][columns] + matrix_2[rows][columns]
    print("Addition of two matrices is")
    for items in matrix_result:
        print(items)


if __name__ == "__main__":
    main()


