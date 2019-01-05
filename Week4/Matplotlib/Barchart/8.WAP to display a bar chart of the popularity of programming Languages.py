"""
Write a Python programming to display a bar chart of the popularity of programming Languages.
Select the width of each bar and their positions.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

"""
import matplotlib.pyplot as plt
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(languages)]

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n")
plt.xticks(x_pos, languages)

width = [0.1,0.2,0.5,1.1,0.2,0.3]
y_pos = [0,.8,1.5,3,5,6]


plt.bar(y_pos, popularity, width=width)

plt.show()