# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7182950282429874176-Oida/

import pandas as pd
from math import sqrt
import re

# Read the Excel file
file_path = 'Excel_Challenge_429 - Pythagorean Quadruples.xlsx'
df = pd.read_excel(file_path, usecols='A:B')

# Perform data transformation and cleansing
def pythagorean_quadruples(col):
    number = 0
    result = -1
    while True:
        values = [int(x) for x in re.sub(r'X, |, X', '', col).split(', ')]
        squares = [x ** 2 for x in values]
        if number == sqrt(sum(squares)):
            result = number
            break
        for i in range(len(values)):
            if values[i] == sqrt(sum([x ** 2 for x in (values[: i] + values[i + 1: ])] + [number ** 2])):
                result = number
                break
        if number == result:
            break
        number += 1
    return result

df['My Answer'] = df['Number'].apply(pythagorean_quadruples)

# Print the output
print(f'\nMy Results:\n{df}')
