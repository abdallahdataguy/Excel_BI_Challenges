# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7188748508772909057-9mDb/

import pandas as pd
import re

# Read the Excel file
file_path = 'Excel_Challenge_441 - Integer Intervals.xlsx'
df = pd.read_excel(file_path)

# Perform data transformation and cleansing
def integer_interval(col):
    regex = r'(\d+-\d+)'
    replacement = lambda x: ', '.join([str(y) for y in range(int(x[1].split('-')[0]), int(x[1].split('-')[1]) + 1)])
    text = re.sub(regex, replacement, col)
    numbers = [str(x) for x in sorted({int(y) for y in text.split(', ')})]
    return ', '.join(numbers)

df['My Answer'] = df['Problem'].apply(integer_interval)

# Display final results
df
