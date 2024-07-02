# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7213753281066536961-WeNQ/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_490 - Fill Down.xlsx'
df = pd.read_excel(file_path, dtype={'Answer Expected': str})

# Perform data wrangling
df['Order'] = pd.notna(df['Level 1']).cumsum()

values = []
for i in df.index:
    order = df.iat[i, 3]
    if i > 0 and df.iat[i, 3] != df.iat[i - 1, 3]:
        increment = 1
    if pd.isnull(df.iat[i, 1]) or pd.notnull(df.iat[i, 0]):
        values.append(f'{order}')
    else:
        values.append(f'{order}.{increment}')
        increment += 1

df['My Answer'] = values
df['Check'] = df['Answer Expected'] == df['My Answer']
df = df.drop('Order', axis=1).astype(str).replace('nan', '')

# Display the final dataset
df
s