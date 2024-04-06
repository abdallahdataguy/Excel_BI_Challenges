# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7182225510289051649-pQ-K/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_171.xlsx'
df = pd.read_excel(file_path, nrows=6, usecols='A:F')

# Transform and clean data
columns = int(df.shape[1] / 2)
values = {'Col1': [], 'Col2': []}
for row in df.iterrows():
    values['Col1'].extend(row[1].values[: columns])
    values['Col2'].extend(row[1].values[columns: ])
df = pd.DataFrame(values)
df.dropna(how='all', inplace=True)
df.reset_index(drop=True, inplace=True)
df.replace(float('nan'), '', inplace=True)

# Print the output
print(df)
