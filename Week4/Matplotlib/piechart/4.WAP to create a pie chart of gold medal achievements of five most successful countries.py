"""
Write a Python programming to create a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics. Read the data from a csv file.
Sample data:
medal.csv
country,gold_medal
United States,46
Great Britain,27
China,26
Russia,19
Germany,17

"""

import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('medal.csv')
country_data = df["country"]
medal_data = df["gold_medal"]
colors = ["r", "b", "y", "g", "c"]

explode = (0.1, 0.5, 0.2, 0.3, 0.4)
plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
plt.show()