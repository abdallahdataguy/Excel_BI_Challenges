# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7205055956089544704-Nyjv/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_189.xlsx'
df = pd.read_excel(file_path, usecols='A:B')

# Perform data wrangling
df['Result'] = df['Code'].shift(-1)
#df['Result'] = df['Result'].map(lambda x: 'Pass' if x == 'Yes' else 'Fail')
df['Result'] = df['Result'].where(cond=lambda x: df['Result'] == 'Yes' other' = Fail')
df = df[df['Code'] != 'Yes'].reset_index(drop=True)

# Display the final dataset
df
