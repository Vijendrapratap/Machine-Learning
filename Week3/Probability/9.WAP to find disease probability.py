"""
In a particular pain clinic, 10% of patients are prescribed narcotic pain killers.
Overall, five percent of the clinic’s patients are addicted to narcotics (including pain killers and illegal substances).
Out of all the people prescribed pain pills, 8% are addicts.
If a patient is an addict, write a program to find the  probability that they will be prescribed pain pills?
"""

def prob_of_precribed_painkellers_given_addict(event1,event2,event3,event4):
    total_probability = event1 * event2 + event3 * event4
    probability = (event1*event2)/total_probability
    return probability

prob_prescribed_painkillers = 0.1
prob_non_prescribed_painkillers = 0.9
prob_addicts_given_prescribed_painkillers = 0.08
prob_addicts_given_non_prescribed_painkillers = 0.05


result = prob_of_precribed_painkellers_given_addict(prob_prescribed_painkillers, prob_addicts_given_prescribed_painkillers,
                                                    prob_non_prescribed_painkillers, prob_addicts_given_non_prescribed_painkillers)
print(result)