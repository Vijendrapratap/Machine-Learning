"""
The average age of major league baseball players is 28.3 years and has a standard deviation
of 2.3 years. If we can assume that ages are Normally distributed, what is the probability
that the average age of 10 randomly selected Red Sox players is less than 27 years?

"""

def probability(mean, standard_deviation, n, x):
    z_score = (x - mean) / (standard_deviation / (n ** 0.5))
    return z_score


g_mean = 28.3
g_standard_deviation = 2.3
g_n = 10
g_x = 27


print(probability(g_mean, g_standard_deviation, g_n, g_x))

print("Probability according to Z table 0.375")