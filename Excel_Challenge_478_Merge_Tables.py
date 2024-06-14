# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7207230297556369408-Gifa/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_478 - Merge Tables.xlsx'
df1 = pd.read_excel(file_path, usecols='A:C', skiprows=1, nrows=7)
df2 = pd.read_excel(file_path, usecols='E:H', skiprows=1, nrows=8)

# Perform data wrangling
df2.columns = [x.replace('.1', '') for x in df2.columns]
df = pd.concat([df2, df1])
df['Sales'] = df.groupby(['Org', 'Year'])['Sales'].transform('sum')
df['Prime'] = df.groupby(['Org', 'Year'])['Prime'].transform('ffill')
df = df.drop_duplicates().sort_values(by=['Org', 'Year'], ignore_index=True)
df['Prime'] = df['Prime'].replace(float('nan'), '')

# Display the final output
df
