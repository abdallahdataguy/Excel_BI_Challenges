# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7213027975884111872-fiOU/

import pandas as pd

# Read the Excel file
file_path = 'Downloads\PQ_Challenge_196.xlsx'
df = pd.read_excel(file_path, usecols='A:C')

# Perform data wrangling
df1 = df.pivot(index='Class', columns='Subject', values='Class')
df2 = df.pivot(index='Class', columns='Subject', values='Marks')
df2.columns = ['Marks-' + column for column in df2.columns]
df = pd.concat([df1, df2], axis=1).reset_index(drop=True)
df = df.fillna(0).astype(int).replace(0, '')

# Display the final dataset
df
