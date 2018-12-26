"""
Write a program to find inverse matrix
"""

def transpose(matrix):
    trans = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            trans[i][j] = matrix[j][i]

    return trans

def minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def deternminant(matrix):
    #base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    d = 0
    for c in range(len(matrix)):
        d += ((-1)**c)*matrix[0][c]*deternminant(minor(matrix,0,c))
    return d

def inverse(matrix):
    d = deternminant(matrix)
    #special case for 2x2 matrix:
    if len(matrix) == 2:
        return [[matrix[1][1]/d, -1*matrix[0][1]/d],
                [-1*matrix[1][0]/d, matrix[0][0]/d]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            m = minor(matrix,r,c)
            cofactorRow.append(((-1)**(r+c)) * deternminant(m))
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/d
    return cofactors

x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
inv = inverse(x)
print(inv)