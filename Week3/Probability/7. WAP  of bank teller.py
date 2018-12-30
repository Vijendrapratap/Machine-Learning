"""
A bank teller serves customers standing in the queue one by one.
Suppose that the service time XiXi for customer ii has mean EXi=2EXi=2 (minutes) and Var(Xi)=1Var(Xi)=1.
We assume that service times for different bank customers are independent.
Let YY be the total time the bank teller spends serving 5050 customers.
Write a program to find P(90<Y<110)
"""



def probability(mean, standard_deviation, n, x1, x2):
    z_score1 = (x1 - mean * n) / (standard_deviation * (n ** 0.5))
    z_score2 = (x2 - mean * n) / (standard_deviation * (n ** 0.5))
    return z_score1,z_score2


mean = 2
standard_deviation = 1 ** 0.5
n = 50
x1 = 90
x2 = 110

print(probability(mean, standard_deviation, n, x1, x2))
z = 0.9207 - 0.793
print("Probability = ", z)