"""
Write a program when
You toss a fair coin three times write a program to find following:
    1.What is the probability of three heads, HHH?
    2.What is the probability that you observe exactly one heads?
    3.Given that you have observed at least one heads, what is the probability that you observe at least two heads?

"""


def probabilityOfEvents():
    sample = {"HHH", "HTT", "HHT", "HTH", "THH", "TTH", "THT", "TTT"}
    event1 = {"HHH"}
    event2 = {"HTT","THT","TTH"}
    event3 = {"HHH", "HTT", "HHT", "HTH", "THH", "TTH", "THT"}
    event4 = {"HHH", "HHT", "HTH", "THH"}

    event5 = event3.intersection(event4)
    prob_intersection = len(event5)/len(sample)

    prob_3Head = len(event1)/len(sample)
    prob_exactly1Head = len(event2)/len(sample)
    prob_atleast1Head = len(event3)/len(sample)

    prob_dependentevent = prob_intersection / prob_atleast1Head


    print("Probability of getting 3 heads is :", prob_3Head)
    print("Probability of getting exactly one head is : ", prob_exactly1Head)
    print("Probability of getting at least two head when we get one head : ", prob_dependentevent)

probabilityOfEvents()

