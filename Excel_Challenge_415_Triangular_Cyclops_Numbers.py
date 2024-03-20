# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7175702542939549697-smzf/

import pandas as pd
from math import sqrt

# Read the Excel file
file_path = 'Excel_Challenge_415 - Triangular Cyclops Numbers.xlsx'
df = pd.read_excel(file_path)

# Create a function to generate the
def triangular_cyclops(n):
    numbers = []
    number = 100
    while len(numbers) != n:
        number += 1
        num_str = str(number)
        if len(num_str) % 2:
            single_zero = num_str.count('0') == 1
            middle_zero = num_str[int(len(num_str) / 2)] == '0'
            odd_length = (len(num_str) % 2) == 1
            triangular = False
            for i in range(1, int(sqrt(2 * number)) + 2):
                if i * (i + 1) == 2 * number:
                    triangular = True
                    break
        else:
            continue
        if all([single_zero, middle_zero, odd_length, triangular]):
            numbers.append(number)
    return numbers

df['My Answer'] = pd.Series(triangular_cyclops(100))

print(f'\n{df.head()}\n\n{df.tail()}')

