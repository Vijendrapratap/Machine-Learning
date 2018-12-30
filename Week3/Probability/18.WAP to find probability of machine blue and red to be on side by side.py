"""
Imagine that, while in Mexico, you also took a side trip to Las Vegas, to pay homage to the
TV show CSI. Late one night in a bar you meet a guy who claims to know that in the casino at
the Tropicana there are two sorts of slot machines: one that pays out 10% of the time, and one
that pays out 20% of the time [note these numbers may not be very realistic]. The two types
of machines are coloured red and blue. The only problem is, the guy is so drunk he can’t quite
remember which colour corresponds to which kind of machine. Unfortunately, that night the guy
becomes the vic in the next CSI episode, so you are unable to ask him again when he’s sober.
Next day you go to the Tropicana to find out more. You find a red and a blue machine side by side.
You toss a coin to decide which machine to try first; based on this you then put the coin into the
red machine. It doesn’t pay out. How should you update your estimate of the probability that this
is the machine you’re interested in? What if it had paid out - what would be your new estimate
then?

"""

p_red = p_blue = 0.5
p_no_win_given_red = 0.8
p_no_win_given_blue = 0.9
p_win_given_red = 1 - p_no_win_given_red
p_win_given_blue = 1 - p_no_win_given_blue

p_red_given_no_win = (p_no_win_given_red * p_red) / (p_no_win_given_red * p_red + p_no_win_given_blue * p_blue)
p_red_given_win =  (p_win_given_red * p_red) / (p_win_given_red * p_red + p_win_given_blue * p_blue)

print(p_red_given_no_win)
print(p_red_given_win)

