"""
Write a program to find probability of drawing an ace from pack of cards
"""

def prob_ace():
    no_ace = 4
    no_cards = 52

    prob_of_ace = no_ace / no_cards
    print("Probability of getting ace from deck of cards : ", prob_of_ace)

prob_ace()