# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7206505728562388992-OjHF/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_476 - Assigning Sales.xlsx'
df1 = pd.read_excel(file_path, usecols='A:B', skiprows=1, nrows=3)
df2 = pd.read_excel(file_path, usecols='D:E', skiprows=1)
df2 = df2.rename(columns={'Store.1': 'Store'})

# Perform data wrangling
df = pd.merge(df2, df1)
df['Count'] = df.groupby('Store')['Store'].transform('count')
df['Sales'] = (df['Sales'] / df['Count']).astype(int)
df = df.iloc[:, : 3]

# Display the final dataset
df
