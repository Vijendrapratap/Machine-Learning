"""
Suppose the age a student graduates from Salem State is Normally distributed. If the mean
age is 23.1 years and the standard deviation is 3.1 years, what is the probability that 6
randomly selected students had a mean age at graduation that was greater than 27?

"""

def prob(mean, standard_deviation, n, x):
    z_score = (x - mean) / (standard_deviation / (n ** 0.5))
    return z_score


mean = 23.1
standard_deviation = 3.1
n = 6
x = 27


print(prob(mean, standard_deviation, n, x))
print("Probability according to Ztable 0.9989")