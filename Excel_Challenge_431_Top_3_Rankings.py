# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7183675094450225152-nhNQ/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_431 - Top 3 Rankings.xlsx'
df = pd.read_excel(file_path, usecols='A:H')

# Perform data transformation and cleansing
for col in df.columns[1: ]:
    df[col] = df[col].rank(ascending=False, method='dense').astype(int)

items = {}
for rank in range(1, 4):
    ranks = []
    items[rank] = []
    for row in df.loc[:, :'2024'].iterrows():
        ranks.append(sum([x for x in row[1] if x == rank]))
    df[rank] = pd.Series(ranks)
    regions = df['Region'][df[rank] == max(df[rank])]
    items[rank] = ', '.join(regions)

items = {'Rank': items.keys(), 'Regions':  items.values()}
df = pd.DataFrame(items)

# Print the output
print(df)
