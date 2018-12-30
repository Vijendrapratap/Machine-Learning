"""
The amount of regular unleaded gasoline purchased every week at a gas station near UCLA
follows the normal distribution
with mean 50000 gallons and standard deviation 10000 gallons.
The starting supply of gasoline is 74000 gallons, and there is a
scheduled weekly delivery of 47000 gallons.
a. Find the probability that, after 11 weeks, the supply of gasoline will be below 20000 gallons.
b. How much should the weekly delivery be so that after 11 weeks the probability that the supply is below 20000 gallons
is only 0.5%?

"""

mean = 50000
no_of_weeks = 11
standard_deviation = 10000
total = 74000 + (11 * 47000)

#supply is below 20000
supply = total - 20000

z_score = (supply - mean * no_of_weeks) / (standard_deviation * no_of_weeks ** 0.5)
print(z_score)
z = 1 - 0.7357
print("probability that, after 11 weeks, the supply of gasoline will be below 20000 gallons is ", z)

z_score = 2.575

supply = (z_score * no_of_weeks ** 0.5 * 10000) + no_of_weeks * mean

total = (supply - 54000) / no_of_weeks

print("Weekly delivery need to be : ",total)