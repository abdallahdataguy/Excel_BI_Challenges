# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7195271480773926912-6K3j/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_182.xlsx'
df = pd.read_excel(file_path, usecols='A:D').astype(str)

# Perform data transformation and cleansing
df['Order'] = (df['Name'] != df['Name'].shift(1)).cumsum()
items = []
for date in df['Date'].unique():
    items.append([date,  'Data1', 'Data2', 'Data3'])
    tmp =  df[df['Date'] == date]
    tmp = tmp.pivot(index=['Order', 'Name'], columns='Data', values='Value').reset_index()
    items.extend([x for x in tmp.iloc[:, 1:].values])

df = pd.DataFrame(items).astype(str).replace('nan', '')

# Display results
df
