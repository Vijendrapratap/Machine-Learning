"""
Write a Python programming to display a horizontal bar chart of the popularity of programming Languages.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

"""

import matplotlib.pyplot as plt


languages = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(languages)]

plt.barh(x_pos, popularity, color='red')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("Popularity of Programming Language\n")

plt.grid()
plt.show()