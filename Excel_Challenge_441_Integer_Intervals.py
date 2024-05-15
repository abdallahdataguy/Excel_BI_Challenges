# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7188748508772909057-9mDb/

import pandas as pd

# Read the Excel file
file_path  = 'Excel_Challenge_441 - Integer Intervals.xlsx'
df = pd.read_excel(file_path)

# Perform data transformation and cleansing
def integer_interval(col):
    chars = col.split(', ')
    numbers = set()
    for char in chars:
        if char.find('-') > -1:
            nums = [int(x) for x in char.split('-')]
            numbers.update([x for x in range(nums[0], nums[1] + 1)])     
        else:
            numbers.add(int(char))
    return ', '.join([str(x) for x in sorted(numbers)])

df['My Answer'] = df['Problem'].apply(integer_interval)

# Display final results
df
