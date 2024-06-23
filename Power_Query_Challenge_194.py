# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7210490795810869248-_kbm/

import pandas as pd

# Read the Excel file
file_path = 'PQ Challenge_194.xlsx'
df = pd.read_excel(file_path, usecols='A:D')

# Perform data wrangling
# Keep the original column names for later use
columns = df.columns
# Add three new columns
cond = df['Amt1'] - df['Amt3'].shift(1)
df['Amt4'] = df['Amt1'].where(pd.isna(cond), cond)
df['Amt5'] = df['Amt2'] - df['Amt1']
df['Amt6'] = df['Amt3'] - df['Amt2']
# Drop the original columns Amt1, Amt2 and Amt3
df = df.iloc[:, [0, 4, 5, 6]]
# Rename the new columns Amt4-6 to Amt1-3
df.columns = columns
    
# Display the final dataset
df
