# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7209404616298442752-DD0P/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_482 - Soccer Result Grid.xlsx'
df = pd.read_excel(file_path, skiprows=1, usecols='A:C')

# Perform data wrangling
values = []
teams = sorted(df['Team 1'].unique())
for t1 in teams:
    value = []
    for t2 in teams:
        condition1 = (df['Team 1'] == t1) & (df['Team 2'] == t2)
        condition2 = (df['Team 1'] == t2) & (df['Team 2'] == t1)
        result1 = df['Result'][condition1].values
        result2 = df['Result'][condition2].values
        if t1 == t2: 
            value.append('X')
        elif len(result1): 
            value.append(result1[0])
        else: 
            value.append('-'.join(result2[0].split('-')[::-1]))
    values.append(value)

df = pd.DataFrame(data=values, columns=teams, index=teams)

# Display the final dataset
df
