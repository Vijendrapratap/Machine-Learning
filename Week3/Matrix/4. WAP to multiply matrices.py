"""
Write a program to multiply matrices

"""

def matrix_prod(x, y):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]
    return (result)


mat1 = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]

result1 = matrix_prod(mat1, mat2)
result2 = matrix_prod(mat2, mat1)

print("Product of matrix1 x matrix2 is : ", result1)
print("Product of matrix2 x matrix1 is : ", result2)