# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7212303700009111553-JvMr/

import pandas as pd
from itertools import combinations

# Create a function to generate the required combinations
def pairs(numbers, total):
    result = []
    for i in range(1, len(numbers) + 1):
        for c in combinations(numbers, i):
            if sum(c) == total:
                result.append(', '.join([str(x) for x in c]))
    return result

# Read the Excel file
file_path = 'Excel_Challenge_488 - Numbers to Meet Target Sum.xlsx'
df = pd.read_excel(file_path, usecols='C', nrows=4)
df1 = pd.read_excel(file_path, usecols='A')
total = pd.read_excel(file_path, usecols='B', nrows=1).iat[0, 0]

# Perform data wrangling
df['My Answer'] = pairs(df1['Numbers'], total)
df['Check'] = df['My Answer'] == df['Answer Expected']

# Display the final dataset
df
