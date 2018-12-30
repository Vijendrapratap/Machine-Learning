"""
A diagnostic test has a probability 0.95 of giving a positive result when applied to a person suffering
from a certain disease, and a probability 0.10 of giving a (false) positive when applied to a non-sufferer. It is
estimated that 0.5 % of the population are sufferers. Suppose that the test is now administered to a person about
whom we have no relevant information relating to the disease (apart from the fact that he/she comes from this
population). Calculate the following probabilities:
(a) that the test result will be positive;
(b) that, given a positive result, the person is a sufferer;
(c) that, given a negative result, the person is a non-sufferer;
(d) that the person will be misclassified.

"""

prob_positive_given_suffering = 0.95
prob_negative_given_suffering = 0.10

prob_positive_given_not_suffering = 0.9
prob_negative_given_not_suffering = 0.05

prob_suffering = 0.5
prob_not_suffering = 0.5

prob_positive = prob_suffering * prob_positive_given_suffering + prob_not_suffering * prob_positive_given_not_suffering
print("probability of getting positive result ", prob_positive)


prob_negative = prob_suffering * prob_negative_given_suffering + prob_not_suffering * prob_negative_given_not_suffering
prob_suffering_given_positive = (prob_suffering * prob_positive_given_suffering) / prob_positive
print("Probability of negative result ", prob_suffering_given_positive)

prob_not_suffering_given_negative = (prob_not_suffering * prob_negative_given_not_suffering) / prob_negative
print("Probability of not suffering when result is negative ", prob_not_suffering_given_negative)

prob_misclassified = (prob_not_suffering * prob_positive_given_not_suffering) + (prob_not_suffering * prob_negative_given_not_suffering)
print("probability of getting misclassified result ",prob_misclassified)