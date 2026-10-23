"""
Matrix Row and Column Sums

This program reads a 3x3 matrix from the user (three rows, numbers
separated by spaces) and prints the sum of each row and each column.
"""


def read_matrix():
    """Read a 3x3 matrix from the user, row by row."""
    matrix = []
    for i in range(3):
        while True:
            try:
                row = list(map(int, input().split()))
                if len(row) != 3:
                    print("Please enter exactly 3 numbers.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter integers only.")
    return matrix


def row_sums(matrix):
    """Return a list with the sum of each row."""
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums


def column_sums(matrix):
    """Return a list with the sum of each column."""
    sums = []
    for j in range(3):
        total = 0
        for i in range(3):
            total += matrix[i][j]
        sums.append(total)
    return sums


def main():
    """Read the matrix and print row and column sums."""
    matrix = read_matrix()

    print("Row sums:")
    for i, total in enumerate(row_sums(matrix), start=1):
        print(f"Row {i}: {total}")

    print()
    print("Column sums:")
    for j, total in enumerate(column_sums(matrix), start=1):
        print(f"Column {j}: {total}")


main()
