"""
Write a program to find the probability of drawing an ace after drawing an ace on the first draw

"""
def probWithreplacement():
    no_cards = 52
    no_ace = 4

    prob_ace = no_ace / no_cards

    print("Probability of drawing an Ace after drawing a Ace with replacement : ", prob_ace*prob_ace)


def probWithoutreplacement():
    no_cards = 52
    no_ace = 4

    prob_ace = (no_ace-1) / (no_cards-1)

    print("Probability of drawing an Ace after drawing a Ace without replacement : ", prob_ace * prob_ace)

probWithoutreplacement()
probWithreplacement()