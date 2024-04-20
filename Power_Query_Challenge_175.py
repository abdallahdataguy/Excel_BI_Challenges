# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7187298942521393153-gI9N/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_175.xlsx'
df = pd.read_excel(file_path, usecols='A:C', nrows=15)

# Perform data transformation and cleansing
dfs = [] # list of data frames
for gen in df['Generation No'].unique():
    dfp = df[df['Generation No'] == gen] # Parent
    dfc = df[df['Generation No'] == gen + 1] # Child
    dfm = dfp.merge(right=dfc, how='inner', on='Family').astype(str) # Merged
    dfm['Relationship'] = dfm['Generation No_x'] + ' - ' + dfm['Generation No_y']
    dfm = dfm.iloc[ : , [0, 1, 3, 5] ]
    dfm.columns = ['Name', 'Family', 'Next Generation', 'Relationship']
    dfs.append(dfm)
df = pd.concat(dfs, ignore_index=True)
df = df.sort_values(by=['Family', 'Relationship', 'Name', 'Next Generation'], ignore_index=True)

# Print the output
print(f'\nFinal Results:\n\n{df}')
