# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7187298942521393153-gI9N/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_175.xlsx'
df = pd.read_excel(file_path, usecols='A:C', nrows=15)

# Perform data transformation and cleansing
df = df.merge(df, how='inner', on='Family')
df = df[df['Generation No_x'] == df['Generation No_y'] + 1]
df['Relationship'] = df['Generation No_y'].astype(str) + ' - ' + df['Generation No_x'].astype(str)
df = df.iloc[ : , [3, 1, 0, 5]]
df.columns = ['Name', 'Family', 'Next Generation', 'Relationship']
df = df.sort_values(by=['Family', 'Relationship', 'Name', 'Next Generation'], ignore_index=True)

# Print the output
print(f'\nFinal Results:\n\n{df}')
