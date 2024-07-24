def mat_mult(mat, rows, m):
    result = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]

    for _ in range(m):
        mul = [[0 for _ in range(rows)] for _ in range(rows)]
        for i in range(rows):
            for j in range(rows):
                for k in range(rows):
                    mul[i][j] += result[i][k] * mat[k][j]
        result = mul

    for row in result:
        print(row)

rows = int(input("Enter the dimensions of the square matrix: "))
mat = []
matrix1 = []

print("Enter the elements of the matrix row by row:")
for i in range(rows):
    a = []
    for j in range(rows):
        a.append(int(input(f"Element [{i + 1}][{j + 1}]: ")))
    mat.append(a)
m = int(input("Enter the argument: "))
mat_mult(mat, rows, m)