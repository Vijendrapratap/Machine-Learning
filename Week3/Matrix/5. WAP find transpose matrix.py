"""
Write a program to find transpose matrix

"""
y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
trans = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(y)):
    for j in range(len(y)):
        trans[i][j] = y[j][i]

print("Given Matrix is: ",y)
print("Transpose of Matrix is : ",trans)