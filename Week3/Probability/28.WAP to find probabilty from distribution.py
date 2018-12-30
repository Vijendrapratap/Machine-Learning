"""
While checking receipts at Reds, it was determined that the average amount spent on food
per table was $21.50 with a standard deviation of $2.22. If we can assume that the amount of
money spent was Normally distributed, what is the probability that the average of 8 checks
is between $20 and $23?

"""

def probability(mean, standard_deviation, n, x1, x2):
    z_score1 = (x1 - mean) / (standard_deviation / (n ** 0.5))
    z_score2 = (x2 - mean) / (standard_deviation / (n ** 0.5))
    return z_score1, z_score2


mean = 28.3
standard_deviation = 2.3
n = 10
event1 = 20
event2 = 23

z1, z2 = probability(mean, standard_deviation, n, event1, event2)
print(z1, z2)
z = 0.9706 - 0.0294
print("Probability = ",z)