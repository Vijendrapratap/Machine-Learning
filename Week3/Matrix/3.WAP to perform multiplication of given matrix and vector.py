"""
Write a program to perform multiplication of given matrix and vector

"""
x = [[5, 1, 3], [1, 1 ,1], [1, 2 ,1]]
y = [1, 2, 3]

#since y*x is possible only of order 1x3
result = [0, 0, 0]

for i in range(len(y)):
    for j in range(len(x)):
        for k in range(len(x)):
            result[i] += x[j][k] * y[i]

print("The resultant matrix is y*x is : ",result)