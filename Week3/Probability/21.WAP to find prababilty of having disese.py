"""
HIV The New York State Health Department reports a 10% rate of the HIV virus
for the “at-risk” population. Under certain conditions, a preliminary screening test
for the HIV virus is correct 95% of the time. (Subjects are not told that they are
HIV infected until additional tests verify the results.) If someone is randomly
selected from the at-risk population, what is the probability that they have the
HIV virus if it is known that they have tested positive in the initial screening?

"""

prob_HIV = 0.1
prob_no_HIV = 0.9
prob_pisotive_given_HIV = 0.95
prob_negative_given_HIV = 0.05

probability_HIV_given_positive = (prob_HIV * prob_pisotive_given_HIV)/(prob_HIV * prob_pisotive_given_HIV + prob_no_HIV*prob_negative_given_HIV)
print("Probability of getting HIV when result is positive ",probability_HIV_given_positive)