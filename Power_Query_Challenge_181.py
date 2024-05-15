# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7194914135711637504-ePRl/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_181.xlsx'
df = pd.read_excel(file_path, usecols='A:D', header=None, nrows=11).astype(str)

# Perform data transformation and cleansing
df[4] = [x if any(str(y) in x for y in range(10)) else float('nan') for x in df[0]]
df[5] = df.index
df = df.ffill()[~(df[1] == 'Data1')]
df = df.melt(id_vars=[5, 0, 4], value_vars=[1, 2, 3], var_name='Data', value_name='Value')
df = df[df['Value'] != 'nan'].sort_values(by=[5, 'Data'], ignore_index=True)
df = df.astype({0: 'str', 4: 'datetime64', 'Data': 'str', 'Value': 'int'})
df = df.iloc[:, [2, 1, 3, 4]].rename(columns={0: 'Name', 4: 'Date'})
df['Data'] = 'Data' + df['Data']

# Display results
df
