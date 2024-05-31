# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7202156851185012737-lR3w/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_467 - Generate Min and Max Rows.xlsx'
df = pd.read_excel(file_path, usecols='A:F', skiprows=1)

# Perform data wrangling
dfs = [pd.concat([df[df[x] == min(df[x])], df[df[x] == max(df[x])]]) for x in df.columns[2 : ]]
df = pd.concat(dfs)
df.index = [x for y in df.columns[2 : ] for x in (f'Min {y} row', f'Max {y} row')]

# Display the final results
df
