def mat_mult(mat, rows, m):
    # Initialize the result matrix as the identity matrix of size 'rows x rows'
    result = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]

    # Multiply the matrix 'm' times
    for _ in range(m):
        # Initialize a temporary matrix to store multiplication results
        mul = [[0 for _ in range(rows)] for _ in range(rows)]

        # Perform matrix multiplication
        for i in range(rows):
            for j in range(rows):
                for k in range(rows):
                    mul[i][j] += result[i][k] * mat[k][j]

        # Update the result matrix with the multiplication result
        result = mul

    # Print the resulting matrix after m multiplications
    for row in result:
        print(row)


# Get the dimensions of the square matrix from the user
rows = int(input("Enter the dimensions of the square matrix: "))
mat = []

# Prompt the user to enter the elements of the matrix row by row
print("Enter the elements of the matrix row by row:")
for i in range(rows):
    a = []
    for j in range(rows):
        a.append(int(input(f"Element [{i + 1}][{j + 1}]: ")))
    mat.append(a)

# Get the argument 'm' from the user, indicating how many times to multiply the matrix
m = int(input("Enter the argument: "))

# Call the matrix multiplication function
mat_mult(mat, rows, m)
