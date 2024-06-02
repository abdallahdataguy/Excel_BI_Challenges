# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7202881638760955904-dSDC/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_188.xlsx'
df = pd.read_excel(file_path, usecols='A:D', nrows=3)

# Perform data wrangling
dfs = []
for i in df.index:
    date_range = pd.date_range(start=df.iat[i, 1], end=df.iat[i, 2])
    l = len(date_range)
    values = {'Store': [df.iat[i, 0]] * l,
              'Date': date_range,
              'Amount': [df.iat[i, 3]] * l
             }
    dfs.append(pd.DataFrame(values))

df = pd.concat(dfs, ignore_index=True)
df['Quarter'] = df['Date'].map(lambda x: f"Q{x.quarter}-{x.strftime('%y')}")
df['QuarterCount'] = df.groupby(['Store', 'Quarter'])['Quarter'].transform('count')
df['StoreCount'] = df.groupby('Store')['Store'].transform('count')
df['NewAmount'] = df.apply(lambda x: round(x[2] * x[4] / x[5]), axis=1)
df = df.iloc[:, [0, 3, 6]].drop_duplicates(ignore_index=True)
df = df.rename(columns={'NewAmount': 'Amount'})

# Display the final results
df
