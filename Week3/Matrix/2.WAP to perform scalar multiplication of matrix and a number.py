"""
Write a program to perform scalar multiplication of matrix and a number

"""

x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
y = 9
result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(x)):
    for j in range(len(x)):

        result[i][j] = y * x[i][j]

print(result)