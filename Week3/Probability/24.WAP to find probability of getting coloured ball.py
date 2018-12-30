"""
Imagine that you have three urns that you cannot see into.
Urn1 is 90%  green balls	and	10% red. Urn2	is 50%	green and 50% blue. Urn3 is	20% green, 40% red,	and	40%	blue.
You	can’t tell which urn is	which. You	randomly select	an	urn	and	 then randomly	select	a ball	from it.
The	ball you drew is	green.	What is	the	 probability that	it	came	from	urn1?

"""


urn1 = urn2 = urn3 = 1 / 3

prob_green_given_urn1 = 0.9
prob_red_given_urn1 = 0.5


prob_green_given_urn2 = 0.1
prob_blue_given_urn2 = 0.5

prob_green_given_urn3 = 0.2
prob_red_given_urn3 = 0.4
prob_blue_given_urn3 = 0.4

total_probability = (urn1 * prob_green_given_urn1) + (urn2 * prob_green_given_urn2) + (urn3 * prob_green_given_urn3)
prob_urn1_given_green = (urn1 * prob_green_given_urn1) / total_probability


print("Probability of getting green from urn1 is ", prob_urn1_given_green)