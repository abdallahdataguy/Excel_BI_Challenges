# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7211219026939678720-mWrM/

import pandas as pd

# Function to generate an nth pandovan number
def pandovan_number(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 3:
        return 1
    memo[n] = pandovan_number(n - 2, memo) + pandovan_number(n - 3, memo)
    return memo[n]

# Read the Excel file
file_path = 'Excel_Challenge_485 - Pandovan Sequence.xlsx'
df = pd.read_excel(file_path)

# Perform data wrangling
df['My Answer'] = df['n'].map(pandovan_number)
df['Check'] = df['Answer Expectecd'] == df['My Answer']

# Display the final dataset
df
