"""
Write a program to find the probability of drawing an ace after drawing a king on the first draw

"""

def probWithreplacement():
    no_cards = 52
    no_kings = 4
    no_ace = 4

    prob_ace = no_ace / no_cards
    prob_king = no_kings / no_cards

    print("Probability of drawing an Ace after drawing a king with replacement : ", prob_ace*prob_king)


def probWithoutreplacement():
    no_cards = 52
    no_kings = 4
    no_ace = 4

    prob_king = no_kings / no_cards
    prob_ace = no_ace / (no_cards-1)

    print("Probability of drawing an Ace after drawing a king without replacement : ", prob_ace * prob_king)

probWithoutreplacement()
probWithreplacement()