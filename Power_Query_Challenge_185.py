# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7199994361248428033-8QhI/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_185.xlsx'
df = pd.read_excel(file_path, usecols='A:B')

# Perform data wrangling
df1 = df.drop_duplicates().copy()
df1['Index'] = df1.groupby('Group').cumcount() + 1
df = df1.merge(df)

# Display the final results
df
