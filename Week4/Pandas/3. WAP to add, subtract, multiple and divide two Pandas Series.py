
"""
Write a Python program to add, subtract, multiple and divide two Pandas Series.

Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
"""

import pandas as pd

series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

add_series = series1 + series2
sub_series = series1 - series2
mul_series = series1 * series2
div_series = series1 / series2

print("Sum of series is ", add_series)
print("Difference of series is ", sub_series)
print("Product of series is ",mul_series)
print("Division of series is", div_series)