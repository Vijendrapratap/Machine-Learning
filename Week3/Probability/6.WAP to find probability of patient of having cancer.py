
"""Given the following statistics, write a program to find the probability that a woman has cancer if she
 has a positive mammogram result?
 		a. One percent of women over 50 have breast cancer.
 		b. Ninety percent of women who have breast cancer test positive on mammograms.
 		c. Eight percent of women will have false positives.
"""

prob_cancer = 0.01
prob_no_cancer = 0.99
prob_positive_cancer_test = 0.9
prob_positive_no_cancer_test = 0.08

total_probability = prob_cancer * prob_positive_cancer_test + prob_no_cancer * prob_positive_no_cancer_test
probability_cancer_given_positive_MMG = (prob_cancer * prob_positive_cancer_test) / total_probability

print("Total probability of having cancer ",probability_cancer_given_positive_MMG)