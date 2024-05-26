# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7200344905100009472--bbY/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_186.xlsx'
df1 = pd.read_excel(file_path, usecols='A')
df2 = pd.read_excel(file_path, usecols='C:D', nrows=6)

# Perform data wrangling
values = []
for i in df1.index:
    for j in df2.index:
        if abs(df1.iat[i, 0].day - df2.iat[j, 0].day) in [0, 1]:
            values.append([df1.iat[i, 0]] + list(df2.iloc[j, 0:]))
            break
df = pd.DataFrame(values, columns=['Calendar Date', 'Delivery Date', 'Vendor'])
df = df1.merge(df, how='left').astype(str).replace('nan', '').replace('NaT', '')

# Display the final results
print(f'\nResulting data frame has {len(df)} records\n')
df.head(15)
