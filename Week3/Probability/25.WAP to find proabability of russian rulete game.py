"""

Ram plays a game of Russian roulette.
He loads 2 bullets in the adjacent slots of a six slot revolver.
He revolves the cylinder and then pulls the trigger.
Luckily, it is an empty slot.
Ram has an option either to pull the trigger again or to spin the cylinder first and then pull the trigger.
What must Ram choose to maximize his chances of survival?

"""
"""
If the cylinder is spun again, the second pull will be exactly the same risk as the first pull. 
There are two rounds, and six locations. There is a one in three chance that you will die. 
This probability does not change with any number of spins. There is a 66.7% chance (4/6) that ram will not kill.

If the cylinder is not spun, the key to calculating the odds is the clue that the rounds are located in adjacent chambers.
This means that there are two rounds next to each other, 
followed by four blank spaces. We heard a click on the first pull,
which means we are somewhere in the run of these four blank locations. 
Of these four spaces, only one of them is followed by a round. 
There is a one chance in four that we are at this bad location, and 
it means that there is a 3 in 4 chance that the chamber to come is empty.
By not spinning again there is a 75% chance we will live.
"""
probability_without_spin = 1/5

probability_with_spin = 2/5