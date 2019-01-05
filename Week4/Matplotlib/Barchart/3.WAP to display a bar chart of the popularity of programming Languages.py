"""
Write a Python programming to display a bar chart of the popularity of programming Languages.
Use uniform color.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

"""

import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(languages)]

plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0))

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n")

plt.show()