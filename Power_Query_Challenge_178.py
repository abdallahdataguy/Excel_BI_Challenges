# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7190226035232174080-HNW-/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_178.xlsx'
df = pd.read_excel(file_path, usecols='A:E')

# Perform data transformation and cleansing
values = []
for i in df.index:
    values.append(list(df.iloc[i, [0, 1, 2]]))
    values[-1].insert(1, 'Role')
    values.append(list(df.iloc[i, [0, 3, 4]]))
    values[-1].insert(1, 'Org')

df = pd.DataFrame(values, columns=['Emp', 'Change', 'Old', 'New']).dropna()

# Print the output
print(df)
